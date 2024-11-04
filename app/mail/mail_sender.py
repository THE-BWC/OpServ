import sentry_sdk
from flask import render_template
from flask_mail import Mail, Message

mail = Mail()


def send_welcome_email(user):
    msg = Message("Welcome to OpServ", recipients=[user.email])
    try:
        msg.body = render_template("emails/transactional/welcome.txt", user=user)
        msg.html = render_template("emails/transactional/welcome.html", user=user)
        mail.send(msg)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return False


def send_activation_email(user, activation_url):
    email = user.email
    msg = Message(
        "Welcome to OpServ",
        recipients=[email],
    )
    try:
        msg.body = render_template(
            "emails/transactional/activation.txt",
            email=email,
            activation_url=activation_url,
        )
        msg.html = render_template(
            "emails/transactional/activation.html",
            email=email,
            activation_url=activation_url,
        )
        mail.send(msg)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return False


def send_password_reset_email(user, reset_url):
    email = user.email
    msg = Message("Password Reset Request", recipients=[email])
    try:
        msg.body = render_template(
            "emails/transactional/reset_password.txt", email=email, reset_url=reset_url
        )
        msg.html = render_template(
            "emails/transactional/reset_password.html", email=email, reset_url=reset_url
        )
        mail.send(msg)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return False
