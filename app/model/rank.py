from typing import List, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import LONGTEXT
from app.model.base_models import ModelBase

if TYPE_CHECKING:
    from app.model.user import User
    from app.model.billet import Billet


class Rank(ModelBase):
    __tablename__ = "ranks"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(LONGTEXT, nullable=True)
    forum_icon: Mapped[str] = mapped_column(String(255), nullable=False)
    fs_icon: Mapped[str] = mapped_column(String(255), nullable=False)
    # primary_user_group_id: Mapped[int] = mapped_column(Integer, ForeignKey("user_groups.id"), nullable=False)
    color_hex: Mapped[str] = mapped_column(String(7), nullable=False)
    # ts3_perms: Mapped[str] = mapped_column(String(255), nullable=True)

    users: Mapped[List["User"]] = relationship(
        back_populates="rank", foreign_keys="User.rank_id"
    )
    billets: Mapped[List["Billet"]] = relationship(back_populates="rank")
