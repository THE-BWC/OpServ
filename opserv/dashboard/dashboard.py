from flask import render_template
from flask_login import login_required
from opserv.model import Session, Game
from opserv.dashboard.base import dashboard_bp


@dashboard_bp.route("/")
@login_required
def index():
    games = Session.query(Game).all()

    return render_template("dashboard/dashboard.html", games=games)
