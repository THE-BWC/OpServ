from flask import Blueprint

dashboard_bp = Blueprint(
    name="dashboard", import_name=__name__, template_folder="templates"
)
