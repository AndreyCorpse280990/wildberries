from flask import render_template, current_app, Blueprint

blueprint = Blueprint('parsing', __name__)


@blueprint.route("/")
def index():
    title = 'Wildberries parser'
    return render_template('news/index.html', page_title=title)