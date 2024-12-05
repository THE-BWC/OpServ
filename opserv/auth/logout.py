from flask import redirect, url_for, flash, make_response
from flask_login import logout_user

from opserv.auth.base import auth_bp
from opserv.config import BaseConfig


@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out", "success")
    response = make_response(redirect(url_for("auth.login")))
    response.delete_cookie(BaseConfig.SESSION_COOKIE_NAME)

    return response
