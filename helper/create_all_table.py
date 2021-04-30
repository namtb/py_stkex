from tables import daily_price
from tables import security
from tables import stock_exchange
from tables import sector
from tables import industry_group
from tables import industry
from tables import sub_industry

def create():
    try:
        daily_price.create_table()
        security.create_table()
        stock_exchange.create_table()
        sector.create_table()
        industry_group.create_table()
        industry.create_table()
        sub_industry.create_table()
        print("daily_price table is created successfully !!!")
        print("security table is created successfully !!!")
        print("stock_exchange table is created successfully !!!")
        print("sector table is created successfully !!!")
        print("industry_group table is created successfully !!!")
        print("industry table is created successfully !!!")
        print("sub_industry table is created successfully !!!")
        return True
    except:
        print("daily_price table is created failed !!!")
        print("security table is created failed !!!")
        print("stock_exchange table is created failed !!!")
        print("sector table is created successfully !!!")
        print("industry_group table is created successfully !!!")
        print("industry table is created successfully !!!")
        print("sub_industry table is created successfully !!!")
        return False
