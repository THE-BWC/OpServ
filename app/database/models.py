import arrow
from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy_utils import ArrowType
from flask_login import UserMixin


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), default=1)
    created_at: Mapped[arrow.Arrow] = mapped_column(ArrowType, default=arrow.utcnow)
    edited_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=True)
    edited_at: Mapped[arrow.Arrow] = mapped_column(ArrowType, default=arrow.utcnow, onupdate=arrow.utcnow)


class User(UserMixin, Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)


class Operation(Base):
    __tablename__ = "operations"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    is_completed: Mapped[bool] = mapped_column(Integer, default=0)
    type_id: Mapped[int] = mapped_column(Integer, ForeignKey("operation_types.id"), nullable=False)
    date_start: Mapped[arrow.Arrow] = mapped_column(ArrowType, nullable=False)
    date_end: Mapped[arrow.Arrow] = mapped_column(ArrowType, nullable=False)
    leader_user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey("games.id"), nullable=False)
    # training_id: Mapped[int] = mapped_column(Integer, ForeignKey("trainings.id"), nullable=True)
    aar_notes: Mapped[str] = mapped_column(Text, nullable=True)
    is_opsec: Mapped[bool] = mapped_column(Integer, default=0)
    discord_voice_channel: Mapped[str] = mapped_column(String(255), nullable=True)
    discord_event_location: Mapped[str] = mapped_column(String(255), nullable=True)


class OperationType(Base):
    __tablename__ = "operation_types"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    tag: Mapped[str] = mapped_column(String(10), nullable=False)
    color_hex: Mapped[str] = mapped_column(String(7), nullable=False)
    live_fire: Mapped[bool] = mapped_column(Integer, default=0)
    retired: Mapped[bool] = mapped_column(Integer, default=0)


class Game(Base):
    __tablename__ = "games"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    tag: Mapped[str] = mapped_column(String(10), nullable=False)
    icon: Mapped[str] = mapped_column(String(255), nullable=False)
    retired: Mapped[bool] = mapped_column(Integer, default=0)
    opsec: Mapped[bool] = mapped_column(Integer, default=0)
    opsec_user_group: Mapped[int] = mapped_column(Integer, nullable=True)
    opsec_discord_role: Mapped[str] = mapped_column(String(255), nullable=True)
