import flask
import os
from .model import Product

def show_page():
    if flask.request.method == "POST":
        product = Product(name = f"{flask.request.form['name']}", image_name = f"{flask.request.form['name']}.png")
        image = flask.request.files["image"] 
        image.save(os.path.abspath(__file__ + f"/../../static/home_page/image/{flask.request.form['name']}.png"))
    return flask.render_template(template_name_or_list = "home.html")