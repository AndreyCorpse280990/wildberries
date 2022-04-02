import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')

# for selenium_similar
PATH_PRICE = "C:\\Users\\corps\\Desktop\\Програмирование\\Learn Python\\project\\wildberries\\price.csv"
PATH_NAME = "C:\\Users\\corps\\Desktop\\Програмирование\\Learn Python\\project\\wildberries\\name.csv"
PATH_URL = "C:\\Users\\corps\\Desktop\\Програмирование\\Learn Python\project\\wildberries\\Url.csv"
ENCODING_SELENIUM = "utf-8"

DRIVER_PATH = "C:\\Users\\corps\\Desktop\\Програмирование\\Learn Python\\project\\wildberries\\ChromeDriver\\chromedriver.exe"
URL_SELENIUM = "https://www.wildberries.ru/catalog/0/search.aspx?search=hdd+3.5"

# for basedata
CREATE_ENGINE = "postgres://idrvtwxh:iRvZ1OzRdTkZ1tI5hE7jhQy1IEs8bhVm@hattie.db.elephantsql.com/idrvtwxh"