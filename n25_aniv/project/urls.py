from .settings import project
import home_page
import shop_page

home_page.home_app.add_url_rule(
    rule = "/",
    view_func = home_page.show_page
)

shop_page.shop_app.add_url_rule(
    rule = "/shop",
    view_func = shop_page.show_page
)

project.register_blueprint(blueprint = home_page.home_app)
project.register_blueprint(blueprint = shop_page.shop_app)