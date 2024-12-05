import logging
from time import time

from flask import session, redirect, url_for
from flask_login import login_user, LoginManager
from opserv.model import Session, User

login_manager = LoginManager()

log = logging.getLogger(__name__)


@login_manager.user_loader
def load_user(id):
    return Session.query(User).get(id)


def after_login(user, next_url, login_from_oidc: bool = False):
    """
    Redirect user to correct page after login.
    If logged in from OIDC, do not look at otp.
    If MFA enabled, redirect to MFA page.
    Otherwise, redirect to dashboard if no next_url.
    """
    # TODO: Implement OTP and possibly FIDO2

    log.debug("Log user %s in", user.username)
    login_user(user)
    session["sudo_time"] = int(time())

    if not user.recruit_application():
        log.debug("User has no recruit application")
        return redirect(url_for("application.expectation"))

    # User comes to login page from another page
    if next_url:
        log.debug("redirect user to %s", next_url)
        return redirect(next_url)
    else:
        log.debug("redirect user to dashboard")
        return redirect(url_for("dashboard.index"))
