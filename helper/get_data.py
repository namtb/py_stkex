import pandas
from datetime import datetime
import config.environment as env
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import re



# Get security data of year
def get_securiry_for_year_quarter():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920x800")
    chrome_options.add_argument("--headless")

    urls = env.finance_info_list_urls

    for ticket,link_address in urls.items():
        browser = webdriver.Chrome(
            chrome_options=chrome_options,
            executable_path="tools/chromedriver.exe"
        )
        browser.get(link_address)
        sleep(5)

        if (ticket in env.list_ticket_type_1 or ticket in env.list_ticket_type_2):
            list_element_ids_quarter = env.list_colums_information_type_1
            link_year = browser.find_element_by_xpath('//*[@id="idTabTaiChinhNam"]')
        if (ticket in env.list_ticket_type_2):
            list_element_ids_quarter = env.list_colums_information_type_2
            link_year = browser.find_element_by_xpath('//*[@id="idTabTaiChinhNam"]')
        if (ticket in env.list_ticket_type_3):
            list_element_ids_quarter = env.list_colums_information_type_3
            link_year = browser.find_element_by_css_selector("#litimetabs2 a")

        link_year.click()
        sleep(3)

        tr_header = browser.find_element_by_xpath('//*[@id="divHoSoCongTyAjax"]/table/tbody/tr[1]')
        if (ticket in env.list_ticket_type_1 or ticket in env.list_ticket_type_2):
            list_th = tr_header.find_elements_by_css_selector("th")
            div = browser.find_element_by_class_name("dltl-other")
            try:
                klcp_niem_yet = div.find_element_by_xpath('//*[@id="content"]/div/div[6]/div[1]/div[3]/ul/li[4]/div[2]')
                klcp_luu_hanh = div.find_element_by_xpath('//*[@id="content"]/div/div[6]/div[1]/div[3]/ul/li[5]/div[2]')
                von_hoa_tt = div.find_element_by_xpath('//*[@id="content"]/div/div[6]/div[1]/div[3]/ul/li[6]/div[2]')
            except NoSuchElementException:
                klcp_niem_yet = div.find_element_by_xpath('//*[@id="content"]/div/div[6]/div[5]/div/ul/li[2]/div[2]')
                klcp_luu_hanh = div.find_element_by_xpath('//*[@id="content"]/div/div[6]/div[5]/div/ul/li[3]/div[2]')
                von_hoa_tt = div.find_element_by_xpath('//*[@id="content"]/div/div[6]/div[5]/div/ul/li[4]/div[2]')
        if (ticket in env.list_ticket_type_3):
            list_th = tr_header.find_elements_by_class_name("tright")
            try:
                div = browser.find_element_by_class_name("tidown")
                klcp_niem_yet = div.find_element_by_xpath('//*[@id="contentV1"]/div[4]/div[2]/div[1]/div[2]/ul/li[7]/span[2]')
                klcp_luu_hanh = div.find_element_by_xpath('//*[@id="contentV1"]/div[4]/div[2]/div[1]/div[2]/ul/li[8]/span[2]')
                von_hoa_tt = div.find_element_by_xpath('//*[@id="contentV1"]/div[4]/div[2]/div[1]/div[2]/ul/li[9]/span[2]')
            except NoSuchElementException:
                div = browser.find_element_by_class_name("dltl-other")
                klcp_niem_yet = div.find_element_by_xpath('//*[@id="contentV1"]/div[4]/div[5]/div/ul/li[2]/div[2]')
                klcp_luu_hanh = div.find_element_by_xpath('//*[@id="contentV1"]/div[4]/div[5]/div/ul/li[3]/div[2]')
                von_hoa_tt = div.find_element_by_xpath('//*[@id="contentV1"]/div[4]/div[5]/div/ul/li[4]/div[2]')

        data = {
            "ticker_id": [],
            "year": [],
            "quarter": [],
            "klcp_niem_yiet": [],
            "klcp_luu_hanh": [],
            "von_hoa_thi_truong": [],
            "created_date": [],
            "last_updated": []
        }

        # current date and time
        now = datetime.now()

        for th in list_th:
            if (ticket in env.list_ticket_type_1 or ticket in env.list_ticket_type_2):
                th_attr = th.get_attribute("align")
                if (th_attr == "right"):
                    th_year = re.sub("\D","",th.text)
                    if (th_year != ""):
                        data["year"].append(th_year)
                        data["quarter"].append(0)
                        data["ticker_id"].append(ticket.upper())
                        data["klcp_niem_yiet"].append(klcp_niem_yet.text.replace(",",""))
                        data["klcp_luu_hanh"].append(klcp_luu_hanh.text.replace(",",""))
                        data["von_hoa_thi_truong"].append(von_hoa_tt.text.replace(",",""))
                        data["created_date"].append(now.strftime("%Y-%m-%d %H:%M:%S"))
                        data["last_updated"].append(now.strftime("%Y-%m-%d %H:%M:%S"))
            if (ticket in env.list_ticket_type_3):
                th_year = re.sub("\D", "", th.text)
                if (th_year != ""):
                    data["year"].append(th_year)
                    data["quarter"].append(0)
                    data["ticker_id"].append(ticket.upper())
                    data["klcp_niem_yiet"].append(klcp_niem_yet.text.replace(",",""))
                    data["klcp_luu_hanh"].append(klcp_luu_hanh.text.replace(",",""))
                    data["von_hoa_thi_truong"].append(von_hoa_tt.text.replace(",",""))
                    data["created_date"].append(now.strftime("%Y-%m-%d %H:%M:%S"))
                    data["last_updated"].append(now.strftime("%Y-%m-%d %H:%M:%S"))

        table = browser.find_element_by_css_selector("#divHoSoCongTyAjax table")
        for key,tr_id in list_element_ids_quarter.items():
            data.update({key: []})
            try:
                tr = table.find_element_by_id(tr_id)
            except NoSuchElementException:
                print("Can not find any year element.")
                for idx in range(0,4):
                    data[key].append("")
                continue

            tds = tr.find_elements_by_css_selector("td")
            for td in tds:
                td_style = td.get_attribute("style")
                if (td_style == "text-align: right;" and len(td.find_elements_by_tag_name("center")) == 0):
                    data[key].append(td.text.replace(",",""))

        # Handle quarter information
        if (ticket in env.list_ticket_type_1 or ticket in env.list_ticket_type_2):
            link_previous = browser.find_element_by_id("idTabTaiChinhQuy")
        if (ticket in env.list_ticket_type_3):
            link_previous = browser.find_element_by_css_selector("#litimetabs1 a")

        link_previous.click()
        sleep(3)

        tr_header = browser.find_element_by_xpath('//*[@id="divHoSoCongTyAjax"]/table/tbody/tr[1]')
        if (ticket in env.list_ticket_type_1 or ticket in env.list_ticket_type_2):
            tr_header = browser.find_element_by_xpath('//*[@id="divHoSoCongTyAjax"]/table/tbody/tr[1]')
            list_th_quarter = tr_header.find_elements_by_css_selector("th")
        if (ticket in env.list_ticket_type_3):
            list_th_quarter = tr_header.find_elements_by_class_name("tright")

        for th in list_th_quarter:
            if (ticket in env.list_ticket_type_1 or ticket in env.list_ticket_type_2):
                th_attr = th.get_attribute("align")
                if (th_attr == "right"):
                    th_year = re.sub("\D", "", th.text)
                    if (th_year != ""):
                        quarter_text = th_year[0]
                        data["year"].append(th_year[1:5])
                        data["quarter"].append(quarter_text)
                        data["ticker_id"].append(ticket.upper())
                        data["klcp_niem_yiet"].append(klcp_niem_yet.text.replace(",",""))
                        data["klcp_luu_hanh"].append(klcp_luu_hanh.text.replace(",",""))
                        data["von_hoa_thi_truong"].append(von_hoa_tt.text.replace(",",""))
                        data["created_date"].append(now.strftime("%Y-%m-%d %H:%M:%S"))
                        data["last_updated"].append(now.strftime("%Y-%m-%d %H:%M:%S"))
            if (ticket in env.list_ticket_type_3):
                th_year = re.sub("\D","",th.text)
                if (th_year != ""):
                    quarter_text = th_year[0]
                    data["year"].append(th_year[1:5])
                    data["quarter"].append(quarter_text)
                    data["ticker_id"].append(ticket.upper())
                    data["klcp_niem_yiet"].append(klcp_niem_yet.text.replace(",",""))
                    data["klcp_luu_hanh"].append(klcp_luu_hanh.text.replace(",",""))
                    data["von_hoa_thi_truong"].append(von_hoa_tt.text.replace(",",""))
                    data["created_date"].append(now.strftime("%Y-%m-%d %H:%M:%S"))
                    data["last_updated"].append(now.strftime("%Y-%m-%d %H:%M:%S"))

        table_quarter = browser.find_element_by_css_selector("#divHoSoCongTyAjax table")
        for key,tr_id in list_element_ids_quarter.items():
            try:
                tr = table_quarter.find_element_by_id(tr_id)
            except NoSuchElementException:
                print("Can not find any quarter element")
                for indx in range(0,4):
                    data[key].append("")
                continue

            tds = tr.find_elements_by_css_selector("td")
            for td in tds:
                td_style = td.get_attribute("style")
                if (td_style == "text-align: right;" and len(td.find_elements_by_tag_name("center")) == 0):
                    data[key].append(td.text.replace(",",""))

        # print(data)
        df = pandas.DataFrame(data)
        df.to_csv('data/fin_info/'+ticket+'_finance_information.csv', index=False)
        print(ticket +"_finance_information.csv: Finished.")
        sleep(1)
        browser.close()