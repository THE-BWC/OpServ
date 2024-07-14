import arrow
from app.database.main import ModelBase
from app.database.game_model import Game
from app.database.user_model import User
from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import ArrowType


class OperationType(ModelBase):
    __tablename__ = "operation_types"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    tag: Mapped[str] = mapped_column(String(10), nullable=False)
    color_hex: Mapped[str] = mapped_column(String(7), nullable=False)
    live_fire: Mapped[bool] = mapped_column(Integer, default=0)
    retired: Mapped[bool] = mapped_column(Integer, default=0)


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
