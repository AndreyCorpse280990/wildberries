import requests
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

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
            #js = json.loads(product_card)
            #print(js)
            product_text = product_card.text

            with open('test.html', 'w', encoding="utf-8") as file:
                file.write(product_text)
            
            print(product_text)
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