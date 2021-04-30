import  config.environment as env
import mplfinance as mpf
import pandas
import model.MDailyPrice as MDailyPrice

def draw_sample():
    ticket_id = "pow"
    start_date = "2021-01-01"
    end_date = "2021-04-21"

    result = MDailyPrice.get_price_from_to_date(ticket_id, start_date, end_date)

    dataFrame = pandas.DataFrame(result, columns=["price_date", "open_price", "high_price", "low_price", "close_price",
                                                  "volume"])
    dataFrame.rename(columns={"price_date": "Date", "open_price": "Open", "high_price": "High", "low_price": "Low",
                              "close_price": "Close", "volume": "Volume"}, inplace=True)
    dataFrame['Date'] = pandas.to_datetime(dataFrame['Date'])
    dataFrame.set_index('Date', inplace=True)

    print(dataFrame)
    mc = mpf.make_marketcolors(
        up='green',
        down='red',
        volume="inherit",
        ohlc="inherit"
    )

    my_style = mpf.make_mpf_style(
        marketcolors=mc,
        y_on_right=True,
        mavcolors=["green", "purple"]
    )
    mpf.plot(
        dataFrame,
        style=my_style,
        type="candle",
        volume=True,
        title="POW, January-April 2021",
        # style= "charles",
        ylabel="Price (VND)",
        ylabel_lower="Volume",
        datetime_format='%Y-%m-%d',
        mav=(9, 26)
    )
