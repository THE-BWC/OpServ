import enum

import arrow
import bcrypt
import unicodedata

from typing import List, Optional
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey, String, Boolean, SmallInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy_utils import ArrowType

from app.utils import sanitize_email

_NORMALIZATION_FORM = "NFKC"


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
Session = db.session


class ModelJunctionBase(Base):
    __abstract__ = True

    created_user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), default=1
    )
    created_at: Mapped[arrow.Arrow] = mapped_column(ArrowType, default=arrow.utcnow)
    edited_user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=True
    )
    edited_at: Mapped[arrow.Arrow] = mapped_column(
        ArrowType, default=arrow.utcnow, onupdate=arrow.utcnow
    )

    _repr_hide = ["created_at", "edited_at"]

    @classmethod
    def query(cls):
        return Session.query(cls)

    @classmethod
    def yield_per_query(cls, page=1000):
        """to be used when iterating on a big table to avoid taking all the memory"""
        return Session.query(cls).yield_per(page).enable_eagerloads(False)

    @classmethod
    def get_by(cls, **kw):
        return Session.query(cls).filter_by(**kw).first()

    @classmethod
    def filter_by(cls, **kw):
        return Session.query(cls).filter_by(**kw)

    @classmethod
    def filter(cls, *args, **kw):
        return Session.query(cls).filter(*args, **kw)

    @classmethod
    def order_by(cls, *args, **kw):
        return Session.query(cls).order_by(*args, **kw)

    @classmethod
    def all(cls):
        return Session.query(cls).all()

    @classmethod
    def count(cls):
        return Session.query(cls).count()

    @classmethod
    def get_or_create(cls, **kw):
        r = cls.get_by(**kw)
        if not r:
            r = cls(**kw)
            Session.add(r)

        return r

    @classmethod
    def create(cls, **kw):
        # Whether to call Session.commit()
        commit = kw.pop("commit", False)
        flush = kw.pop("flush", False)

        r = cls(**kw)
        Session.add(r)

        if commit:
            Session.commit()

        if flush:
            Session.flush()

        return r

    def save(self):
        Session.add(self)

    @classmethod
    def first(cls):
        return Session.query(cls).first()

    def __repr__(self):
        values = ", ".join(
            "%s=%r" % (n, getattr(self, n))
            for n in self.__table__.c.keys()
            if n not in self._repr_hide
        )
        return "%s(%s)" % (self.__class__.__name__, values)


class ModelBase(ModelJunctionBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    @classmethod
    def get(cls, id):
        return Session.query(cls).get(id)

    @classmethod
    def delete(cls, obj_id, commit=False):
        Session.query(cls).filter(cls.id == obj_id).delete()

        if commit:
            Session.commit()


class EnumE(enum.Enum):
    @classmethod
    def has_value(cls, value: int) -> bool:
        return value in set(item.value for item in cls)

    @classmethod
    def get_name(cls, value: int) -> Optional[str]:
        for item in cls:
            if item.value == value:
                return item.name

        return None

    @classmethod
    def get_value(cls, name: str) -> Optional[int]:
        for item in cls:
            if item.name == name:
                return item.value

        return None


class User(UserMixin, ModelBase):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=True)
    rank_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("ranks.id"), nullable=False, default=19
    )
    timezone: Mapped[str] = mapped_column(
        String(255), nullable=False, default="America/New_York"
    )
    rank: Mapped["Rank"] = relationship(
        back_populates="users", foreign_keys="User.rank_id"
    )
    date_activated: Mapped[arrow.Arrow] = mapped_column(ArrowType, nullable=True)
    date_discharged: Mapped[arrow.Arrow] = mapped_column(ArrowType, nullable=True)

    def colorhex(self):
        return self.rank.color_hex

    def set_password(self, password):
        password = unicodedata.normalize(_NORMALIZATION_FORM, password)
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(password.encode(), salt).decode()

    def check_password(self, password):
        if not self.password:
            return False

        password = unicodedata.normalize(_NORMALIZATION_FORM, password)
        return bcrypt.checkpw(password.encode(), self.password.encode())

    @classmethod
    def create(cls, email, username, password=None, **kwargs):
        email = sanitize_email(email)
        user: User = super(User, cls).create(email=email, username=username, **kwargs)  # type: ignore

        if password:
            user.set_password(password)

        return user


