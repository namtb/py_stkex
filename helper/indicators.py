from services import MDailyPrice
import pandas


def calculate_moving_average (dataframe_colum, rollback=20):
    return dataframe_colum.rolling(rollback).mean()


def calculate_exponent_moving_average (dataframe_colum, rollback=12):
    return pandas.Series(dataframe_colum.ewm(span=rollback, min_periods=rollback).mean())


def calculate_bolliger_band_distance (dataframe=None, ticker_id="", start_date=None, end_date=None):
    if (ticker_id == "" or start_date is None or end_date is None):
        return False

    if (dataframe is None):
        data = MDailyPrice.get_price_from_to_date(ticker_id, start_date, end_date)
        if data.empty:
            return False
    else:
        data = dataframe

    # Simple moving average
    data['MA_20'] = calculate_moving_average(data["close_price"], rollback=20)

    # Calculate the upper and lower Bollinger Bands
    data["bb_upper"] = data['MA_20'] + data['close_price'].rolling(20).std() * 2
    data["bb_lower"] = data['MA_20'] - data['close_price'].rolling(20).std() * 2
    data["bb_distance"] = data["bb_upper"] - data["bb_lower"]
    # pandas.set_option('display.max_rows', None)
    return data


def calculate_MACD(ticket_id="", start_date=None, end_date=None):
    if (ticket_id == "" or start_date is None or end_date is None):
        return False

    data = MDailyPrice.get_price_from_to_date(ticket_id, start_date, end_date)
    if data.empty:
        return False

    # Colum Data for EMA 12
    data["EMA_12"] = calculate_exponent_moving_average(data['close_price'], rollback=12)
    # Colum Data for EMA 26
    data["EMA_26"] = calculate_exponent_moving_average(data['close_price'], rollback=26)
    # Colum Data for calculating MACD
    data["MACD"] = pandas.Series(data["EMA_12"] - data["EMA_26"])
    # Colum Data for calculating Signal Data
    data["MACD_signal"] = calculate_exponent_moving_average(data['MACD'], rollback=9)
    # Colum Data for calculating histogram barchart
    data["histogram "] = data['MACD'] - data['MACD_signal']

    return data


def calculate_rsi_index(ticket_id="", start_date=None, end_date=None):
    if (ticket_id == "" or start_date is None or end_date is None):
        return False

    data = MDailyPrice.get_price_from_to_date(ticket_id, start_date, end_date)
    if data.empty:
        return False

    data['RSI'] = computeRSI(data['close_price'], time_window=14)

    return data

# Calculate the RSI values
def computeRSI(dataframe, time_window):
    # diff in one field(one day)
    diff = dataframe.diff(1).dropna()

    # this preservers dimensions off diff values
    up_chg = 0 * diff
    down_chg = 0 * diff

    # up change is equal to the positive difference, otherwise equal to zero
    up_chg[diff > 0] = diff[diff > 0]

    # down change is equal to negative deifference, otherwise equal to zero
    down_chg[diff < 0] = diff[diff < 0]

    # check pandas documentation for ewm
    up_chg_avg = up_chg.ewm(com=time_window - 1, min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window - 1, min_periods=time_window).mean()

    rs = abs(up_chg_avg / down_chg_avg)
    rsi = 100 - 100 / (1 + rs)
    return rsi


