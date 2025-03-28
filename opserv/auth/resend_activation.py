import logging

from flask import flash, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired
from sqlalchemy import select

from opserv.auth.base import auth_bp
from opserv.auth.register import send_activation_email
from opserv.model import User, Session
from opserv.utils import sanitize_email, limiter

log = logging.getLogger(__name__)


class ResendActivationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])


@auth_bp.route("/resend_activation", methods=["GET", "POST"])
@limiter.limit("10/hour")
def resend_activation():
    form = ResendActivationForm(request.form)

    if form.validate_on_submit():
        email = sanitize_email(form.email.data)
        user: User = Session.execute(select(User).filter(User.email == email)).scalar()

        if not user:
            flash("There is no such email", "warning")
            return render_template("auth/resend_activation.html", form=form)

        if user.email_verified:
            flash("This email is already verified, please login", "success")
            return redirect(url_for("auth.login"))

        log.debug("User %s is not activated", user)
        flash(
            "An email verification has been sent to you. Please check your inbox/spam folder",
            "warning",
        )
        send_activation_email(user, request.args.get("next"))
        return render_template("auth/register_waiting_activation.html")

    return render_template("auth/resend_activation.html", form=form)
