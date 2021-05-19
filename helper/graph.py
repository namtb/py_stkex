import pandas
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class PlotGraph:
    def __init__(self, number_rows, list_titles = []):
        self.titles = list_titles
        self.fig = make_subplots(
                rows=number_rows, cols=1,
                shared_xaxes=True, vertical_spacing=0.01,
                subplot_titles=(self.titles),
                row_heights=[1, 0.3, 0.3, 0.3]
            )

    # Plot the candlestick chart
    def plot_candlestick(self, data):
        if data.empty:
            return False

        self.fig.add_trace(go.Candlestick(
            x=data["price_date"],
            open=data["open_price"],
            high=data["high_price"],
            low=data["low_price"],
            close=data["close_price"],
            name="Candlestick",
            increasing_line_color="#33cc33",
            increasing_fillcolor="#33cc33",
            decreasing_line_color="red",
            decreasing_fillcolor="red"
        ), row=1, col=1)

        self.fig.update_yaxes(side="right")
        self.fig.update_xaxes(
            rangebreaks=[
                dict(bounds=["sat", "mon"]),
                dict(values=["2021-02-10", "2021-02-11", "2021-02-12", "2021-02-13", "2021-02-14", "2021-02-15", "2021-02-16"])
            ]
        )

    # Plot the Bolliger Band graph
    def plot_bolliger_band (self, data):
        if data.empty:
            return False

        # Simple moving average
        data['MA20'] = data["close_price"].rolling(20).mean()

        self.fig.add_trace(
            go.Scatter(x=data["price_date"], y=data['MA20'], line=dict(color='red', width=1, dash='dash'), name="MA20"))

        # Calculate the upper and lower Bollinger Bands
        data["bol_upper"] = data['MA20'] + data['close_price'].rolling(20).std() * 2
        data["bol_lower"] = data['MA20'] - data['close_price'].rolling(20).std() * 2
        self.fig.add_trace(
            go.Scatter(x=data["price_date"], y=data['bol_upper'], fill=None,
                       line=dict(color="rgb(50,205,50,0.3)", width=1), name="bolliger_band_upper"))
        self.fig.add_trace(
            go.Scatter(x=data["price_date"], y=data['bol_lower'], fill='tonexty',
                       line=dict(color="rgb(50,205,50,0.3)", width=1), name="bolliger_band_lower"))

    # Plot the MACD graph
    def plot_MACD (self, data):
        if data.empty:
            return False

        data["EMA_12"] = pandas.Series(data['close_price'].ewm(span=12, min_periods=12).mean())
        data["EMA_26"] = pandas.Series(data['close_price'].ewm(span=26, min_periods=26).mean())
        data["MACD"] = pandas.Series(data["EMA_12"] - data["EMA_26"])
        data["MACD_signal"] = pandas.Series(data["MACD"].ewm(span=9, min_periods=9).mean())
        data["Sub_MACD_9"] = data['MACD'] - data['MACD_signal']

        self.fig.add_trace(go.Scatter(
            x=data["price_date"], y=data['MACD_signal'],
            line=dict(color='blue', width=2), name="signal Line"),
            row=3, col=1
        )
        self.fig.add_trace(go.Scatter(
            x=data["price_date"], y=data['MACD'],
            line=dict(color='red', width=2), name="MACD Line"),
            row=3, col=1
        )
        self.fig.add_trace(go.Scatter(
            x=[data["price_date"].min(), data["price_date"].max()],
            y=[1, 1],
            line=dict(color='purple', width=0.5, dash='dot'),
            name="Positive Amplitude"),
            row=3, col=1
        )
        self.fig.add_trace(go.Scatter(
            x=[data["price_date"].min(), data["price_date"].max()],
            y=[-1, -1],
            line=dict(color='purple', width=0.5, dash='dot'),
            name="Negative Amplitude"),
            row=3, col=1
        )
        self.fig.add_trace(go.Scatter(
            x=[data["price_date"].min(), data["price_date"].max()],
            y=[0, 0],
            line=dict(color='purple', width=1),
            name="Main Coordinate"),
            row=3, col=1
        )
        self.fig.add_trace(go.Bar(
            x=data['price_date'],
            y=data['Sub_MACD_9'],
            marker={'color': "grey"},
            showlegend=False),
            row=3, col=1
        )

    # Plot the volum bar chart
    def plot_volum_chart (self, data):
        if data.empty:
            return False

        data["color"] = "red"
        indx = 0
        for dt in data["color"]:
            if (data["close_price"][indx] - data["open_price"][indx] > 0):
                data.loc[indx, "color"] = "green"
            indx = indx+1

        # Bar trace for volumes on 2nd row without legend
        self.fig.add_trace(go.Bar(
            x=data['price_date'], y=data['volume'],
            marker={'color': data["color"]}, showlegend=False),
            row=2, col=1
        )

    # Plot the RSI chart
    def plot_RSI (self, data):
        if data.empty:
            return False

        data['RSI'] = self.computeRSI(data['close_price'], 14)
        self.fig.add_trace(go.Scatter(
            x=data["price_date"], y=data['RSI'],
            line=dict(color='red', width=2), name="RSI Line"),
            row=4, col=1
        )

        self.fig.add_trace(go.Scatter(
            x=[data["price_date"].min(), data["price_date"].max()],
            y=[30, 30],
            line=dict(color='purple', width=0.5, dash='dot'),
            name="Line 80"),
            row=4, col=1
        )
        self.fig.add_trace(go.Scatter(
            x=[data["price_date"].min(), data["price_date"].max()],
            y=[70, 70],
            line=dict(color="purple", width=0.5, dash='dot'),
            fill="tonexty", fillcolor="rgba(204,51,255,0.3)",
            name="Line 80"),
            row=4, col=1
        )

    # Calculate the RSI values
    def computeRSI(self, data, time_window):
        diff = data.diff(1).dropna()  # diff in one field(one day)

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

    # Plot 4 graphs : Candlestick, bolliger band, MACA , RSI
    def plot_graphs(self, data):
        if isinstance(data, pandas.DataFrame):
            if not data.empty:
                # config appearance
                config = dict({'scrollZoom': True})

                self.plot_candlestick(data)
                self.plot_bolliger_band(data)
                self.plot_MACD(data)
                self.plot_volum_chart(data)
                self.plot_RSI(data)

                self.fig.update(layout_xaxis_rangeslider_visible=False)
                self.fig.update_layout(dragmode='pan', hovermode='x unified', hoverdistance=1)

                self.fig.update_yaxes(
                    showspikes=True, spikemode='across', spikesnap='cursor', showline=True,
                    spikedash='dot', spikethickness=1, showticklabels=True, spikecolor="grey"
                )

                self.fig.update_xaxes(
                    showspikes=True, spikemode='across', spikesnap='cursor', showline=True,
                    spikedash='dot', spikethickness=1, spikecolor="grey"
                )

                # Save graph into file graph.html
                self.fig.write_html("graph.html", config=config)
                # Show on default browser with random port
                self.fig.show(config=config)
