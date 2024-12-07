import logging

from flask import request, render_template, redirect, url_for, flash, g
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, validators
from sqlalchemy import select

from opserv.auth.base import auth_bp
from opserv.auth.login_utils import after_login
from opserv.config import BaseConfig
from opserv.events.auth_event import LoginEvent
from opserv.limiter import limiter
from opserv.model import Session, User
from opserv.utils import sanitize_email, sanitize_next_url

log = logging.getLogger(__name__)


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[validators.DataRequired()])
    password = StringField("Password", validators=[validators.DataRequired()])


@auth_bp.route("/login", methods=["GET", "POST"])
@limiter.limit(
    "10/minute", deduct_when=lambda r: hasattr(g, "deduct_limit") and g.deduct_limit
)
def login():
    next_url = sanitize_next_url(request.args.get("next"))

    if current_user.is_authenticated:
        if next_url:
            sanitized_next_url = next_url.replace("\r\n", "").replace("\n", "")
            log.debug(
                "User is already authenticated, redirecting to %s", sanitized_next_url
            )
            next_url = sanitize_next_url(next_url)
            return redirect(next_url)
        else:
            log.debug("User is already authenticated, redirecting to dashboard")
            return redirect(url_for("dashboard.index"))

    form = LoginForm(request.form)

    show_resend_activation = False

    if form.validate_on_submit():
        email = sanitize_email(form.email.data)
        user: User = Session.execute(select(User).where(User.email == email)).first()

        if not user or not user.authenticate(form.password.data):
            # Rate limit login attempts
            g.deduct_limit = True
            form.password.data = None
            flash("Invalid email or password", "error")
            LoginEvent(LoginEvent.ActionType.failed).send()
        elif user.date_discharged:
            flash(
                "Your account is disabled. Please contact your COC or S-1 for assistance.",
                "error",
            )
            LoginEvent(LoginEvent.ActionType.disabled_login).send()
        elif not user.email_verified:
            show_resend_activation = True
            flash(
                "Your email is not verified. Please check your email for verification instructions.",
                "error",
            )
            LoginEvent(LoginEvent.ActionType.email_not_verified).send()
        else:
            LoginEvent(LoginEvent.ActionType.success).send()
            return after_login(user, next_url)

    return render_template(
        "auth/login.html",
        form=form,
        next_url=next_url,
        show_resend_activation=show_resend_activation,
        connect_with_oidc=BaseConfig.OAUTH2_CLIENT_ID is not None,
    )
