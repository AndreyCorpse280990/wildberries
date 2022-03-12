import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
def get_html(url):
    s=Service(
        'C:\\Users\\corps\\Desktop\\Програмирование\\Learn Python\\project\\wildberries\\chromedriver\\chromedriver.exe'
        )
    
    
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    
    

    try:
        driver.get(url=url)
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, 555)")
        while True:
            end_page = driver.find_element_by_class_name("i-pager")
            
            if driver.find_element_by_class_name("pagination__wrapper"):
                with open('test.html', 'w') as file:
                    file.write(driver.page_source)
                    break
            else:
                action = ActionChains(driver)
                action.move_to_element(end_page).perform()
                time.sleep(5)
            
        
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def main():
    get_html(url='https://www.wildberries.ru/catalog/0/search.aspx?search=hdd+3.5')

if __name__ == '__main__':
    main()