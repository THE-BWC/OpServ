import logging
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from opserv.model import Session, Game, UserStatus
from opserv.dashboard.base import dashboard_bp

log = logging.getLogger(__name__)


@dashboard_bp.route("/")
@login_required
def index():
    if not current_user.state == UserStatus.ACTIVE:
        log.info("User has no recruit application")
        return redirect(url_for("application.enlistment_status"))

    games = Session.query(Game).all()

    return render_template("dashboard/dashboard.html", games=games)
