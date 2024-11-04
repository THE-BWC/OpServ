from flask import render_template, redirect, url_for
from flask_login import current_user
from app.database.models import Session, Game
from app.dashboard.base import dashboard_bp


@dashboard_bp.route("/")
def index():
    if current_user.is_anonymous:
        return redirect(url_for("auth.login"))

    games = Session.query(Game).all()

    return render_template("dashboard/dashboard.html", games=games)
