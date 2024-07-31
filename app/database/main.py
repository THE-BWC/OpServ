import arrow
from typing import List
from flask_login import UserMixin
from sqlalchemy import Integer, ForeignKey, String, Text, Boolean, SmallInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy_utils import ArrowType


class ModelJunctionBase(DeclarativeBase):
    __abstract__ = True

    created_user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), default=1
    )
    created_at: Mapped[arrow.Arrow] = mapped_column(ArrowType, default=arrow.utcnow)
    edited_user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=True
    )
    edited_at: Mapped[arrow.Arrow] = mapped_column(
        ArrowType, default=arrow.utcnow, onupdate=arrow.utcnow
    )


class ModelBase(ModelJunctionBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True)


class User(UserMixin, ModelBase):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    rank_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("ranks.id"), nullable=False, default=19
    )

    rank: Mapped["Rank"] = relationship(
        back_populates="users", foreign_keys="User.rank_id"
    )

    def colorhex(self):
        return self.rank.color_hex


class Game(ModelBase):
    __tablename__ = "games"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    tag: Mapped[str] = mapped_column(String(10), nullable=False)
    icon: Mapped[str] = mapped_column(String(255), nullable=False)
    retired: Mapped[bool] = mapped_column(Integer, default=0)
    opsec: Mapped[bool] = mapped_column(Integer, default=0)
    opsec_user_group: Mapped[int] = mapped_column(Integer, nullable=True)
    opsec_discord_role: Mapped[str] = mapped_column(String(255), nullable=True)

    operations: Mapped[List["Operation"]] = relationship(back_populates="game")


class MemberGames(ModelJunctionBase):
    __tablename__ = "member_games"

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id), primary_key=True)
    game_id: Mapped[int] = mapped_column(ForeignKey(Game.id), primary_key=True)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=0)
    sort_order: Mapped[int] = mapped_column(SmallInteger, default=0)


class OperationType(ModelBase):
    __tablename__ = "operation_types"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    tag: Mapped[str] = mapped_column(String(10), nullable=False)
    color_hex: Mapped[str] = mapped_column(String(7), nullable=False)
    live_fire: Mapped[bool] = mapped_column(Integer, default=0)
    retired: Mapped[bool] = mapped_column(Integer, default=0)

    operations: Mapped[List["Operation"]] = relationship(back_populates="type")


class Operation(ModelBase):
    __tablename__ = "operations"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    is_completed: Mapped[bool] = mapped_column(Integer, default=0)
    type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OperationType.id), nullable=False
    )
    date_start: Mapped[arrow.Arrow] = mapped_column(ArrowType, nullable=False)
    date_end: Mapped[arrow.Arrow] = mapped_column(ArrowType, nullable=False)
    leader_user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(User.id), nullable=False
    )
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey(Game.id), nullable=False)
    # training_id: Mapped[int] = mapped_column(Integer, ForeignKey("trainings.id"), nullable=True)
    aar_notes: Mapped[str] = mapped_column(Text, nullable=True)
    is_opsec: Mapped[bool] = mapped_column(Integer, default=0)
    discord_voice_channel: Mapped[str] = mapped_column(String(255), nullable=True)
    discord_event_location: Mapped[str] = mapped_column(String(255), nullable=True)

    type: Mapped["OperationType"] = relationship(back_populates="operations")
    game: Mapped["Game"] = relationship(back_populates="operations")
    leader: Mapped["User"] = relationship(foreign_keys="Operation.leader_user_id")


class Rank(ModelBase):
    __tablename__ = "ranks"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    forum_icon: Mapped[str] = mapped_column(String(255), nullable=False)
    fs_icon: Mapped[str] = mapped_column(String(255), nullable=False)
    # primary_user_group_id: Mapped[int] = mapped_column(Integer, ForeignKey("user_groups.id"), nullable=False)
    color_hex: Mapped[str] = mapped_column(String(7), nullable=False)
    # ts3_perms: Mapped[str] = mapped_column(String(255), nullable=True)

    users: Mapped[List["User"]] = relationship(
        back_populates="rank", foreign_keys="User.rank_id"
    )
    billets: Mapped[List["Billet"]] = relationship(back_populates="rank")


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

    rank: Mapped["Rank"] = relationship(back_populates="billets")
