import pandas
from datetime import datetime
from sqlalchemy import and_, or_, not_,asc, desc
import config.environment as env
from models.models import DailyPrice
from models.models import Security

def get_price_of_security(ticket_id=None):
    query = env.session.query(DailyPrice)
    if (ticket_id is not None):
        query = query.filter(DailyPrice.ticker_id == ticket_id)

    result = pandas.read_sql(query.statement, env.session.bind)
    return result

# sample parameters
# ticket_id = "pow"
# start_date = "2021-04-01"
# end_date = "2021-04-27"
def get_price_from_to_date(ticket_id=None, start_date=None, end_date=None):

    query = env.session.query(DailyPrice)

    if(ticket_id != None and ticket_id != ""):
        query = query.filter(DailyPrice.ticker_id == ticket_id)
    if(start_date != None and start_date != ""):
        start_date_format = datetime.strptime(start_date, "%Y-%m-%d")
        query = query.filter(DailyPrice.price_date >= start_date_format)
    if(end_date != None and end_date != ""):
        end_date_format = datetime.strptime(end_date, "%Y-%m-%d")
        query = query.filter(DailyPrice.price_date <= end_date_format)

    query = query.order_by(asc("price_date"))
    result = pandas.read_sql(query.statement, env.session.bind)
    return result

def get_price_security_belongto_sub_industry(sub_industry_id):
    query = env.session.query(DailyPrice).join(Security, DailyPrice.ticker_id == Security.ticker_id)\
        .filter(Security.sub_industry_id == sub_industry_id)\
        .order_by(asc("price_date"))
    result = pandas.read_sql(query.statement, env.session.bind)
    return result

def get_price_security_belong_to_date(ticker_id=None, listday=[]):
    if (len(listday) == 0 or listday is None):
        return False
    query = env.session.query(DailyPrice).filter(DailyPrice.price_date.in_(listday))
    if (ticker_id != None):
        query = query.filter(DailyPrice.ticker_id == ticker_id)
    result = pandas.read_sql(query.statement, env.session.bind)
    return result
