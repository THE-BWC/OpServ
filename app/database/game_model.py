from app.database.main import ModelBase
from app.database.user_model import User
from sqlalchemy import Integer, String, ForeignKey, SmallInteger, Boolean
from sqlalchemy.orm import Mapped, mapped_column


class Game(ModelBase):
    __tablename__ = "games"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    tag: Mapped[str] = mapped_column(String(10), nullable=False)
    icon: Mapped[str] = mapped_column(String(255), nullable=False)
    retired: Mapped[bool] = mapped_column(Integer, default=0)
    opsec: Mapped[bool] = mapped_column(Integer, default=0)
    opsec_user_group: Mapped[int] = mapped_column(Integer, nullable=True)
    opsec_discord_role: Mapped[str] = mapped_column(String(255), nullable=True)


class MemberGames(ModelBase):
    __tablename__ = "member_games"

    user_id = mapped_column(Integer, ForeignKey(User.id), primary_key=True)
    game_id = mapped_column(Integer, ForeignKey(Game.id), primary_key=True)
    is_primary = mapped_column(Boolean, default=False)
    sort_order = mapped_column(SmallInteger, default=0)