class Game(ModelBase):
    __tablename__ = "games"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    tag: Mapped[str] = mapped_column(String(10), nullable=False)
    icon: Mapped[str] = mapped_column(String(255), nullable=False)
    retired: Mapped[bool] = mapped_column(Integer, default=0)
    opsec: Mapped[bool] = mapped_column(Integer, default=0)
    opsec_user_group: Mapped[int] = mapped_column(Integer, nullable=True)
    opsec_discord_role: Mapped[str] = mapped_column(String(255), nullable=True)

    operations: Mapped[List["Operation"]] = relationship(back_populates="game")


class MemberGames(ModelJunctionBase):
    __tablename__ = "member_games"

    user_id: Mapped[int] = mapped_column(ForeignKey(User.id), primary_key=True)
    game_id: Mapped[int] = mapped_column(ForeignKey(Game.id), primary_key=True)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=0)
    sort_order: Mapped[int] = mapped_column(SmallInteger, default=0)


class OperationType(ModelBase):
    __tablename__ = "operation_types"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    tag: Mapped[str] = mapped_column(String(10), nullable=False)
    color_hex: Mapped[str] = mapped_column(String(7), nullable=False)
    live_fire: Mapped[bool] = mapped_column(Integer, default=0)
    retired: Mapped[bool] = mapped_column(Integer, default=0)

    operations: Mapped[List["Operation"]] = relationship(back_populates="type")


class Operation(ModelBase):
    __tablename__ = "operations"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(LONGTEXT, nullable=True)
    is_completed: Mapped[bool] = mapped_column(Integer, default=0)
    type_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(OperationType.id), nullable=False
    )
    date_start: Mapped[arrow.Arrow] = mapped_column(ArrowType, nullable=False)
    date_end: Mapped[arrow.Arrow] = mapped_column(ArrowType, nullable=False)
    leader_user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey(User.id), nullable=False
    )
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey(Game.id), nullable=False)
    # training_id: Mapped[int] = mapped_column(Integer, ForeignKey("trainings.id"), nullable=True)
    aar_notes: Mapped[str] = mapped_column(LONGTEXT, nullable=True)
    is_opsec: Mapped[bool] = mapped_column(Integer, default=0)
    discord_voice_channel: Mapped[str] = mapped_column(String(255), nullable=True)
    discord_event_location: Mapped[str] = mapped_column(String(255), nullable=True)

    type: Mapped["OperationType"] = relationship(back_populates="operations")
    game: Mapped["Game"] = relationship(back_populates="operations")
    leader: Mapped["User"] = relationship(foreign_keys="Operation.leader_user_id")


class Rank(ModelBase):
    __tablename__ = "ranks"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(LONGTEXT, nullable=True)
    forum_icon: Mapped[str] = mapped_column(String(255), nullable=False)
    fs_icon: Mapped[str] = mapped_column(String(255), nullable=False)
    # primary_user_group_id: Mapped[int] = mapped_column(Integer, ForeignKey("user_groups.id"), nullable=False)
    color_hex: Mapped[str] = mapped_column(String(7), nullable=False)
    # ts3_perms: Mapped[str] = mapped_column(String(255), nullable=True)

    users: Mapped[List["User"]] = relationship(
        back_populates="rank", foreign_keys="User.rank_id"
    )
    billets: Mapped[List["Billet"]] = relationship(back_populates="rank")


class Billet(ModelBase):
    __tablename__ = "billets"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey(Game.id), nullable=False)
    description: Mapped[str] = mapped_column(LONGTEXT, nullable=False)
    office_id: Mapped[int] = mapped_column(Integer, nullable=True)
    taskforce_id: Mapped[int] = mapped_column(Integer, nullable=True)
    rank_id: Mapped[int] = mapped_column(Integer, ForeignKey(Rank.id), nullable=False)
    last_filled_date = mapped_column(ArrowType, nullable=True)
    # ts3_perms: Mapped[str] = mapped_column(String(255), nullable=True)
    retired: Mapped[bool] = mapped_column(SmallInteger, default=0)

    rank: Mapped["Rank"] = relationship(back_populates="billets")
