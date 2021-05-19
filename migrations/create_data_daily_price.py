import pandas
import config.environment as env
from mysql.connector import Error

def create():
    excel_file = pandas.ExcelFile('data/daily_price.xlsx')

    # get the first sheet as an object
    df = pandas.read_excel(excel_file, sheet_name=0)

    # convert datatype to datetime
    df['price_date'] = pandas.to_datetime(df['price_date'], format='%Y%m%d')
    df['created_date'] = pandas.to_datetime(df['created_date'])
    df['last_updated'] = pandas.to_datetime(df['last_updated'])

    # Write data from file to database
    try:
        df.to_sql('daily_price', env.engine, if_exists="append", index=False)
        print("daily_price data is created successfully !!!")

    except Error as e:
        print(e)
        print("daily_price data is created failed !!!")
        return False

    return True
