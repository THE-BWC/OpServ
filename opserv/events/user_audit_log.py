from enum import Enum

from opserv.model import User, UserAuditLog, Session


class UserAuditLogAction(Enum):
    CreateUser = "create_user"
    ActivateUser = "activate_user"
    ResetPassword = "reset_password"
    EmailVerified = "email_verified"


def emit_user_audit_log(user: User, action: UserAuditLogAction, message: str):
    audit = UserAuditLog(
        user_id=user.id, username=user.username, action=action.value, message=message
    )
    Session.add(audit)
    Session.commit()
