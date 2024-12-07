from opserv.model import Session, Game, MemberGames


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
        if not Session.query(Game).get(game.id):
            Session.add(game)

    Session.commit()
    print("Games seeded")


def seed_member_games():
    member_games = [
        MemberGames(user_id=1, game_id=15, is_primary=True, sort_order=1),
        MemberGames(user_id=7519, game_id=15, is_primary=True, sort_order=1),
    ]

    for member_game in member_games:
        if not Session.query(MemberGames).get(
            (member_game.user_id, member_game.game_id)
        ):
            Session.add(member_game)

    Session.commit()
    print("Member Games seeded")
