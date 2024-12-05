from sqlalchemy import String, Integer, Index
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import LONGTEXT
from app.model.base_models import ModelBase


class UserAuditLog(ModelBase):
    __tablename__ = "user_audit_log"

    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    action: Mapped[str] = mapped_column(String(255), nullable=False)
    message: Mapped[str] = mapped_column(LONGTEXT, nullable=True)

    __table_args__ = (
        Index("ix_user_audit_log_user_id", "user_id"),
        Index("ix_user_audit_log_username", "username"),
        Index("ix_user_audit_log_created_at", "created_at"),
    )
