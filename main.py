import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from config import (
    get_web_driver_options,
    get_chrome_web_driver,
    set_ignore_certificate_error,
    set_browser_as_incognito,
    set_automation_as_head_less,
    BASE_URL,
    NAME,
    FILTERS)
from bs4 import BeautifulSoup as BS
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
        self.set_filter = f"date/{filter['date']}"
        #self.set_filter = f"{filter['state']}/{filter['period']}/"
    
    def Run(self):
        print("Starting the script...")
        print(f"Looking for {self.searchTerm}")
        PageSource=self.GetPageData()
        self.ScarpData(PageSource)
        

    def GetPageData(self):
        self.driver.get(self.baseURL)
        time.sleep(1)
        self.driver.get(f"{self.driver.current_url}/{self.set_filter}")
        time.sleep(2)
        PageSource=self.driver.page_source
        self.driver.quit()
        return PageSource
            
    def ScarpData(self, page_source):
        soup = BS(page_source, "html.parser")
        container = soup.find('lib-city-history-observation')
        check = container.find('tbody')

        data = []

        for c in check.find_all('tr', class_='ng-star-inserted'):
            for i in c.find_all('td', class_='ng-star-inserted'):
                trial = i.text
                trial = trial.strip('  ')
                data.append(trial)
        print(data)

    # def GetPage(self):
    #     self.driver.get(self.baseURL)
    #     element = self.driver.find_element_by_id("wuSearch")
    #     element.send_keys(self.searchTerm)
    #     time.sleep(2)
    #     element.send_keys(Keys.ENTER)
    #     time.sleep(1)
    #     self.driver.get(f"{self.driver.current_url}")#.replace('weather',self.set_filter)}
    #     time.sleep(10)
    #     print("FIND THE LINK")
    #     ResultList=self.driver.find_elements_by_class_name('region-content-top')
    #     try:
    #         result =ResultList[0].find_element_by_xpath(
    #             "//div[2]/lib-subnav/div/div[3]/ul/li[5]/a"
    #         )
    #     except Exception as e:
    #         print(e)
    #         print("couldnt find")

if __name__ == '__main__' :
    hi= WUndergroundAPI(NAME,BASE_URL,FILTERS)
    hi.Run()