import time
from selenium.webdriver.common.keys import Keys
from config import (
    get_web_driver_options,
    get_chrome_web_driver,
    set_ignore_certificate_error,
    set_browser_as_incognito,
    set_automation_as_head_less,
    BASE_URL,
    NAME,
    FILTERS)

#url = "https://www.wunderground.com/{history}/{monthly}/in/pune/VAPO/date/2020-6"

#wuSearch

class WUndergroundAPI:
    def __init__(self,searchTerm,baseURL,filter):
        self.baseURL=baseURL
        self.searchTerm=searchTerm
        options = get_web_driver_options()
        set_ignore_certificate_error(options)
        set_browser_as_incognito(options)
        self.driver=get_chrome_web_driver(options)
        self.set_filter = f"{filter['state']}/{filter['period']}/"
    
    def Run(self):
        print("Starting the script...")
        print(f"Looking for {self.searchTerm}")
        self.GetPage()
        time.sleep(6)
        self.driver.quit

    def GetPage(self):
        self.driver.get(self.baseURL)
        element = self.driver.find_element_by_id("wuSearch")
        element.send_keys(self.searchTerm)
        time.sleep(1)
        element.send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.get(f"{self.driver.current_url}")#.replace('weather',self.set_filter)}
        time.sleep(10)
        print("FIND THE LINK")
        try:
            self.driver.find_element_by_class_name('subnav subnav-left')
        except Exception as e:
            print (e)
            print("couldnt find link")

if __name__ == '__main__' :
    hi= WUndergroundAPI(NAME,BASE_URL,FILTERS)
    hi.Run()