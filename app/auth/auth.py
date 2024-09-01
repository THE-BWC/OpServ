import requests

from flask import Blueprint, flash, redirect, url_for, abort, session
from flask_login import LoginManager, login_user, logout_user, current_user
from authlib.integrations.flask_client import OAuth
from app.database.main import db
from app.database.main import User
from app.config import BaseConfig

auth_bp = Blueprint(
    name="auth", import_name=__name__, url_prefix="/auth", template_folder="templates"
)
login_manager = LoginManager()

oauth = OAuth()
discovery_url = f"{BaseConfig.OAUTH2_METADATA_URL}/.well-known/openid-configuration"
oauth.register(
    name="keycloak",
    client_id=BaseConfig.OAUTH2_CLIENT_ID,
    client_secret=BaseConfig.OAUTH2_CLIENT_SECRET,
    server_metadata_url=discovery_url,
    client_kwargs={"scope": BaseConfig.OAUTH2_SCOPE},
)


@login_manager.user_loader
def load_user(id):
    return db.session.query(User).get(id)


# @auth_bp.route("/login")
# def login():
#     if not current_user.is_anonymous:
#         return redirect(url_for("dashboard.index"))
#
#     return render_template("auth/login.html")


@auth_bp.route("/auth")
def authorize():
    redirect_uri = url_for("auth.callback", _external=True)
    return oauth.keycloak.authorize_redirect(redirect_uri)


@auth_bp.route("/callback")
def callback():
    if not current_user.is_anonymous:
        return redirect(url_for("dashboard.index"))

    token = oauth.keycloak.authorize_access_token()
    if token is None:
        abort(404)

    session["tokenResponse"] = token
    user_info = token.get("userinfo")

    # Find or create the user in the database
    user = db.session.query(User).filter_by(email=user_info["email"]).first()
    if user is None:
        user = User(
            email=user_info["email"],
            username=user_info.get(
                "name", user_info.get("preferred_username", user_info["email"])
            ),
        )
        db.session.add(user)
        db.session.commit()

    # Log the user in
    login_user(user)

    return redirect("/")


@auth_bp.route("/logout")
def logout():
    token_response = session.get("tokenResponse")

    if token_response is not None:
        # Propagate logout to Keycloak
        refresh_token = token_response["refresh_token"]
        end_session_endpoint = (
            f"{BaseConfig.OAUTH2_METADATA_URL}/protocol/openid-connect/logout"
        )

        try:
            requests.post(
                end_session_endpoint,
                data={
                    "client_id": BaseConfig.OAUTH2_CLIENT_ID,
                    "client_secret": BaseConfig.OAUTH2_CLIENT_SECRET,
                    "refresh_token": refresh_token,
                },
                timeout=5,
            )
        except requests.exceptions.Timeout:
            flash("Failed to log out of Keycloak.", "error")
        except requests.exceptions.RequestException as e:
            flash(f"Failed to log out of Keycloak: {e}", "error")

    session.pop("tokenResponse", None)
    logout_user()
    flash("You have been logged out.")

    return redirect("/")
