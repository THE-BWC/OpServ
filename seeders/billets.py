import logging
from opserv.model import Session, Billet
from sqlalchemy import select
import arrow

log = logging.getLogger(__name__)


def seed_billets():
    billets = [
        Billet(
            id=16,
            name="Administrative Officer",
            game_id=15,
            description="",
            office_id=15,
            taskforce_id=45,
            rank_id=102,
            last_filled_date=arrow.now(),
            retired=False,
        ),
    ]

    for billet in billets:
        if not Session.execute(select(Billet).filter_by(id=billet.id)).scalar():
            Session.add(billet)
            log.info(f"Permission {billet.name} created")

    Session.commit()
    log.info("Billets seeded")
