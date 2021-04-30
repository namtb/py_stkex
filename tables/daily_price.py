from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Float
import config.environment as env

BASE = declarative_base()


class DailyPrice(BASE):
    __tablename__ = "daily_price"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    ticker_id = Column(String(20), nullable=False)
    price_date = Column(Date(), nullable=False)
    open_price = Column(Float(), nullable=False)
    high_price = Column(Float(), nullable=False)
    low_price = Column(Float(), nullable=False)
    close_price = Column(Float(), nullable=False)
    volume = Column(Integer(), nullable=False)
    created_date = Column(DateTime(50), nullable=False)
    last_updated = Column(DateTime(50), nullable=False)


def create_table():
    BASE.metadata.create_all(env.engine)
