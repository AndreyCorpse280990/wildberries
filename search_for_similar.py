import bs4
import requests
import json
import logging
import html5lib

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('wb')

class Client:
    
    def __init__(self):
      self.session = requests.Session()
      self.session.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.31',
        'Assept-Language': 'ru',     
      }
    def load_page(self):
        url = 'https://www.wildberries.ru/catalog/zhenshchinam/odezhda/verhnyaya-odezhda'
        result = self.session.get(url=url)
        result.raise_for_status()
        return result.text
    
    def parge_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        product_card = soup.select('div.product-card.j-card-item')
        for block in product_card:
            self.parse_block(block=block)
            
    def parse_block(self, block):
        logger.info(block)
        logger.info('=' * 100)
        
    def run(self):
        text = self.load_page()
        self.parge_page(text=text)
        
if __name__=="__main__":
    parser = Client()
    parser.run()
# def main():
#     r = requests.get("https://www.wildberries.ru/catalog/0/search.aspx?search=iphone")
#     soup = BeautifulSoup(r.content,'html5lib')
#     lol = soup.find_all('div',class_='goods-name')
#     print(lol)


