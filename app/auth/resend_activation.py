from flask import flash, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.validators import DataRequired

from app.auth.base import auth_bp
from app.auth.register import send_activation_email
from app.database.models import User
from app.log import LOG
from app.utils import sanitize_email


class ResendActivationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])


@auth_bp.route("/resend_activation", methods=["GET", "POST"])
# @limiter.limit("10/hour")
def resend_activation():
    form = ResendActivationForm(request.form)

    if form.validate_on_submit():
        email = sanitize_email(form.email.data)
        user = User.get_by(email=email)

        if not user:
            flash("There is no such email", "warning")
            return render_template("auth/resend_activation.html", form=form)

        if user.email_verified:
            flash("This email is already verified, please login", "success")
            return redirect(url_for("auth.login"))

        LOG.d("User %s is not activated", user)
        flash(
            "An email verification has been sent to you. Please check your inbox/spam folder",
            "warning",
        )
        send_activation_email(user, request.args.get("next"))
        return render_template("auth/register_waiting_activation.html")

    return render_template("auth/resend_activation.html", form=form)
