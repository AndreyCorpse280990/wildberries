from flask import render_template, Blueprint
from webapp.parsing.models import Item, ItemPrice

blueprint = Blueprint('parsing', __name__)


@blueprint.route("/")
def index():
    title = 'Wildberries parser'
    return render_template('news/index.html', page_title=title)