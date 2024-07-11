from flask_sqlalchemy import SQLAlchemy
from app.database.models import Base

db = SQLAlchemy(model_class=Base)
