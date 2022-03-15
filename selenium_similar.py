import csv
import bs4
import requests
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from operator import methodcaller

def get_html(url):
    s=Service(
        'C:\\Users\\corps\\Desktop\\Програмирование\\Learn Python\\project\\wildberries\\chromedriver\\chromedriver.exe'
        )
    
    
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    
    

    try:
        driver.get(url=url)
        time.sleep(3)
        html = driver.find_element_by_class_name('pagination-next')

        while True:
            html.send_keys(Keys.END)
            time.sleep(3)
            product_card = driver.find_element_by_xpath("//div[@id='catalog-content']")
            soup = bs4.BeautifulSoup(product_card.get_attribute('innerHTML'), 'lxml')
            find_price = soup.find_all('span', {'class': 'lower-price'})
            lower_price = ([price.get_text() for price in find_price])
            
            find_name = soup.find_all('span', {'class': 'goods-name'})
            goods_name = ([name.get_text() for name in find_name])
            
            
            print(lower_price)
            print(goods_name)
            #with open('test.txt', 'w', encoding="utf-8") as file:
                #file.write(" ".join(lower_price))
             #   file.write(goods_name.split(','))#непонятно как разделить кроме как циклом for
             #   file.write(map(goods_name.split(',')))
            break
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def main():
    get_html(url='https://www.wildberries.ru/catalog/0/search.aspx?search=hdd+3.5')

if __name__ == '__main__':
    main()