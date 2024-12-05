import arrow

from typing import TYPE_CHECKING
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import ArrowType
from opserv.model.base_models import ModelBase
from opserv.model.meta import _expiration_1h

if TYPE_CHECKING:
    from opserv.model.user import User


class ActivationCode(ModelBase):
    __tablename__ = "activation_code"

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False
    )
    code: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)

    user: Mapped["User"] = relationship("User", foreign_keys="ActivationCode.user_id")

    expired: Mapped[arrow.Arrow] = mapped_column(
        ArrowType, nullable=False, default=_expiration_1h
    )

    def is_expired(self):
        return self.expired < arrow.now()
