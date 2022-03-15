from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def html(url):
    s=Service('C:\\Users\\corps\\Desktop\\Програмирование\\Learn Python\\project\\wildberries\\chromedriver\\chromedriver.exe')
    url = "https://www.wildberries.ru/catalog/0/search.aspx?search=hdd+3.5"
    driver = webdriver.Chrome(service=s)
    driver.get(url=url)
    time.sleep(5)
    #html = driver.page_source
    #soup = BeautifulSoup(html, 'lxml')
    #a = soup.find('section', 'wrapper')
    while True:
        product_card = driver.find_element_by_xpath("//div[@id='catalog-content']")
        with open('test.html', 'w') as file:
                file.write(str(product_card))
        
        print(product_card.text)
        break


def main():
    html(url='https://www.wildberries.ru/catalog/0/search.aspx?search=hdd+3.5')

if __name__ == '__main__':
    main()