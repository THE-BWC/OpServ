import logging

from flask_migrate import Migrate

from app.model.meta import Session, db
from app.model.base_models import EnumE
from app.model.rank import Rank
from app.model.user import User
from app.model.enlistment_application import EnlistmentApplication
from app.model.activation_code import ActivationCode
from app.model.reset_password import ResetPasswordCode
from app.model.game import Game
from app.model.billet import Billet
from app.model.operation_type import OperationType
from app.model.operation import Operation
from app.model.member_game import MemberGames
from app.model.audit_user import UserAuditLog

__all__ = [
    "Session",
    "User",
    "ActivationCode",
    "ResetPasswordCode",
    "Game",
    "Rank",
    "Billet",
    "OperationType",
    "Operation",
    "MemberGames",
    "EnlistmentApplication",
    "UserAuditLog",
    "init_model",
    "EnumE",
]

log = logging.getLogger(__name__)


def init_model(app):
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)
