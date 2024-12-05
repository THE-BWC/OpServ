from __future__ import annotations

import arrow
import bcrypt
import unicodedata

from typing import TYPE_CHECKING
from flask_login import UserMixin
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import ArrowType
from opserv.utils import sanitize_email
from opserv.model.base_models import ModelBase
from opserv.model.enlistment_application import EnlistmentApplication
from opserv.model.meta import _NORMALIZATION_FORM

if TYPE_CHECKING:
    from opserv.model.rank import Rank


class User(UserMixin, ModelBase):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(128), nullable=True)
    rank_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("ranks.id"), nullable=False, default=19
    )
    timezone: Mapped[str] = mapped_column(
        String(255), nullable=False, default="America/New_York"
    )
    rank: Mapped["Rank"] = relationship(
        back_populates="users", foreign_keys="User.rank_id"
    )
    email_verified: Mapped[bool] = mapped_column(Boolean, default=0)
    signed_sop: Mapped[bool] = mapped_column(Boolean, default=0)
    referred_by: Mapped[str] = mapped_column(String(255), nullable=True)
    date_activated: Mapped[arrow.Arrow] = mapped_column(ArrowType, nullable=True)
    date_discharged: Mapped[arrow.Arrow] = mapped_column(ArrowType, nullable=True)

    def colorhex(self):
        return self.rank.color_hex

    def set_password(self, password):
        password = unicodedata.normalize(_NORMALIZATION_FORM, password)
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(password.encode(), salt).decode()

    def check_password(self, password):
        if not self.password:
            return False

        password = unicodedata.normalize(_NORMALIZATION_FORM, password)
        return bcrypt.checkpw(password.encode(), self.password.encode())

    @classmethod
    def create(cls, email, username, password=None, **kwargs):
        email = sanitize_email(email)
        user: User = super(User, cls).create(email=email, username=username, **kwargs)  # type: ignore

        if password:
            user.set_password(password)

        return user

    def recruit_application(self):
        return EnlistmentApplication.get_by(user_id=self.id)
