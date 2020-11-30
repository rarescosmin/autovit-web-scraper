import requests
from bs4 import BeautifulSoup

AUTOVIT_BASE_URL = "https://www.autovit.ro/autoturisme/"

response = requests.get(AUTOVIT_BASE_URL)

if response.status_code == 200:
    html = response.text
    #print(html)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

