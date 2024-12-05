import arrow
from opserv.model import db, Operation, OperationType


def seed_operation_types():
    operation_type = [
        OperationType(id=1, name="Training", tag="TRAINING", color_hex="#FF0000"),
        OperationType(
            id=2, name="Field Training Exercise", tag="FTX", color_hex="#E5E500"
        ),
        OperationType(
            id=3, name="Operation", tag="OP", color_hex="#008000", live_fire=True
        ),
        OperationType(
            id=4,
            name="24 Hour Operation",
            tag="24H",
            color_hex="#008080",
            live_fire=True,
            retired=True,
        ),
        OperationType(id=5, name="Meeting", tag="*MTG*", color_hex="#FFFFFF"),
        OperationType(
            id=6, name="Forum Warrior", tag="FW", color_hex="#FF00FF", live_fire=True
        ),
        OperationType(
            id=7,
            name="BWC Legendary Operations",
            tag="LegOP",
            color_hex="#FFA500",
            live_fire=True,
        ),
        OperationType(
            id=8, name="Joint Operation", tag="JO", color_hex="#808080", live_fire=True
        ),
        OperationType(id=9, name="Meetup", tag="MEET", color_hex="#0099FF"),
        OperationType(
            id=11,
            name="Epic Operation",
            tag="EPIC",
            color_hex="#B03BFF",
            live_fire=True,
        ),
        OperationType(
            id=14,
            name="24 Hour Paintball",
            tag="24PB",
            color_hex="#008080",
            live_fire=True,
            retired=True,
        ),
        OperationType(id=15, name="Intoxi OP", tag="INTOXI", color_hex="#FFFFFF"),
        OperationType(
            id=16,
            name="Beta Operation",
            tag="BETA",
            color_hex="#FF66FF",
            live_fire=True,
        ),
        OperationType(id=17, name="Social Event", tag="SOC", color_hex="#ADD8E6"),
        OperationType(id=18, name="Tournaments", tag="TRNY", color_hex="#7FBF7F"),
        OperationType(
            id=19,
            name="Combined Arms Operations",
            tag="CAOP",
            color_hex="#9365B8",
            live_fire=True,
        ),
    ]

    for operation in operation_type:
        if not db.session.query(OperationType).get(operation.id):
            db.session.add(operation)

    db.session.commit()
    print("Operation Types seeded")


def seed_operations():
    operations = [
        Operation(
            id=1,
            name="Operation: Black Widow Company Training",
            description="This is a training operation for BWC members.",
            type_id=1,
            date_start=arrow.get("2025-06-01T19:00:00"),
            date_end=arrow.get("2025-06-01T21:00:00"),
            leader_user_id=1,
            game_id=15,
        )
    ]

    for operation in operations:
        if not db.session.query(Operation).get(operation.id):
            db.session.add(operation)

    db.session.commit()
    print("Operations seeded")
