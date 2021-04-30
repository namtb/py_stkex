from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date
import config.environment as env

BASE = declarative_base()


class Sector(BASE):
    __tablename__ = "sector"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    code = Column(String(20), nullable=False)
    name_vn = Column(String(200), nullable=True)
    name_en = Column(String(200), nullable=True)
    created_date = Column(DateTime(50), nullable=False)
    last_updated = Column(DateTime(50), nullable=False)


def create_table():
    BASE.metadata.create_all(env.engine)
