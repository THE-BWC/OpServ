from app.database.main import Session, Rank
from sqlalchemy.sql import text


def seed_ranks():
    ranks = [
        # Normal ranks
        Rank(
            id=19,
            name="Recruit",
            description="Recruit",
            forum_icon="[FORUM]-Recruit.png",
            fs_icon="[FS]-Recruit.png",
            color_hex="#FFFF00",
        ),
        Rank(
            id=17,
            name="Private",
            description="Private",
            forum_icon="[FORUM]-Private.png",
            fs_icon="[FS]-Private.png",
            color_hex="#FFFF00",
        ),
        Rank(
            id=18,
            name="Private first class",
            description="Private first class",
            forum_icon="[FORUM]-Private-first-class.png",
            fs_icon="[FS]-Private-first-class.png",
            color_hex="#FFFF00",
        ),
        Rank(
            id=24,
            name="Specialist",
            description="Specialist",
            forum_icon="[FORUM]-Specialist.png",
            fs_icon="[FS]-Specialist.png",
            color_hex="#FFFF00",
        ),
        # NBR NCO ranks
        Rank(
            id=10,
            name="Corporal",
            description="Corporal",
            forum_icon="[FORUM]-Corporal.png",
            fs_icon="[FS]-Corporal.png",
            color_hex="#FFA500",
        ),
        Rank(
            id=21,
            name="Sergeant",
            description="Sergeant",
            forum_icon="[FORUM]-Sergeant.png",
            fs_icon="[FS]-Sergeant.png",
            color_hex="#FFA500",
        ),
        Rank(
            id=25,
            name="Staff Sergeant",
            description="Staff Sergeant",
            forum_icon="[FORUM]-Staff-Sergeant.png",
            fs_icon="[FS]-Staff-Sergeant.png",
            color_hex="#FFA500",
        ),
        Rank(
            id=22,
            name="Sergeant first class",
            description="Sergeant first class",
            forum_icon="[FORUM]-Sergeant-First-Class.png",
            fs_icon="[FS]-Sergeant-First-Class.png",
            color_hex="#FFA500",
        ),
        Rank(
            id=16,
            name="Master Sergeant",
            description="Master Sergeant",
            forum_icon="[FORUM]-Master-Sergeant.png",
            fs_icon="[FS]-Master-Sergeant.png",
            color_hex="#FFA500",
        ),
        # Billeted ranks
        Rank(
            id=2,
            name="Lieutenant",
            description="Lieutenant",
            forum_icon="[FORUM]-Lieutenant.png",
            fs_icon="[FS]-Lieutenant.png",
            color_hex="#0276FD",
        ),
        Rank(
            id=3,
            name="Captain",
            description="Captain",
            forum_icon="[FORUM]-Captain.png",
            fs_icon="[FS]-Captain.png",
            color_hex="#0276FD",
        ),
        Rank(
            id=102,
            name="O-2",
            description="O-2",
            forum_icon="[FORUM]-O-2.png",
            fs_icon="[FS]-O-2.png",
            color_hex="#0276FD",
        ),
        Rank(
            id=89,
            name="O-3",
            description="O-3",
            forum_icon="[FORUM]-O-3.png",
            fs_icon="[FS]-O-3.png",
            color_hex="#0276FD",
        ),
        # Command ranks
        Rank(
            id=93,
            name="BWC Yeoman",
            description="BWC Yeoman",
            forum_icon="[FORUM]-BWC-Yeoman.png",
            fs_icon="[FS]-BWC-Yeoman.png",
            color_hex="#32CD32",
        ),
        Rank(
            id=8,
            name="BWC Command Sergeant Major",
            description="BWC Command Sergeant Major",
            forum_icon="[FORUM]-BWC-Command-Sergeant-Major.png",
            fs_icon="[FS]-BWC-Command-Sergeant-Major.png",
            color_hex="#FFA500",
        ),
        Rank(
            id=7,
            name="BWC Executive Officer",
            description="BWC Executive Officer",
            forum_icon="[FORUM]-BWC-Executive-Officer.png",
            fs_icon="[FS]-BWC-Executive-Officer.png",
            color_hex="#0276FD",
        ),
        Rank(
            id=6,
            name="BWC Commanding Officer",
            description="BWC Commanding Officer",
            forum_icon="[FORUM]-BWC-Commanding-Officer.png",
            fs_icon="[FS]-BWC-Commanding-Officer.png",
            color_hex="#FF0000",
        ),
    ]

    Session.execute(text("SET FOREIGN_KEY_CHECKS = 0"))
    for rank in ranks:
        if not Session.query(Rank).get(rank.id):
            Session.add(rank)

    Session.commit()
    Session.execute(text("SET FOREIGN_KEY_CHECKS = 1"))
    print("Ranks seeded")
