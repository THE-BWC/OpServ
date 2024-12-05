from sqlalchemy import ForeignKey, Boolean, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column
from .base_models import ModelJunctionBase
from .user import User
from .game import Game


class MemberGames(ModelJunctionBase):
    __tablename__ = "member_games"

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id), primary_key=True)
    game_id: Mapped[int] = mapped_column(ForeignKey(Game.id), primary_key=True)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=0)
    sort_order: Mapped[int] = mapped_column(SmallInteger, default=0)
