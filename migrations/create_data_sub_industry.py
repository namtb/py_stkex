import pandas
import config.environment as env

def create():
    excel_file = pandas.ExcelFile('data/sub_industry.xlsx')

    # get the first sheet as an object
    df = pandas.read_excel(excel_file, sheet_name=0)

    # convert datatype to datetime
    df['created_date'] = pandas.to_datetime(df['created_date'])
    df['last_updated'] = pandas.to_datetime(df['last_updated'])

    # Write data from file to database
    try:
        df.to_sql('sub_industry', env.engine, if_exists='append', index=False)
        print("sub_industry data is created successfully !!!")
    except:
        print("sub_industry data is created failed !!!")
        return False

    return True

