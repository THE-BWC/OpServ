from flask import Blueprint

application_bp = Blueprint(
    name="application",
    url_prefix="/application",
    import_name=__name__,
    template_folder="templates",
)
