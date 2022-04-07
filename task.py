
from RPA.Browser.Selenium import Selenium
from RPA.HTTP import HTTP
import pandas as pd


browser = Selenium(auto_close=False)
r = HTTP()


def login():
    browser.open_chrome_browser(url="https://botsdna.com/notaries/")
    
from time import sleep

def get_details(notary, area,dist):
    browser.input_text(locator="//*[@id='notary']", text=notary, clear=True)
    browser.input_text(locator="//*[@id='area']", text=area, clear=True)
    browser.click_element(locator='//*[@id="DIST"]')
    sleep(5)
    # browser.click_element(locator=f'//*[@id="DIST"]/option[{dist}]')
    # browser.click_element(locator=f'//option[text()="${dist}"]')
    # browser.click_element(locator='//*[@id="DIST"]/option[5]')
    browser.click_element(locator='//*[contains(text(),"KRISHNA")]').select_option('KRISHNA')

    # browser.wait_until_element_is_visible(locator=f'//*[@id="DIST"]/option[{dist}]')
    # browser.click_element(locator=f'//*[@id="DIST"]/option[{dist}]')
    # browser.select_from_list_by_value(locator='//*[@id="DIST"]',values=str(dist))
    # browser.select_from_list_by_label(locator='//*[@id="DIST"]',labels=str(dist))
    # browser.press_keys(locator='//*[@id="DIST"]', keys=dist)
    browser.click_button(locator='//input[@type="button"]')
    browser.wait_until_element_is_visible(locator="//*[@id='TransNo']")
    t_no = browser.get_text(locator='//*[@id="TransNo"]')
    return t_no
    
def to_main_page():
    browser.go_back()   

def download_data():
    r.download(url="https://botsdna.com/notaries/AP-ADVOCATES.xlsx", target_file="data/")

def enter_data():
    df = pd.read_excel('data/AP-ADVOCATES.xlsx')
    dist = []
    for x in df['SL.NO.']:
        if "DIST" in str(x):
            dist.append(x)
        elif "GOVT" in str(x):
                dist.append(x)
        else:
            try:
                x = dist[-1]
                dist.append(x)
            except:
                pass
    df['Districts'] = pd.DataFrame(dist)
    df = df.drop('Transaction Number', axis=1)
    df = df.dropna(axis=0)
    return print(df.head())

def main():
    download_data()
    login()
    get_details('GURUBELLI KRISHNA RAO','Tekkali, Srikakulam Dist.','5')
    # to_main_page()
    enter_data()


if __name__ == "__main__":
    main()
