import requests
from bs4 import BeautifulSoup

AUTOVIT_BASE_URL = "https://www.autovit.ro/autoturisme/"

response = requests.get(AUTOVIT_BASE_URL)

articles = []

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    carDivList = soup.select("div.offers.list")
    carDivContent = carDivList[0].contents
    for item in carDivContent:
        if item != '\n':
            articles.append(item)
    

    
    


