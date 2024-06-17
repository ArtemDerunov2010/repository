import flask

shop_app  = flask.Blueprint(name = "shop_app", import_name = "app", template_folder = "shop_page/templates", static_folder = "static/shop_page")