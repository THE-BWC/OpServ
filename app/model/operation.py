import arrow

from typing import TYPE_CHECKING
from sqlalchemy import String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import ArrowType
from sqlalchemy.dialects.mysql import LONGTEXT
from app.model.base_models import ModelBase

if TYPE_CHECKING:
    from app.model.user import User
    from app.model.game import Game
    from app.model.operation_type import OperationType


class Operation(ModelBase):
    __tablename__ = "operations"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(LONGTEXT, nullable=True)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=0)
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
    aar_notes: Mapped[str] = mapped_column(LONGTEXT, nullable=True)
    is_opsec: Mapped[bool] = mapped_column(Boolean, default=0)
    discord_voice_channel: Mapped[str] = mapped_column(String(255), nullable=True)
    discord_event_location: Mapped[str] = mapped_column(String(255), nullable=True)

    type: Mapped["OperationType"] = relationship(back_populates="operations")
    game: Mapped["Game"] = relationship(back_populates="operations")
    leader: Mapped["User"] = relationship(foreign_keys="Operation.leader_user_id")
