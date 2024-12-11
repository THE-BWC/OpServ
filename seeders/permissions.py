import logging
from opserv.model import Session, Permission
from sqlalchemy import select

log = logging.getLogger(__name__)


def seed_permissions():
    perms = [
        Permission(
            id=1,
            name="can_search_member",
            category_id=1,
            shown_name="Search Members",
            sort=1,
        ),
    ]

    for perm in perms:
        if not Session.execute(select(Permission).filter_by(id=perm.id)).scalar():
            Session.add(perm)
            log.info(f"Permission {perm.name} created")

    Session.commit()
    log.info("Permissions seeded")
