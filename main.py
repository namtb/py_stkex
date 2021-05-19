import pandas
from helper import indicators
from services import MAlgorithmParameters

from migrations import create_data_daily_price as table



def main():
    print("Main Function")

    ticker_id = "pow"
    start_date = "2021-01-01"
    end_date = "2021-04-30"
    result = indicators.calculate_bolliger_band_distance(ticker_id=ticker_id, start_date=start_date, end_date=end_date)
    parameters = MAlgorithmParameters.get_algorithm_parameters_for_tickerid(ticker_id=ticker_id)

    result["result"] = ""
    for index, row in result.iterrows():
        result.loc[index, "result"] = False
        if(row["bb_distance"] > float(parameters["bb_hoi_tu"]) and row["bb_distance"] < float(parameters["bb_phan_ky"])):
            result.loc[index, "result"] = True
    pandas.set_option('display.max_rows', None)
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()



