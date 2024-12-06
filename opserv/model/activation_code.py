import arrow

from typing import TYPE_CHECKING
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import ArrowType
from opserv.model.meta import _expiration_1h, Model

if TYPE_CHECKING:
    from opserv.model.user import User


class ActivationCode(Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False
    )
    code: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    expired: Mapped[arrow.Arrow] = mapped_column(
        ArrowType, nullable=False, default=_expiration_1h
    )
    user: Mapped["User"] = relationship("User", foreign_keys="ActivationCode.user_id")

    def is_expired(self):
        return self.expired < arrow.now()
