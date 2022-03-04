import requests
import json
from bs4 import BeautifulSoup


url = 'https://www.wildberries.ru/catalog/19257508/detail.aspx?targetUrl=XS'

def seach_similar(url):
    try:
        responce = requests.get(url)
        print(responce.status_code)
    except(requests.RecursionError, ConnectionResetError, requests.RequestException):
            print('Ошибка сети')
            return False
    soup = BeautifulSoup(responce.text, 'lxml')
    similar = soup.find_all('a', class_='mix-block__find-similar j-wba-card-item')
    print(similar)
    a = json.loads(similar)
    
    
if __name__=="__main__":
    seach_similar('https://www.wildberries.ru/catalog/19257508/detail.aspx?targetUrl=XS')
