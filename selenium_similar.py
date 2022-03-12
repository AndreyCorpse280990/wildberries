import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_html(url):
    s=Service(
        'C:\\Users\\corps\\Desktop\\Програмирование\\Learn Python\\project\\wildberries\\chromedriver\\chromedriver.exe'
        )
    
    
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    
    

    try:
        driver.get(url=url)
        time.sleep(5)
        
        while True:
            product_card = driver.find_element_by_xpath("//div[@id='catalog-content']")
            with open('test.html', 'w') as file:
                file.write(str(product_card))
                
            print(product_card.text)
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