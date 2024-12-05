from typing import TYPE_CHECKING

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import LONGTEXT
from opserv.model.base_models import ModelBase
from opserv.model.meta import Session

if TYPE_CHECKING:
    from opserv.model.user import User


class EnlistmentApplication(ModelBase):
    __tablename__ = "enlistment_applications"

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False
    )
    primary_game_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("games.id"), nullable=False
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
        Integer, default=0, nullable=False
    )  # 0 = Pending, 1 = Accepted, 2 = Denied

    user: Mapped["User"] = relationship(
        "User", foreign_keys="EnlistmentApplication.user_id"
    )

    # Check if the user has submitted an application
    @classmethod
    def has_application(cls, user_id: int) -> bool:
        return Session.query(cls).filter(cls.user_id == user_id).first() is not None

    # Get the application status
    @classmethod
    def get_application_status(cls, user_id: int) -> str:
        application = Session.query(cls).filter(cls.user_id == user_id).first()
        if application is not None:
            return application.status
        return "None"
