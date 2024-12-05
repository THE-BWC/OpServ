import secrets

from app.config import BaseConfig
from app.model import Session, ResetPasswordCode
from app.mail import mail_sender


def send_reset_password_email(user):
    """
    Generate a reset password link and send it to the user's email
    """
    reset_password_code = ResetPasswordCode.create(
        user_id=user.id, code=secrets.token_urlsafe(32)
    )
    Session.commit()
    reset_password_link = (
        f"{BaseConfig.URL}/auth/reset_password?code={reset_password_code.code}"
    )
    mail_sender.send_password_reset_email(user, reset_password_link)
