from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, ValidationError


def star_citizen_validator(form, field):
    # If Star Citizen (16) is selected as the primary game, this field is required
    if form.primary_game.data == "16" and not field.data:
        raise ValidationError("Star Citizen requires this field to be filled out.")


class RecruitForm(FlaskForm):
    primary_game = SelectField("Primary Game", validators=[DataRequired()])
    referred_by = StringField("Referred By")
    country = StringField("Country", validators=[DataRequired()])
    previous_guilds = StringField("Previous Guilds", widget=TextArea())
    why_join = StringField("Why Join?", widget=TextArea(), validators=[DataRequired()])
    experience = StringField("Experience", widget=TextArea())
    other_info = StringField("Other Info", widget=TextArea())
    primary_id = StringField("Primary ID", validators=[DataRequired()])
    steam_id = StringField("Steam ID")
    discord_id = StringField("Discord ID", validators=[star_citizen_validator])
    rsi_handle = StringField("RSI Handle", validators=[star_citizen_validator])
