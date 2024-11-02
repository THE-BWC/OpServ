import requests
from flask import request, flash, render_template, redirect, url_for
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, validators

from app.auth.base import auth_bp
from app.config import BaseConfig
from app.events.auth_event import RegisterEvent
from app.log import LOG
from app.database.models import Session, User, ActivationCode
from app.mail import mail_sender
from app.utils import encode_url, random_string


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
        if BaseConfig.TURNSTILE_SECRET:
            token = request.form.get("cf-turnstile-response")
            params = {"secret": BaseConfig.TURNSTILE_SECRET, "response": token}
            hcaptcha_res = requests.post(
                "https://challenges.cloudflare.com/turnstile/v0/siteverify", data=params
            ).json()

            if not hcaptcha_res["success"]:
                LOG.w(
                    "User failed hCaptcha verification: %s %s",
                    form.email.data,
                    hcaptcha_res,
                )
                flash("Wrong Captcha", "error")
                RegisterEvent(RegisterEvent.ActionType.captcha_failed).send()
                return render_template(
                    "auth/register.html",
                    form=form,
                    next_url=next_url,
                    TURNSTILE_SITEKEY=BaseConfig.TURNSTILE_SITEKEY,
                )

        LOG.d("Create user %s", form.email.data)
        user = User.create(
            email=form.email.data,
            username=form.username.data,
            password=form.password.data,
        )
        Session.commit()

        try:
            send_activation_email(user, next_url)
            RegisterEvent(RegisterEvent.ActionType.success).send()
            Session.commit()
        except Exception:
            Session.query(User).filter(User.id == user.id).delete()
            Session.commit()
            flash(
                "Could not send activation email. Are you sure the email is correct?",
                "error",
            )
            RegisterEvent(RegisterEvent.ActionType.invalid_email).send()
            return redirect(url_for("auth.register"))

        return render_template("auth/register_waiting_activation.html")

    return render_template(
        "auth/register.html",
        form=form,
        next_url=next_url,
        TURNSTILE_SITEKEY=BaseConfig.TURNSTILE_SITEKEY,
        connect_with_oidc=BaseConfig.OAUTH2_CLIENT_ID is not None,
    )


def send_activation_email(user, next_url):
    Session.query(ActivationCode).filter(ActivationCode.user_id == user.id).delete()
    activation = ActivationCode.create(user_id=user.id, code=random_string(30))
    Session.commit()

    activation_link = f"{BaseConfig.URL}/auth/activate?code={activation.code}"
    if next_url:
        LOG.d("Redirect user to %s after activation", next_url)
        activation_link = activation_link + "&next=" + encode_url(next_url)

    mail_sender.send_activation_email(user, activation_link)
