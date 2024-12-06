import arrow
import enum

from typing import Final, Literal, Optional
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy_utils import ArrowType
from flask_sqlalchemy import SQLAlchemy

_NORMALIZATION_FORM: Final[Literal["NFKC"]] = "NFKC"


def _expiration_1h():
    return arrow.now().shift(hours=1)


class Base(DeclarativeBase):
    created_user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id"), default=1
    )
    created_at: Mapped[arrow.Arrow] = mapped_column(ArrowType, default=arrow.utcnow)
    edited_user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id"), nullable=True
    )
    edited_at: Mapped[arrow.Arrow] = mapped_column(
        ArrowType, default=arrow.utcnow, onupdate=arrow.utcnow
    )


class EnumE(enum.Enum):
    @classmethod
    def has_value(cls, value: int) -> bool:
        return value in set(item.value for item in cls)

    @classmethod
    def get_name(cls, value: int) -> Optional[str]:
        for item in cls:
            if item.value == value:
                return item.name

        return None

    @classmethod
    def get_value(cls, name: str) -> Optional[int]:
        for item in cls:
            if item.name == name:
                return item.value

        return None


db = SQLAlchemy(model_class=Base)
Model = db.Model
Session = db.session
