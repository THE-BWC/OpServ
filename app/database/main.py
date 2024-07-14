import arrow
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy_utils import ArrowType


class ModelBase(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
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


from app.database.user_model import User  # noqa
from app.database.game_model import Game, MemberGames  # noqa
from app.database.operation_model import OperationType, Operation  # noqa
from app.database.rank_model import Rank  # noqa
from app.database.billet_model import Billet  # noqa
