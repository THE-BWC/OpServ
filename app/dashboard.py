from flask import render_template, Blueprint, redirect, url_for
from flask_login import current_user
from app.database.main import Session, Game

dashboard_bp = Blueprint(
    name="dashboard", import_name=__name__, template_folder="templates"
)


@dashboard_bp.route("/")
def index():
    if current_user.is_anonymous:
        return redirect(url_for("auth.login"))

    games = Session.query(Game).all()

    return render_template("dashboard/dashboard.html", games=games)
