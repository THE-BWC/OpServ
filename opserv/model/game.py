from typing import List, TYPE_CHECKING
from sqlalchemy import String, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from opserv.model.base_models import ModelBase

if TYPE_CHECKING:
    from opserv.model.operation import Operation


class Game(ModelBase):
    __tablename__ = "games"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    tag: Mapped[str] = mapped_column(String(10), nullable=False)
    icon: Mapped[str] = mapped_column(String(255), nullable=False)
    retired: Mapped[bool] = mapped_column(Boolean, default=0)
    opsec: Mapped[bool] = mapped_column(Boolean, default=0)
    opsec_user_group: Mapped[int] = mapped_column(Integer, nullable=True)
    opsec_discord_role: Mapped[str] = mapped_column(String(255), nullable=True)

    operations: Mapped[List["Operation"]] = relationship(back_populates="game")
