1. Some necessary libraries:
- pip install pandas
- pip install sqlalchemy
- pip install mysql.connector
- pip install selenium

2. Generate all models class from Database tables.
sqlacodegen mysql+mysqlconnector://root:root@localhost/py_stkex>models.py

3. Plot example graph:
    ticker_id = "tcb"
    start_date = "2019-01-01"
    end_date = "2021-04-30"
    result = MDailyPrice.get_price_from_to_date(ticker_id, start_date, end_date)
    graph_title = ["Techcombank Candlesticks Chart", "", ""]
    my_graph = graph.PlotGraph(4, graph_title)
    my_graph.plot_graphs(result)