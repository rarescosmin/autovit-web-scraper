import requests
from bs4 import BeautifulSoup

AUTOVIT_BASE_URL = "https://www.autovit.ro/autoturisme/"

def getCars(carDivContent):
    cars = []
    for item in carDivContent:
        if 'article' in str(item):
            car = {
                'make': item.contents[3].contents[1].contents[1].text.strip().split()[0],
                'model': item.contents[3].contents[1].contents[1].text.strip().split()[1]
            }
            cars.append(car)
    return cars
    

if __name__ == '__main__':

    response = requests.get(AUTOVIT_BASE_URL)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        carDivList = soup.select("div.offers.list")
        carDivContent = carDivList[0].contents
        cars = getCars(carDivContent)
        print ('stop')
    


