from enum import Enum

from opserv.model import User, UserAuditLog


class UserAuditLogAction(Enum):
    CreateUser = "create_user"
    ActivateUser = "activate_user"
    ResetPassword = "reset_password"
    EmailVerified = "email_verified"


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
