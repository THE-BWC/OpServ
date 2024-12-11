from typing import TYPE_CHECKING, List
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from opserv.model.meta import Model


if TYPE_CHECKING:
    from opserv.model.billet import Billet


class Permission(Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    category_id: Mapped[int] = mapped_column(Integer, nullable=False)
    shown_name: Mapped[str] = mapped_column(String(255), nullable=False)
    sort: Mapped[int] = mapped_column(Integer, nullable=False)

    billets: Mapped[List["Billet"]] = relationship(
        "Billet", secondary="billet_permission", back_populates="permissions"
    )

    def __repr__(self):
        return f"<Permission {self.name}>"
