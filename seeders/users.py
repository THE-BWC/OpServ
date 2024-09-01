from app.database.main import db, User


def seed_users():
    users = [
        User(
            id=1,
            username="Black Widow Company",
            email="admin@example.com",
            password="admin",
        ),
        User(
            id=7519, username="Patrick", email="patrick@example.com", password="patrick"
        ),
    ]

    for user in users:
        if not db.session.query(User).get(user.id):
            db.session.add(user)

    db.session.commit()
    print("Users seeded")
