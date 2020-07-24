from bs4 import BeautifulSoup
import requests
url = "https://www.wunderground.com/history/monthly/in/pune/VAPO/date/2020-6"
# loading monthly data of pune of JUNE
page = requests.get(url)
soup = BeautifulSoup(page.content,'lxml')
for i in range(5):
    body = soup.find('table') # there are multiple tables of the same class
    print(""" 
    -------START------


    -------Prints one table----
    """)
    print(body.prettify()) # printing all the Tables
    print(""" 

    --------END-------
    
    """)