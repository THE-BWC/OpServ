import unicodedata
import bcrypt
from typing import Literal, Final

from app.model import db, User

_NORMALIZATION_FORM: Final[Literal["NFKC"]] = "NFKC"


def create_password(password):
    password = unicodedata.normalize(_NORMALIZATION_FORM, password)
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()


def seed_users():
    users = [
        User(
            id=1,
            username="Black Widow Company",
            email="admin@example.com",
            password=create_password("admin"),
        ),
        User(
            id=7519,
            username="Patrick",
            email="patrick@example.com",
            password=create_password("patrick"),
        ),
    ]

    for user in users:
        if not db.session.query(User).get(user.id):
            db.session.add(user)

    db.session.commit()
    print("Users seeded")
