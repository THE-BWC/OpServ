import logging
from opserv.model import Session, User
from sqlalchemy import select

log = logging.getLogger(__name__)


def seed_users():
    admin = User(email="admin@example.com", username="Black Widow Company")  # type: ignore[call-arg]
    admin.set_password("admin")

    patrick = User(id=7519, email="patrick@example.com", username="Patrick")  # type: ignore[call-arg]
    patrick.set_password("patrick")

    if not Session.execute(select(User).filter(User.email == admin.email)).scalar():
        Session.add(admin)

    if not Session.execute(select(User).filter(User.email == patrick.email)).scalar():
        Session.add(patrick)

    Session.commit()
    log.info("Users seeded")
