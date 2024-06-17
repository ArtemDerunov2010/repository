from project.settings import data_base

class Product(data_base.Model):
    id = data_base.Column(data_base.Integer, primary_key = True)
    name = data_base.Column(data_base.String(50), nullable = False)
    image_name = data_base.Column(data_base.String(100), nullable = False)