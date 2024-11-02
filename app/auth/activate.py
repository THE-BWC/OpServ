import arrow

from flask import g, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user

from app.auth.base import auth_bp
from app.database.models import ActivationCode, Session
from app.events.user_audit_log import UserAuditLogAction, emit_user_audit_log
from app.limiter import limiter
from app.log import LOG
from app.mail import mail_sender
from app.utils import sanitize_next_url


@auth_bp.route("/activate", methods=["GET", "POST"])
@limiter.limit(
    "10/minute", deduct_when=lambda r: hasattr(g, "deduct_limit") and g.deduct_limit
)
def activate():
    if current_user.is_authenticated:
        return (
            render_template("auth/activate.html", error="You are already logged in"),
            400,
        )

    code = request.args.get("code")

    activation_code: ActivationCode = ActivationCode.get_by(code=code)

    if not activation_code:
        g.deduct_limit = True
        return (
            render_template("auth/activate.html", error="Activation code missing"),
            400,
        )

    if activation_code.is_expired():
        return (
            render_template(
                "auth/activate.html",
                error="Activation code has expired",
                show_resend_activation=True,
            ),
            400,
        )

    user = activation_code.user
    user.date_activated = arrow.utcnow()
    emit_user_audit_log(
        user=user,
        action=UserAuditLogAction.ActivateUser,
        message=f"User has been activated: {user.username}",
    )
    login_user(user)

    ActivationCode.delete(activation_code.id)
    Session.commit()

    flash("Your account has been activated", "success")

    mail_sender.send_welcome_email(user)

    if "next" in request.args:
        next_url = sanitize_next_url(request.args.get("next"))
        LOG.d("Redirecting to next URL: %s", next_url)
        return redirect(next_url)
    else:
        LOG.d("Redirecting to dashboard")
        return redirect(url_for("dashboard.index"))
