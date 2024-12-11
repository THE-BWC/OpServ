import logging
from opserv.model import Session, BilletPermission, Billet, Permission
from sqlalchemy import select

log = logging.getLogger(__name__)


def seed_billet_permissions():
    admin_officer: Billet = Session.execute(
        select(Billet).filter_by(name="Administrative Officer")
    ).scalar()
    permission: Permission = Session.execute(
        select(Permission).filter_by(name="can_search_member")
    ).scalar()

    billet_permission = BilletPermission(
        billet_id=admin_officer.id, permission_id=permission.id
    )
    Session.add(billet_permission)
    Session.commit()
    log.info(f"Seeded billet_permission: {billet_permission}")
