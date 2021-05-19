import pandas
import config.environment as env
import os

def create():
    # excel_file = get_all_excel_files()
    excel_file = {
        "algorithm_analysis": "algorithm_analysis.xlsx",
        "algorithm_parameters": "algorithm_parameters.xlsx"
    }
    keys = list(excel_file.keys())
    datetime_fields = ["created_date", "updated_date", "birth_date", "enter_date", "matching_date"]
    date_fields = ["price_date"]

    for key in keys:
        dataframe = pandas.read_excel("data/"+excel_file[key], sheet_name=key)
        for i, column in enumerate(dataframe):
            if (column in date_fields):
                dataframe[column] = pandas.to_datetime(dataframe[column], format='%Y%m%d')
            if (column in datetime_fields):
                dataframe[column] = pandas.to_datetime(dataframe[column])

        # Write data from file to database
        try:
            dataframe.to_sql(key, env.engine, if_exists='append', index=False)
            print(key+" data is created successfully !!!")
        except EnvironmentError:
            print(EnvironmentError)
            print(key+" data is created failed !!!")
            return False

    return True


def get_all_excel_files():
    files = {}
    files_path = os.listdir("data")
    for file in files_path:
        excel_file = pandas.ExcelFile("data/"+file)
        sheet_name = excel_file.sheet_names[0]
        files[sheet_name] = file

    return files