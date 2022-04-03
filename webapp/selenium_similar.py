import csv
import bs4
import time
from webapp import config
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
                                  executable_path=config.DRIVER_PATH)

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

            # formatting spaces and the '₽' sign
            lower_price = ([str(''.join(price.get_text().replace('₽', '')
                                        .split())) for price in find_price])
            # transformation in int
            lower_price = list(map(int, lower_price))

            find_name = soup.select('.goods-name')
            goods_name = ([name.get_text() for name in find_name])

            # getting URL
            product_divs = soup.select('.product-card__wrapper')
            product_url = []
            for div in product_divs:
                prod_url = ([div.find('a')['href']])
                product_url += prod_url

            # saving csv
            path_name = config.PATH_NAME
            with open(path_name, 'w', encoding=config.ENCODING_SELENIUM)\
                    as file_name:
                writer_name = csv.writer(file_name, delimiter=':')
                writer_name.writerows([goods_name])

            path_price = config.PATH_PRICE
            with open(path_price, 'w', encoding=config.ENCODING_SELENIUM)\
                    as file_price:
                writer_price = csv.writer(file_price, delimiter=':')
                writer_price.writerows([lower_price])

            path_url = config.PATH_URL
            with open(path_url, 'w', encoding=config.ENCODING_SELENIUM)\
                    as file_url:
                writer_url = csv.writer(file_url, delimiter=':')
                writer_url.writerows([product_url])

            break

        return goods_name, lower_price, product_url

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    get_html(url=config.URL_SELENIUM)