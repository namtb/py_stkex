import pandas
from datetime import datetime
from sqlalchemy import and_, or_, not_,asc, desc
from sqlalchemy.sql import text
import config.environment as env
from models.models import FinanceAnalysis
from models.models import DailyPrice

def get_finance_information_by_tickerID(ticker_id):
    query_sql = text("select fa.* from finance_analysis as fa "
                     "left join daily_price as da ON da.ticker_id = fa.ticker_id "
                     "where fa.ticker_id='POW' and fa.year='2019' and fa.quarter='0'")
    result = pandas.DataFrame(env.engine.connect().execute(query_sql))
    print(result)
    return True
