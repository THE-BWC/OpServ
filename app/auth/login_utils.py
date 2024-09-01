from time import time

from flask import session, redirect, url_for
from flask_login import login_user

from app.log import LOG


def after_login(user, next_url, login_from_oidc: bool = False):
    """
    Redirect user to correct page after login.
    If logged in from OIDC, do not look at otp.
    If MFA enabled, redirect to MFA page.
    Otherwise, redirect to dashboard if no next_url.
    """
    # TODO: Implement OTP and possibly FIDO2

    LOG.d("Log user %s in", user)
    login_user(user)
    session["sudo_time"] = int(time())

    # User comes to login page from another page
    if next_url:
        LOG.d("redirect user to %s", next_url)
        return redirect(next_url)
    else:
        LOG.d("redirect user to dashboard")
        return redirect(url_for("dashboard.index"))
