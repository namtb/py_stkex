from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date
import config.environment as env

BASE = declarative_base()


class StockExchange(BASE):
    __tablename__ = "stock_exchange"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    exchange_code = Column(String(20), nullable=False)
    exchange_name_vn = Column(String(200), nullable=True)
    exchange_name_en = Column(String(200), nullable=True)
    currency = Column(String(20), nullable=False)
    created_date = Column(DateTime(50), nullable=False)
    last_updated = Column(DateTime(50), nullable=False)


def create_table():
    BASE.metadata.create_all(env.engine)
