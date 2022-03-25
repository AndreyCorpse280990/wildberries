import csv
import bs4
import time
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys


def get_html(url):
    try:
        # to protect against detection
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")

        options.add_experimental_option("excludeSwitches",
                                        ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options,
                                  executable_path=r"C:\\Users\corps\\"
                                                  r"Desktop\Програмирование\\"
                                                  r"Learn Python\project\\"
                                                  r"wildberries\ChromeDriver\\"
                                                  r"chromedriver.exe")

        # client settings
        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win64",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        driver.get(url=url)
        time.sleep(2)
        html = driver.find_element_by_class_name('nav-element__logo')

        while True:
            html.send_keys(Keys.END)
            time.sleep(3)
            # searching for a block of elements and getting html
            product_card = driver.find_element_by_xpath(
                "//div[@id='catalog-content']")
            soup = bs4.BeautifulSoup(product_card.get_attribute('innerHTML'),
                                     'lxml')

            # getting the text of products and price and URL
            find_price = soup.select('.lower-price')
            lower_price = ([price.get_text().strip().replace("₽", '')
                            for price in find_price])
            
            find_name = soup.select('.goods-name')
            goods_name = ([name.get_text() for name in find_name])
            
            path_name = 'name.csv'
            with open(path_name, 'w', encoding='utf-8') as file_name:
                writer_name = csv.writer(file_name, delimiter=':')
                writer_name.writerows([goods_name])
                
            path_price = 'price.csv'
            with open(path_price, 'w', encoding='utf-8') as file_price:
                writer_price = csv.writer(file_price, delimiter=';')
                writer_price.writerows([lower_price])
            for n, p in zip(goods_name, lower_price):
                print(p)
            break
            
        return goods_name, lower_price

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    get_html(
        url='https://www.wildberries.ru/catalog/0/search.aspx?search=hdd+3.5')