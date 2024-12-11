import logging

from opserv.model.meta import Session, db, EnumE
from opserv.model.activation_code import ActivationCode
from opserv.model.reset_password import ResetPasswordCode
from opserv.model.rank import Rank
from opserv.model.user import User, UserStatus
from opserv.model.game import Game
from opserv.model.enlistment_application import EnlistmentApplication, EnlistmentStatus
from opserv.model.billet import Billet
from opserv.model.operation_type import OperationType
from opserv.model.operation import Operation
from opserv.model.member_game import MemberGames
from opserv.model.audit_user import UserAuditLog
from opserv.model.permission import Permission
from opserv.model.billet_permission import BilletPermission

__all__ = [
    "db",
    "Session",
    "EnumE",
    "User",
    "UserStatus",
    "ActivationCode",
    "ResetPasswordCode",
    "Game",
    "Rank",
    "Billet",
    "Permission",
    "BilletPermission",
    "OperationType",
    "Operation",
    "MemberGames",
    "EnlistmentApplication",
    "EnlistmentStatus",
    "UserAuditLog",
    "init_model",
]

log = logging.getLogger(__name__)


def init_model(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
