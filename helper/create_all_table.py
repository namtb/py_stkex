from models import models


def create():
    try:
        models.create_table()
        print("daily_price table is created successfully !!!")
        print("security table is created successfully !!!")
        print("stock_exchange table is created successfully !!!")
        print("sector table is created successfully !!!")
        print("industry_group table is created successfully !!!")
        print("industry table is created successfully !!!")
        print("sub_industry table is created successfully !!!")
        print("algorithm table is created successfully !!!")
        print("algorithm_analysis table is created successfully !!!")
        print("algorithm_parameters table is created successfully !!!")
        print("finance_analysis table is created successfully !!!")
        return True
    except:
        print("daily_price table is created failed !!!")
        print("security table is created failed !!!")
        print("stock_exchange table is created failed !!!")
        print("sector table is created failed !!!")
        print("industry_group table is created failed !!!")
        print("industry table is created failed !!!")
        print("sub_industry table is created failed !!!")
        print("algorithm table is created failed !!!")
        print("algorithm_analysis table is created failed !!!")
        print("algorithm_parameters table is created failed !!!")
        print("finance_analysis table is created failed !!!")
        return False
