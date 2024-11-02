from enum import Enum

from app.database.models import User, UserAuditLog


class UserAuditLogAction(Enum):
    CreateUser = "craete_user"
    ActivateUser = "activate_user"
    ResetPassword = "reset_password"


def emit_user_audit_log(
    user: User, action: UserAuditLogAction, message: str, commit: bool = False
):
    UserAuditLog.create(
        user_id=user.id,
        username=user.username,
        action=action.value,
        message=message,
        commit=commit,
    )
