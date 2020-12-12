import requests
from bs4 import BeautifulSoup

AUTOVIT_BASE_URL = "https://www.autovit.ro/autoturisme/"

def getCarArticles(carDivContent):
    carArticles = []
    for item in carDivContent:
        if 'article' in str(item):
            carArticles.append(item)
    return carArticles

if __name__ == '__main__':

    response = requests.get(AUTOVIT_BASE_URL)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        carDivList = soup.select("div.offers.list")
        carDivContent = carDivList[0].contents
        carArticles = getCarArticles(carDivContent)
        print ('stop')
    


