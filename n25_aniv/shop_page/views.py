import flask
from home_page.model import Product

def show_page():
    return flask.render_template(template_name_or_list="shop.html", products = Product.query.all)