import pandas
import config.environment as env
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException


def get_data_from_ssi_board():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1920x800")

    browser = webdriver.Chrome(
        chrome_options=chrome_options,
        executable_path="tools/chromedriver"
    )

    url = env.default_url
    browser.get(url)

    sleep(10)

    ticket_ids = []
    ticket_ceil_price = []
    ticket_floor_price = []
    ticket_ref_price = []
    ticket_matched_price = []
    ticket_matched_volum = []
    ticket_price_change = []
    ticket_percent_change = []
    container = browser.find_element_by_id("table-table-scroll")
    all_trs = container.find_elements_by_css_selector("tr")
    for tr in all_trs:
        try:
            td_symbol = tr.find_element_by_css_selector("td.stockSymbol")
            ticket_ids.append(td_symbol.text)
            td_ceil = tr.find_element_by_css_selector("td.ceiling")
            ticket_ceil_price.append(td_ceil.text)
            td_floor = tr.find_element_by_css_selector("td.floor")
            ticket_floor_price.append(td_floor.text)
            td_ref = tr.find_element_by_css_selector("td.refPrice")
            ticket_ref_price.append(td_ref.text)
            ele_matched_price = tr.find_element_by_css_selector(".matchedPrice div")
            ticket_matched_price.append(ele_matched_price.text)
            ele_match_volum = tr.find_element_by_css_selector(".matchedVolume div")
            ticket_matched_volum.append(ele_match_volum.text)
            ele_price_change = tr.find_element_by_css_selector(".priceChange div")
            ticket_price_change.append(ele_price_change.text)
            ele_percent_change = tr.find_element_by_css_selector(".priceChangePercent div")
            ticket_percent_change.append(ele_percent_change.text)

        except NoSuchElementException:
            pass

    df = pandas.DataFrame(list(zip(
        ticket_ids,
        ticket_ceil_price,
        ticket_floor_price,
        ticket_ref_price,
        ticket_matched_price,
        ticket_matched_volum,
        ticket_price_change,
        ticket_percent_change
    )), columns=[
        "ticket_id", "ceil_price",
        "floor_price", "ref_price",
        "matched_price", "matched_volum",
        "price_changed", "percent_change"
    ])

    print(df)
    sleep(5)
    browser.close()