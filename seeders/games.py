from app.database.main import db, Game, MemberGames


def seed_games():
    games = [
        Game(
            id=15,
            name="Black Widow Company",
            tag="BWC",
            icon="[BWC]-Black-Widow-Company.png",
        ),
    ]

    for game in games:
        if not db.session.query(Game).get(game.id):
            db.session.add(game)

    db.session.commit()
    print("Games seeded")


def seed_member_games():
    member_games = [
        MemberGames(user_id=1, game_id=15, is_primary=True, sort_order=1),
        MemberGames(user_id=7519, game_id=15, is_primary=True, sort_order=1),
    ]

    for member_game in member_games:
        if not db.session.query(MemberGames).get(
            (member_game.user_id, member_game.game_id)
        ):
            db.session.add(member_game)

    db.session.commit()
    print("Member Games seeded")
