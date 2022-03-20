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
                                  executable_path=r"chromedriver\\chromedriver.exe")

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
        time.sleep(11)
        html = driver.find_element_by_class_name('nav-element__logo')



        while True:
            html.send_keys(Keys.PAGE_DOWN) * 5
            time.sleep(3)
            # searching for a block of elements and getting html
            product_card = driver.find_element_by_xpath(
                "//div[@id='catalog-content']")
            soup = bs4.BeautifulSoup(product_card.get_attribute('innerHTML'),
                                     'lxml')

            # getting the text of products and prices
            find_price = soup.find_all('span', {'class': 'lower-price'})
            lower_price = ([price.get_text().strip() for price in find_price])
            find_name = soup.find_all('span', {'class': 'goods-name'})
            goods_name = ([name.get_text() for name in find_name])
            
            #for n, p in zip(goods_name, lower_price):
                #print(n)
                #print(p)
                
            path_name = 'C:\\Users\\corps\\Desktop\\Програмирование\\Learn Python\\project\\wildberries\\name.csv'
            with open(path_name, 'w', encoding='utf-8') as file_name:
                writer_name = csv.writer(file_name, delimiter=':')
                writer_name.writerows([goods_name])

            path_price = 'C:\\Users\\corps\\Desktop\\Програмирование\\' \
                         'Learn Python\\project\\wildberries\\price.csv'
            with open(path_price, 'w', encoding='utf-8') as file_price:
                writer_price = csv.writer(file_price, delimiter=';')
                writer_price.writerows([lower_price])
            
            print(soup.text)
            
            break
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_html(
        url='https://www.wildberries.ru/catalog/0/search.aspx?search=hdd+3.5')


if __name__ == '__main__':
    main()
