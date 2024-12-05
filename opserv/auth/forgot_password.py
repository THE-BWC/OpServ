import logging

from flask import request, render_template, flash, g
from flask_wtf import FlaskForm
from wtforms import StringField, validators

from opserv.auth.base import auth_bp
from opserv.dashboard.account_setting import send_reset_password_email
from opserv.limiter import limiter
from opserv.model import User
from opserv.utils import sanitize_email

log = logging.getLogger(__name__)


class ForgotPasswordForm(FlaskForm):
    email = StringField("Email", validators=[validators.DataRequired()])


@auth_bp.route("/forgot_password", methods=["GET", "POST"])
@limiter.limit(
    "10/hour", deduct_when=lambda r: hasattr(g, "deduct_limit") and g.deduct_limit
)
def forgot_password():
    form = ForgotPasswordForm(request.form)

    if form.validate_on_submit():
        g.deuct_limit = True

        flash(
            "If an account with that email exists, a password reset link will be sent to that email.",
            "success",
        )

        email = sanitize_email(form.email.data)
        user = User.get_by(email=email)

        if user:
            log.debug("Send forgot password email to %s", user)
            send_reset_password_email(user)

    return render_template("auth/forgot_password.html", form=form)
