from pydoc import text
import requests
import logging
from bs4 import BeautifulSoup

logging.basicConfig(filename="parser.log", level=logging.INFO)

url = 'https://www.wildberries.ru/catalog/19257508/detail.aspx?targetUrl=XS'

def description(url):
    try:
        responce = requests.get(url)
        return responce.text
    except(requests.RecursionError, ConnectionResetError, requests.RequestException):
            print('Ошибка сети')
            return False
    
def get_information(html):
    soup = BeautifulSoup(html, 'lxml')
    info = soup.find('div', {'id': 'app'}).find(id)
    app = info.find('meta', {'itemprop': 'name'}) # тут незаконченный вопрос с name
    print(app)
    
    
def main(url):
    html = description(url)
    get_information(html)
        
if __name__=="__main__":
    main(url)
