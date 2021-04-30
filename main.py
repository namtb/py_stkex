from datetime import datetime
import pprint
import pandas
from model import MDailyPrice
from helper import graph
from helper import get_data
from model import MSecurity


def main():
    print("Main Function")
    get_data.get_data_from_ssi_board()
    # ticket_id = "pow"
    # start_date = "2021-01-01"
    # end_date = "2021-04-30"
    # result = MDailyPrice.get_price_from_to_date(ticket_id, start_date, end_date)
    # graph.plot_graph_by_plotly(result)
    # test = MSecurity.get_security_by_sector("40")
    # print(test)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
