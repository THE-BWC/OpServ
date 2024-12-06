from typing import TYPE_CHECKING
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy_utils import ArrowType
from opserv.model.meta import Model

if TYPE_CHECKING:
    from opserv.model.rank import Rank


class Billet(Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey("game.id"), nullable=False)
    description: Mapped[str] = mapped_column(LONGTEXT, nullable=False)
    office_id: Mapped[int] = mapped_column(Integer, nullable=True)
    taskforce_id: Mapped[int] = mapped_column(Integer, nullable=True)
    rank_id: Mapped[int] = mapped_column(Integer, ForeignKey("rank.id"), nullable=False)
    last_filled_date = mapped_column(ArrowType, nullable=True)
    # ts3_perms: Mapped[str] = mapped_column(String(255), nullable=True)
    retired: Mapped[bool] = mapped_column(Boolean, default=0)

    rank: Mapped["Rank"] = relationship(back_populates="billets")
