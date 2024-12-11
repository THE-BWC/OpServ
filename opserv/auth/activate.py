import logging
from flask import g, render_template, request, flash
from flask_login import current_user
from sqlalchemy import select

from opserv.auth.base import auth_bp
from opserv.auth.login_utils import after_login
from opserv.model import ActivationCode, Session
from opserv.events.user_audit_log import UserAuditLogAction, emit_user_audit_log
from opserv.mail import mail_sender
from opserv.utils import sanitize_next_url, limiter

log = logging.getLogger(__name__)


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

    activation_code: ActivationCode = (
        Session.execute(select(ActivationCode).filter_by(code=code)).scalars().first()
    )
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
    user.email_verified = True
    emit_user_audit_log(
        user=user,
        action=UserAuditLogAction.EmailVerified,
        message=f"User has verified their email: {user.username} ({user.email})",
    )

    Session.delete(activation_code)
    Session.commit()

    flash("Your email has been verified", "success")

    mail_sender.send_welcome_email(user)

    next_url = sanitize_next_url(request.args.get("next"))
    after_login(user, next_url)
