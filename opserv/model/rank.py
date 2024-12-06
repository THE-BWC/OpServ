from typing import List, TYPE_CHECKING
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import LONGTEXT
from opserv.model.meta import Model

if TYPE_CHECKING:
    from opserv.model.user import User
    from opserv.model.billet import Billet


class Rank(Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(LONGTEXT, nullable=True)
    forum_icon: Mapped[str] = mapped_column(String(255), nullable=False)
    fs_icon: Mapped[str] = mapped_column(String(255), nullable=False)
    color_hex: Mapped[str] = mapped_column(String(7), nullable=False)

    users: Mapped[List["User"]] = relationship(
        back_populates="rank", foreign_keys="User.rank_id"
    )
    billets: Mapped[List["Billet"]] = relationship(back_populates="rank")
