from bs4 import BeautifulSoup
import requests
url = "https://www.wunderground.com/history/monthly/in/pune/VAPO"

page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
for i in range(5):
    body = soup.find(class_="columns small-12")
    print(""" 

    -----------------------

    """)
    print(body)
    print(""" 

    -----------------------
    
    """)