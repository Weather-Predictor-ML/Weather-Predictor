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
        self.set_filter = f"/{filter['state']}/{filter['period']}/"
    
    def Run(self):
        print("STarting the script...")


if __name__ == '__main__' :
    WUndergroundAPI(N)