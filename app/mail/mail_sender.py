import sentry_sdk
from flask import render_template
from flask_mail import Mail, Message

mail = Mail()


def send_welcome_email(user):
    subject = "Welcome to OpServ"
    msg = Message(
        subject,
        recipients=[user.email],
    )
    try:
        msg.body = render_template(
            "emails/transactional/welcome.txt", user=user, subject=subject
        )
        msg.html = render_template(
            "emails/transactional/welcome.html", user=user, subject=subject
        )
        mail.send(msg)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return False


def send_activation_email(user, activation_url):
    link = activation_url
    email = user.email
    subject = "Welcome to OpServ"
    msg = Message(
        subject,
        recipients=[email],
    )
    try:
        msg.body = render_template(
            "emails/transactional/activation.txt", email=email, activation_url=link
        )
        msg.html = render_template(
            "emails/transactional/activation.html", email=email, activation_url=link
        )
        mail.send(msg)
    except Exception as e:
        sentry_sdk.capture_exception(e)
        return False
