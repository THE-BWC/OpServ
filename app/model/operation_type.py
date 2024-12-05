from typing import List, TYPE_CHECKING
from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.model.base_models import ModelBase

if TYPE_CHECKING:
    from app.model.operation import Operation


class OperationType(ModelBase):
    __tablename__ = "operation_types"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    tag: Mapped[str] = mapped_column(String(10), nullable=False)
    color_hex: Mapped[str] = mapped_column(String(7), nullable=False)
    live_fire: Mapped[bool] = mapped_column(Boolean, default=0)
    retired: Mapped[bool] = mapped_column(Boolean, default=0)

    operations: Mapped[List["Operation"]] = relationship(back_populates="type")
