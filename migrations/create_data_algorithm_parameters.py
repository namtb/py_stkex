import pandas
import config.environment as env

def create():
    excel_file = pandas.ExcelFile('data/algorithm_parameters.xlsx')

    # get the first sheet as an object
    df = pandas.read_excel(excel_file, sheet_name=0)

    # convert datatype to datetime
    df["matching_date"] = pandas.to_datetime(df["matching_date"])
    df['created_date'] = pandas.to_datetime(df['created_date'])
    df['last_updated'] = pandas.to_datetime(df['last_updated'])

    # Write data from file to database
    try:
        df.to_sql('algorithm_parameters', env.engine, if_exists='append', index=False)
        print("algorithm_parameters data is created successfully !!!")
    except EnvironmentError:
        print("algorithm_parameters data is created failed !!!")
        return False

    return True

