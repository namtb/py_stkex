import pandas
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# sample data
# ticket_id = "pow"
# start_date = "2021-01-01"
# end_date = "2021-04-30"
# data = MDailyPrice.get_price_from_to_date(ticket_id, start_date, end_date)
def plot_graph_by_plotly(data):
    if isinstance(data, pandas.DataFrame):
        if not data.empty:
            data['MA9'] = data["close_price"].rolling(9).mean()
            data['MA12'] = data["close_price"].rolling(12).mean()
            data['MA26'] = data["close_price"].rolling(26).mean()

            # data["Status"] = [inc_dec(c, o) for c, o in zip(data["close_price"], data["open_price"])]

            # config appearance
            config = dict({'scrollZoom': True})
            # Create subplots and mention plot grid size
            fig = make_subplots(
                rows=2,
                cols=1,
                shared_xaxes=True,
                vertical_spacing=0.01,
                subplot_titles=('POW 2021', ""),
                row_width=[0.2, 0.7])

            # Plot OHLC on 1st row
            fig.add_trace(go.Candlestick(
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
            fig.update_yaxes(side="right")
            fig.update_xaxes(
                rangebreaks=[
                    dict(bounds=["sat", "mon"]),
                    dict(values=["2021-02-10", "2021-02-11", "2021-02-12", "2021-02-13", "2021-02-14", "2021-02-15",
                                 "2021-02-16"])
                ]
            )

            fig.add_trace(
                go.Scatter(x=data["price_date"], y=data['MA9'], line=dict(color='orange', width=2), name="MA9"))
            fig.add_trace(
                go.Scatter(x=data["price_date"], y=data['MA26'], line=dict(color='purple', width=2), name="MA26"))
            fig.add_trace(
                go.Scatter(x=data["price_date"], y=data['MA12'], line=dict(color='blue', width=2), name="MA212"))

            # Bar trace for volumes on 2nd row without legend
            fig.add_trace(go.Bar(
                x=data['price_date'],
                y=data['volume'],
                marker={'color': "brown"},
                showlegend=False), row=2, col=1)

            # Do not show OHLC's rangeslider plot
            fig.update(layout_xaxis_rangeslider_visible=False)

            fig.update_layout(dragmode='pan', hovermode='x unified',hoverdistance=1)

            fig.update_yaxes(
                showspikes=True,
                spikemode='across',
                spikesnap='cursor',
                showline=True,
                spikedash='dot',
                spikethickness=1,
                showticklabels=True,
                spikecolor="grey"
            )

            fig.update_xaxes(
                showspikes=True,
                spikemode='across',
                spikesnap='cursor',
                showline=True,
                spikedash='dot',
                spikethickness=1,
                spikecolor="grey"
            )

            fig.write_html("test.html", config=config)

            # show on default browser with random port
            fig.show(config=config)


def inc_dec(c, o):
    if c > o:
        value = "Increase"
    elif c < o:
        value = "Decrease"
    else:
        value = "Equal"
    return value