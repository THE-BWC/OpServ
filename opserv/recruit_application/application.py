import logging

from flask import render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import BooleanField, validators
from opserv.model import User, Session, EnlistmentApplication, Game
from flask_login import current_user, login_required

from opserv.recruit_application.forms import RecruitForm

from opserv.recruit_application.base import application_bp

log = logging.getLogger(__name__)


class ExpectationForm(FlaskForm):
    accept_sop = BooleanField("I accept the SOP", [validators.DataRequired()])


@application_bp.route("/expectation", methods=["GET", "POST"])
@login_required
def expectation():
    if current_user.signed_sop:
        return redirect(url_for("application.enlist"))

    form = ExpectationForm(request.form)
    if form.validate_on_submit():
        if not form.accept_sop.data:
            flash("You must sign the SOP to continue.")
        else:
            user = User.get_by(id=current_user.id)
            user.signed_sop = True
            Session.commit()
            return redirect(url_for("application.enlist"))

    return render_template(
        "recruit_application/expectation.html",
        form=form,
    )


@application_bp.route("/enlistment-status", methods=["GET"])
@login_required
def enlistment_status():
    app = current_user.recruit_application()

    return render_template(
        "recruit_application/enlistment_status.html", status=app.status
    )


@application_bp.route("/enlist", methods=["GET", "POST"])
@login_required
def enlist():
    user = User.get_by(id=current_user.id)
    app = user.recruit_application()
    if app.status == 0:  # Pending
        return redirect(url_for("application.enlistment_status"))

    if app.status == 1:  # Accepted
        return redirect(url_for("dashboard.index"))

    if app.status == 2:  # Denied
        return redirect(url_for("application.reenlist"))

    form = RecruitForm(request.form)
    games = Game.all()
    form.primary_game.choices = [(game.id, game.name) for game in games]

    if form.validate_on_submit():
        log.debug("Creating enlistment application for user %s", user.username)
        EnlistmentApplication.create(
            user_id=user.id,
            primary_game_id=form.primary_game.data,
            referred_by=form.referred_by.data,
            country=form.country.data,
            previous_guilds=form.previous_guilds.data,
            why_join=form.why_join.data,
            experience=form.experience.data,
            other_info=form.other_info.data,
            primary_id=form.primary_id.data,
            steam_id=form.steam_id.data,
            discord_id=form.discord_id.data,
            rsi_handle=form.rsi_handle.data,
            status=0,
            created_user_id=user.id,
        )
        Session.commit()
        return redirect(url_for("application.enlistment_status"))

    return render_template(
        "recruit_application/enlist.html",
        form=form,
    )


@application_bp.route("/reenlist", methods=["GET", "POST"])
@login_required
def reenlist():
    return "Reenlistment form"
