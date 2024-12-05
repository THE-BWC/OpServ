import enum
import arrow

from typing import Optional
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import ArrowType
from opserv.model.meta import Base, Session


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
