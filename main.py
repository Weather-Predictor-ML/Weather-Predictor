import time
#from selenium.webdriver.common.keys import Keys
import pandas as pd
from functools import reduce
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


class DataHandler:
    """It takes Raw data (list) produced by the API and process it to create dataset for one month"""
    def __init__(self, Data,filter):
        print("Processing the data....")
        self.rawData = Data
        self.filter=filter
        Dataframe=self.ProcessData(self.rawData)
        self.MakeCSV(Dataframe)

    def MakeCSV(self,DF):
        """Convert A DataFrame to a CSV file"""
        self.df=DF
        self.df.to_csv('data.csv',index=None)
        print(f"Created File for {self.filter['date']}")

    def ProcessData(self, data):
        """Process the RawData produced by the API and greats a DataFrame"""
        self.data= data
        list_of_df=[]
        print("Processing the data....")
        if round(len(self.data) / 17 - 1) == 31:
            Temperature = pd.DataFrame([self.data[32:128][x:x + 3] for x in range(0, len(self.data[32:128]), 3)][1:],
                                       columns=['Temp_max', 'Temp_avg', 'Temp_min'])
            Dew_Point = pd.DataFrame([self.data[128:224][x:x + 3] for x in range(0, len(self.data[128:224]), 3)][1:],
                                     columns=['Dew_max', 'Dew_avg', 'Dew_min'])
            Humidity = pd.DataFrame([self.data[224:320][x:x + 3] for x in range(0, len(self.data[224:320]), 3)][1:],
                                    columns=['Hum_max', 'Hum_avg', 'Hum_min'])
            Wind = pd.DataFrame([self.data[320:416][x:x + 3] for x in range(0, len(self.data[320:416]), 3)][1:],
                                columns=['Wind_max', 'Wind_avg', 'Wind_min'])
            Pressure = pd.DataFrame([self.data[416:512][x:x + 3] for x in range(0, len(self.data[416:512]), 3)][1:],
                                    columns=['Pres_max', 'Pres_avg', 'Pres_min'])
            Date = pd.DataFrame(self.data[:32][1:], columns=self.data[:1])
            Precipitation = pd.DataFrame(self.data[512:][1:], columns=['Precipitation'])
            print(f"{self.filter['date']} finished")
        elif round(len(self.data) / 17 - 1) == 28:
            Temperature = pd.DataFrame([self.data[29:116][x:x + 3] for x in range(0, len(self.data[29:116]), 3)][1:],
                                       columns=['Temp_max', 'Temp_avg', 'Temp_min'])
            Dew_Point = pd.DataFrame([self.data[116:203][x:x + 3] for x in range(0, len(self.data[116:203]), 3)][1:],
                                     columns=['Dew_max', 'Dew_avg', 'Dew_min'])
            Humidity = pd.DataFrame([self.data[203:290][x:x + 3] for x in range(0, len(self.data[203:290]), 3)][1:],
                                    columns=['Hum_max', 'Hum_avg', 'Hum_min'])
            Wind = pd.DataFrame([self.data[290:377][x:x + 3] for x in range(0, len(self.data[290:377]), 3)][1:],
                                columns=['Wind_max', 'Wind_avg', 'Wind_min'])
            Pressure = pd.DataFrame([self.data[377:464][x:x + 3] for x in range(0, len(self.data[377:463]), 3)][1:],
                                    columns=['Pres_max', 'Pres_avg', 'Pres_min'])
            Date = pd.DataFrame(self.data[:29][1:], columns=self.data[:1])
            Precipitation = pd.DataFrame(self.data[464:][1:], columns=['Precipitation'])
            print(f"{self.filter['date']} finished")
        elif round(len(self.data) / 17 - 1) == 29:
            Temperature = pd.DataFrame([self.data[30:120][x:x + 3] for x in range(0, len(self.data[30:120]), 3)][1:],
                                       columns=['Temp_max', 'Temp_avg', 'Temp_min'])
            Dew_Point = pd.DataFrame([self.data[120:210][x:x + 3] for x in range(0, len(self.data[120:210]), 3)][1:],
                                     columns=['Dew_max', 'Dew_avg', 'Dew_min'])
            Humidity = pd.DataFrame([self.data[210:300][x:x + 3] for x in range(0, len(self.data[210:300]), 3)][1:],
                                    columns=['Hum_max', 'Hum_avg', 'Hum_min'])
            Wind = pd.DataFrame([self.data[300:390][x:x + 3] for x in range(0, len(self.data[300:390]), 3)][1:],
                                columns=['Wind_max', 'Wind_avg', 'Wind_min'])
            Pressure = pd.DataFrame([self.data[390:480][x:x + 3] for x in range(0, len(self.data[390:480]), 3)][1:],
                                    columns=['Pres_max', 'Pres_avg', 'Pres_min'])
            Date = pd.DataFrame(self.data[:30][1:], columns=self.data[:1])
            Precipitation = pd.DataFrame(self.data[480:][1:], columns=['Precipitation'])
            print(f"{self.filter['date']} finished")
        elif round(len(self.data) / 17 - 1) == 30:
            Temperature = pd.DataFrame([self.data[31:124][x:x + 3] for x in range(0, len(self.data[31:124]), 3)][1:],
                                       columns=['Temp_max', 'Temp_avg', 'Temp_min'])
            Dew_Point = pd.DataFrame([self.data[124:217][x:x + 3] for x in range(0, len(self.data[124:217]), 3)][1:],
                                     columns=['Dew_max', 'Dew_avg', 'Dew_min'])
            Humidity = pd.DataFrame([self.data[217:310][x:x + 3] for x in range(0, len(self.data[217:310]), 3)][1:],
                                    columns=['Hum_max', 'Hum_avg', 'Hum_min'])
            Wind = pd.DataFrame([self.data[310:403][x:x + 3] for x in range(0, len(self.data[310:403]), 3)][1:],
                                columns=['Wind_max', 'Wind_avg', 'Wind_min'])
            Pressure = pd.DataFrame([self.data[403:496][x:x + 3] for x in range(0, len(self.data[403:496]), 3)][1:],
                                    columns=['Pres_max', 'Pres_avg', 'Pres_min'])
            Date = pd.DataFrame(self.data[:31][1:], columns=self.data[:1])
            Precipitation = pd.DataFrame(self.data[496:][1:], columns=['Precipitation'])
            print(f"{self.filter['date']} finished")
        else:
            print('Data not in normal length')

        dfs = [Date, Temperature, Dew_Point, Humidity, Wind, Pressure, Precipitation]

        df_final = reduce(lambda left, right: pd.merge(left, right, left_index=True, right_index=True), dfs)

        df_final['Date'] = self.filter['date']+ "-" + df_final.iloc[:, :1].astype(str)
        print(f"Data processed for {self.filter['date']}")
        return df_final
        #list_of_df.append(df_final)
       # print (list_of_df)

