from sqlalchemy import Column, ForeignKey, Integer
from opserv.model.meta import Model


class BilletPermission(Model):
    __tablename__ = "billet_permission"
    billet_id = Column(Integer, ForeignKey("billet.id"), primary_key=True)
    permission_id = Column(Integer, ForeignKey("permission.id"), primary_key=True)
