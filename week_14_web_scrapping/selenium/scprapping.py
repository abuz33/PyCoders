from selenium import webdriver

browser = webdriver.Chrome(
    executable_path='week_14_web_scrapping\selenium\chromedriver.exe')


# bol page linki
browser.get("https://www.bol.com/nl/l/vrieskisten/N/31631/?page=1")
