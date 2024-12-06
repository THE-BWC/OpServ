from sqlalchemy import ForeignKey, Boolean, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column
from opserv.model.meta import Model


class MemberGames(Model):
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)
    game_id: Mapped[int] = mapped_column(ForeignKey("game.id"), primary_key=True)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=0)
    sort_order: Mapped[int] = mapped_column(SmallInteger, default=0)
