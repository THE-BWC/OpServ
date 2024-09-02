from flask import request, flash, render_template, redirect, url_for
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, validators

from app.auth.base import auth_bp
from app.config import BaseConfig
from app.events.auth_event import RegisterEvent
from app.log import LOG
from app.database.models import Session, User
from app.utils import sanitize_email


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[validators.DataRequired()])
    email = StringField("Email", validators=[validators.DataRequired()])
    password = StringField(
        "Password",
        validators=[validators.DataRequired(), validators.Length(min=8, max=100)],
    )


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        LOG.d("User is already authenticated, redirecting to dashboard")
        flash("You are already logged in", "warning")
        return redirect(url_for("dashboard.index"))

    if BaseConfig.DISABLE_REGISTRATION:
        flash("Registration is closed", "error")
        return redirect(url_for("auth.login"))

    form = RegisterForm(request.form)
    next_url = request.args.get("next")

    if form.validate_on_submit():
        email = sanitize_email(form.email.data)
        LOG.d("Create user %s", email)
        User.create(
            email=email,
            username=form.username.data,
            password=form.password.data,
        )
        Session.commit()

        try:
            # TODO: Send email
            RegisterEvent(RegisterEvent.ActionType.success).send()
            Session.commit()
        except Exception:
            flash("Invalid email, are you sure the email is correct?", "error")
            RegisterEvent(RegisterEvent.ActionType.invalid_email).send()
            return redirect(url_for("auth.register"))

        return render_template("auth/register_waiting_activation.html")

    return render_template(
        "auth/register.html",
        form=form,
        next_url=next_url,
    )
