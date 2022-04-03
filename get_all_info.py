from webapp import create_app
# from webapp.selenium_similar import get_html
from webapp import config
from webapp.import_database import save_to_base

app = create_app()
with app.app_context():
    save_to_base(config.URL_SELENIUM)
    