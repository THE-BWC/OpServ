import arrow

from typing import Final, Literal
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy

_NORMALIZATION_FORM: Final[Literal["NFKC"]] = "NFKC"


def _expiration_1h():
    return arrow.now().shift(hours=1)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
Session = db.session
