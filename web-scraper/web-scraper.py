import requests
from bs4 import BeautifulSoup
import csv


AUTOVIT_URL = "https://www.autovit.ro/autoturisme/?search%5Border%5D=created_at%3Adesc&page={}"


# parses car model for BMWs
# if BMW has 'Seria' in model, then it returns Seria + nr
def parseCarModel(carModel):
    if 'BMW' in str(carModel[0]) and ('seria' in str(carModel[1]) or 'Seria' in str(carModel[1])):
        return carModel[1] + ' ' + carModel[2]
    return carModel[1]

def checkIfCarItemIsNull(carItem):
    if (carItem == None):
        return ''
    return carItem

def writeCarsToCSV(carDivContent, shouldWriteCSVheader):
     with open('cars.csv', 'a', newline='') as csvfile:
        fieldnames = ['make', 'model', 'year', 'mileage', 'fuelType', 'engineCapacity', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if shouldWriteCSVheader == 1:
            writer.writeheader()

        for item in carDivContent:
            try: 
                if 'article' in str(item):
                    car = {
                        'make': checkIfCarItemIsNull(item.contents[3].contents[1].contents[1].text.strip().split()[0]),
                        'model': checkIfCarItemIsNull(parseCarModel(item.contents[3].contents[1].contents[1].text.strip().split())),
                        'year': checkIfCarItemIsNull(item.contents[3].contents[3].contents[1].text.strip()),
                        'mileage': checkIfCarItemIsNull(item.contents[3].contents[3].contents[3].text.strip()),
                        'fuelType': checkIfCarItemIsNull(item.contents[3].contents[3].contents[5].text.strip()),
                        'engineCapacity': checkIfCarItemIsNull(item.contents[3].contents[3].contents[7].text.strip()),
                        'price': checkIfCarItemIsNull(item.contents[3].contents[5].text.replace('\n', '').split('EUR')[0].strip())
                    }
                    writer.writerow(car)
            except Exception:
                print('not inserted')

if __name__ == '__main__':

    for i in range(1, 500):
        response = requests.get(AUTOVIT_URL.format(i))
        
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            carDivList = soup.select("div.offers.list")
            carDivContent = carDivList[0].contents
            writeCarsToCSV(carDivContent, i)
        
        print('scraping.......')
    
    print('FINISHED!')
    