class WUndergroundAPI:
    """This Api will create a VM on the page it acess and Then scrap the data of the page and then 
    A raw set of the data  of the Dailt Observation is produced and returned """
    def __init__(self,searchTerm,baseURL,filter):
        self.baseURL=baseURL
        self.searchTerm=searchTerm
        self.filter=filter
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
        Data=self.ScrapeData(PageSource)
        return Data

    def GetPageData(self):
        """Creates the VM to open the page and returns the page Source"""
        self.driver.get(self.baseURL)
        time.sleep(1)
        self.driver.get(f"{self.driver.current_url}/{self.set_filter}")
        time.sleep(10)
        PageSource=self.driver.page_source
        self.driver.quit()
        print(f"Got the page Data for {self.filter['date']}....")
        return PageSource
            
    def ScrapeData(self, page_source):
        """The page source is a scraped to returns the data of the Table"""
        print("Scraping the Data....")
        soup = BS(page_source, "html.parser")
        container = soup.find('lib-city-history-observation')
        check = container.find('tbody')

        data = []

        for c in check.find_all('tr', class_='ng-star-inserted'):
            for i in c.find_all('td', class_='ng-star-inserted'):
                trial = i.text
                trial = trial.strip('  ')
                data.append(trial)
        return data

    
    # def GetPage(self):
    #     """Opens the BaseURl and navigated to the page needed to scrape data from"""
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
    API= WUndergroundAPI(NAME,BASE_URL,FILTERS)
    data=API.Run()
    hi=DataHandler(data,FILTERS)