from app.database.main import User
from app.database.db import db


def seed_users():
    users = [
        User(id=1, username="Black Widow Company", email="admin@example.com"),
        User(id=7519, username="Patrick", email="patrick@example.com"),
    ]

    for user in users:
        if not db.session.query(User).get(user.id):
            db.session.add(user)

    db.session.commit()
    print("Users seeded")
