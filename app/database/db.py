from flask_sqlalchemy import SQLAlchemy
from app.database.main import ModelBase

db = SQLAlchemy(model_class=ModelBase)
Session = db.session
