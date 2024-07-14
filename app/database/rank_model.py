from app.database.main import ModelBase
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column


class Rank(ModelBase):
    __tablename__ = "ranks"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    forum_icon: Mapped[str] = mapped_column(String(255), nullable=False)
    fs_icon: Mapped[str] = mapped_column(String(255), nullable=False)
    # primary_user_group_id: Mapped[int] = mapped_column(Integer, ForeignKey("user_groups.id"), nullable=False)
    color_hex: Mapped[str] = mapped_column(String(7), nullable=False)
    # ts3_perms: Mapped[str] = mapped_column(String(255), nullable=True)
