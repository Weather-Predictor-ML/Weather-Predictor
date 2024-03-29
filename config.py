from selenium import webdriver

NAME="Pune"
FILTERS={
    "state": "history",
    "period": "monthly",
    "date" : "2020-7"
}
BASE_URL = "https://www.wunderground.com/history/monthly/in/pune/VAPO"#"https://www.wunderground.com/"


def get_chrome_web_driver(options):
    return webdriver.Chrome("chromedriver", chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')


def set_automation_as_head_less(options):
    options.add_argument('--headless')