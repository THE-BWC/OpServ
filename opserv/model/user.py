import arrow

from typing import TYPE_CHECKING
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import ArrowType
from opserv.model.meta import Model

if TYPE_CHECKING:
    from opserv.model.rank import Rank
    from opserv.model.enlistment_application import EnlistmentApplication


class User(Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(128), nullable=True)
    rank_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("rank.id"), nullable=False, default=19
    )
    timezone: Mapped[str] = mapped_column(
        String(255), nullable=False, default="America/New_York"
    )
    email_verified: Mapped[bool] = mapped_column(Boolean, default=0)
    signed_sop: Mapped[bool] = mapped_column(Boolean, default=0)
    referred_by: Mapped[str] = mapped_column(String(255), nullable=True)
    date_activated: Mapped[arrow.Arrow] = mapped_column(ArrowType, nullable=True)
    date_discharged: Mapped[arrow.Arrow] = mapped_column(ArrowType, nullable=True)

    rank: Mapped["Rank"] = relationship(
        back_populates="users", foreign_keys="User.rank_id"
    )
    applications: Mapped["EnlistmentApplication"] = relationship(
        "EnlistmentApplication",
        backref="user",
        foreign_keys="EnlistmentApplication.user_id",
    )

    def set_password(self, password: str) -> None:
        self._password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self._password, password)

    serialize_rules = "-_password"
