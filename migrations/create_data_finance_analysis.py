import pandas
import config.environment as env
from models.finance_analysis import FinanceAnalysis
import os
import services.MDailyPrice as daily_price
import numpy as np

def create ():

    files_path = os.listdir("data/fin_info")
    # files_path = ["bvh_finance_information.csv"]
    year_quarter_list = []
    for yq in env.price_date_quarter.values():
        year_quarter_list.append(yq)

    for file in files_path:
        df_data = pandas.read_csv("data/fin_info/" + file)

        # convert datatype to datetime
        df_data['created_date'] = pandas.to_datetime(df_data['created_date'])
        df_data['last_updated'] = pandas.to_datetime(df_data['last_updated'])

        df_to_dict = pandas.DataFrame.transpose(df_data).to_dict()

        new_security = FinanceAnalysis()

        all_attributes = new_security._props()
        df = pandas.DataFrame(df_to_dict,index=all_attributes).transpose()

        df["von_hoa_thi_truong"] = df["von_hoa_thi_truong"]*1000000000

        # get data from daily_price table
        daily_price_data = daily_price.get_price_security_belong_to_date(ticker_id=file[0:3], listday=year_quarter_list)

        for index, row in df.iterrows():
            fa_year_quarter = str(row["quarter"]) + str(row["year"])
            if (str(row["quarter"]) == "0"):
                fa_year_quarter = "4" +""+ str(row["year"])

            if (env.price_date_quarter.get(fa_year_quarter, None)):
                for key, value in daily_price_data.iterrows():
                    if (str(env.price_date_quarter[fa_year_quarter]) == str(value["price_date"])):
                        df.loc[index,"gia_thi_truong"] = value["close_price"]


        # Write data from file to database
        try:
            df.to_sql('finance_analysis', env.engine, if_exists='append', index=False)
            print("finance analysis data of " + file +  " is created successfully !!!")
        except:
            print("finance analysis data of " + file +  " is created failed !!!")
            return False

    return True

def calculate_finance_indexs (year=None, quarter=None):
    query_year = ["2021", "2020", "2019", "2018", "2017", "2016", "2015"]
    query_quarter = ["0","1", "2", "3", "4"]
    if (year != None):
        if (len(year) > 0):
            query_year = year
        elif (type(year) == str):
            query_year = [year]

    if (quarter != None):
        if (len(quarter) > 0):
            query_quarter = quarter
        elif (type(quarter) == str):
            query_quarter = [quarter]


    query = env.session.query(FinanceAnalysis).filter(FinanceAnalysis.year.in_(query_year) , FinanceAnalysis.quarter.in_(query_quarter))
    result = pandas.read_sql(query.statement, env.session.bind)

    # EPS: = (Lợi nhuận sau thuế – Cổ tức cổ phiếu ưu đãi) / Tổng số cổ phiếu thường đang lưu hành)
    result["eps_basic"] = result["loi_nhuan_sau_thue"] / result["klcp_luu_hanh"]
    result["eps_basic"] = result["eps_basic"].astype("float").round(3)
    result["eps_basic"] = result["eps_basic"].fillna(0)

    # P/E = Giá thị trường / EPS (EPS: Lợi nhuận sau thuế của 1 cổ phiếu)
    result["pe"] = result["gia_thi_truong"] / result["eps_basic"]
    result["pe"] = result["pe"].astype("float").round(3)
    result["pe"] = result["pe"].fillna(0)
    result["pe"] = result["pe"].replace([np.inf, -np.inf], np.nan)

    # BVPS = {Tổng tài sản – Tài sản vô hình – Nợ } / Số lượng cổ phiếu phát hành
    result["book_value"] = (result["tong_tai_san"] - result["tong_no"]) / result["klcp_luu_hanh"]
    result["book_value"] = result["book_value"].astype("float").round(3)
    result["book_value"] = result["book_value"].fillna(0)

    # ROA = Lợi nhuận sau thuế (Earnings) / Tài sản (Assets) * 100%
    result["roa"] = result["loi_nhuan_sau_thue"] *100 / result["tong_tai_san"]
    result["roa"] = result["roa"].astype("float").round(3)
    result["roa"] = result["roa"].fillna(0)

    # ROE = Lợi nhuận sau thuế  / Vốn chủ sở hữu * 100%
    result["roe"] = result["loi_nhuan_sau_thue"] * 100 / result["von_chu_so_huu"]
    result["roe"] = result["roe"].astype("float").round(3)
    result["roe"] = result["roe"].fillna(0)

    # ROS = (Lợi nhuận sau thuế  / Doanh thu thuan) * 100%
    result["ros"] = result["loi_nhuan_sau_thue"] * 100 / result["doanh_thu_thuan"]
    result["ros"] = result["ros"].astype("float").round(3)
    result["ros"] = result["ros"].fillna(0)

    # GOS = [(doanh thu thuần – giá vốn hàng bán) / doanh thu thuần]× 100%
    result["gos"] = (result["doanh_thu_thuan"] - result["gia_von"]) * 100 / result["doanh_thu_thuan"]
    result["gos"] = result["gos"].astype("float").round(3)
    result["gos"] = result["gos"].fillna(0)

    # DAR (Hệ số nợ) = Tổng nợ/ Tổng tài sản
    result["dar"] = result["tong_no"] / result["tong_tai_san"]
    result["dar"] = result["dar"].astype("float").round(3)
    result["dar"] = result["dar"].fillna(0)

    result.to_sql('finance_analysis', env.engine, if_exists='replace')
    return True
