import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date
import config.environment as env

BASE = declarative_base()

class Security(BASE):
    __tablename__ = "security"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    ticker_id = Column(String(20), nullable=False)
    exchange_id = Column(Integer(), nullable=False)
    ticker_name_vn = Column(String(200), nullable=True)
    ticker_name_en = Column(String(200), nullable=True)
    sub_industry_id = Column(String(20), nullable=True)
    created_date = Column(DateTime(50), nullable=False)
    last_updated = Column(DateTime(50), nullable=False)

    def __init__(self, id, ticker_id, exchange_id, ticker_name_vn="", ticker_name_en="",sub_industry_id="", created_date=None, last_updated=None):
        date_format = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.id                 = id
        self.ticker_id          = ticker_id
        self.exchange_id        = exchange_id
        self.ticker_name_vn     = ticker_name_vn
        self.ticker_name_en     = ticker_name_en
        self.sub_industry_id    = sub_industry_id
        self.created_date       = date_format
        self.last_updated       = date_format
        if created_date != None or created_date != "":
            self.created_date   =  created_date
        if last_updated != None or last_updated != "":
            self.last_updated   =  last_updated

    # listOfDicts = {"id": "1", "ticker_id": 10, "exchange_id": "",...},
    @classmethod
    def alternative_init(self, dict_info):
        date_format = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        if not dict_info: return False
        else:
            if (dict_info["id"] != None): self.id = dict_info["id"]
            if (dict_info["ticker_id"] != None): self.ticker_id = dict_info["ticker_id"]
            if (dict_info["exchange_id"] != None): self.exchange_id = dict_info["exchange_id"]
            if (dict_info["ticker_name_vn"] != None): self.ticker_name_vn = dict_info["ticker_name_vn"]
            if (dict_info["ticker_name_en"] != None): self.ticker_name_en = dict_info["ticker_name_en"]
            if (dict_info["sub_industry_id"] != None): self.sub_industry_id = dict_info["sub_industry_id"]
            if (dict_info["created_date"] != ""):
                self.created_date = dict_info["created_date"]
            else:
                self.created_date = date_format

            if (dict_info["last_updated"] != ""):
                self.last_updated = dict_info["last_updated"]
            else:
                self.last_updated = date_format

        return self

def create_table():
    BASE.metadata.create_all(env.engine)
