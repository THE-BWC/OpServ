import enum

from sqlalchemy import String, Integer, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import LONGTEXT
from opserv.model.meta import Model


class EnlistmentStatus(enum.Enum):
    PENDING = 1
    APPROVED = 2
    DENIED = 3


class EnlistmentApplication(Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    primary_game_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("game.id"), nullable=False
    )
    referred_by: Mapped[str] = mapped_column(String(255), nullable=True)
    country: Mapped[str] = mapped_column(String(255), nullable=False)
    previous_guilds: Mapped[str] = mapped_column(LONGTEXT, nullable=True)
    why_join: Mapped[str] = mapped_column(LONGTEXT, nullable=False)
    experience: Mapped[str] = mapped_column(LONGTEXT, nullable=True)
    other_info: Mapped[str] = mapped_column(LONGTEXT, nullable=True)
    primary_id: Mapped[str] = mapped_column(String(255), nullable=True)
    steam_id: Mapped[str] = mapped_column(String(255), nullable=True, unique=True)
    discord_id: Mapped[str] = mapped_column(String(255), nullable=True, unique=True)
    rsi_handle: Mapped[str] = mapped_column(String(255), nullable=True, unique=True)
    status: Mapped[int] = mapped_column(
        Enum(EnlistmentStatus), nullable=False, default=EnlistmentStatus.PENDING
    )
