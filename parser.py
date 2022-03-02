import requests
from bs4 import BeautifulSoup

url = 'https://www.wildberries.ru/catalog/19257508/detail.aspx?targetUrl=XS'

def description(url):
    try:
        responce = requests.get(url)
        print(responce.status_code)
    except(requests.RecursionError, ConnectionResetError, requests.RequestException):
            print('Ошибка сети')
            return False
    soup = BeautifulSoup(responce.text, 'lxml')
    parameters = soup.find_all('body', class_='ru')
    for i in parameters:
        param = {}
        param = i.find('script').text
        print(param)
        
        
if __name__=="__main__":
    description('https://www.wildberries.ru/catalog/19257508/detail.aspx?targetUrl=XS')
