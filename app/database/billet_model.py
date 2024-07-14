from app.database.main import ModelBase
from sqlalchemy import String, Text, Integer, ForeignKey, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import ArrowType
from app.database.rank_model import Rank
from app.database.game_model import Game


class Billet(ModelBase):
    __tablename__ = "billets"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey(Game.id), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    office_id: Mapped[int] = mapped_column(Integer, nullable=True)
    taskforce_id: Mapped[int] = mapped_column(Integer, nullable=True)
    rank_id: Mapped[int] = mapped_column(Integer, ForeignKey(Rank.id), nullable=False)
    last_filled_date = mapped_column(ArrowType, nullable=True)
    # ts3_perms: Mapped[str] = mapped_column(String(255), nullable=True)
    retired: Mapped[bool] = mapped_column(SmallInteger, default=0)
