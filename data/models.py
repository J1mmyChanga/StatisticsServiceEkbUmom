from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database.main import Database
from .db_session import SqlAlchemyBase


class OrderStatistics(SqlAlchemyBase):
    __tablename__ = 'order_statistics'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dish_id = Column(Integer, ForeignKey('dishs_.id'))
    category = Column(String)
    dish_title = Column(String)
    price = Column(Integer)
    order_day = Column(Date)
    week_day = Column(String)
    weather = Column(String)
    weekend = Column(Boolean)
    callories = Column(Integer)
    proteins = Column(Integer)
    fats = Column(Integer)
    carbohydrates = Column(Integer)
    meat = Column(Boolean)
    raw_food = Column(Boolean)
    lenten_food = Column(Boolean)
    milk_food = Column(Boolean)

    dishs = relationship('Dishs', backref='order_statistics')


class Dishs(SqlAlchemyBase):
    __tablename__ = 'dishs_'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Integer)
    category = Column(String)
    callories = Column(Integer)
    proteins = Column(Integer)
    fats = Column(Integer)
    carbohydrates = Column(Integer)


def register_models():
    Database.BASE.metadata.create_all(Database().engine)