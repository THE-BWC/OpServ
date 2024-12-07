from opserv.model import Session, User


def seed_users():
    users = [
        User.create(
            email="admin@example.com", username="Black Widow Company", password="admin"
        ),
        User.create(
            email="patrick@example.com", username="Patrick", password="patrick"
        ),
    ]

    for user in users:
        if not Session.query(User).get(user.id):
            Session.add(user)

    Session.commit()
    print("Users seeded")
