# file name: shoppingmall_info.py
# pwd: /shoppingMall_zioyou/start_shoppingmall/models/shoppingmall_info.py

from start_shoppingmall import db

class Accounts(db.Model):
    __tablename__ = 'accounts'
    user_id = db.Column(db.Integer, unique=True)
    user_email = db.Column(db.String(50), unique=True, primary_key=True)
    user_name = db.Column(db.String(50))
    user_password = db.Column(db.String(100))


    def __init__(self, user_email, user_name, user_password):
        self.user_email = user_email
        self.user_name = user_name
        self.user_password = user_password


class Product(db.Model):
    __tablename__ = 'product'
    product_id = db.Column(db.Integer, unique=True, primary_key=True)
    product_name = db.Column(db.CHAR(50))
    product_price = db.Column(db.FLOAT)

    def __init__(self, product_id, product_name, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price

class Cart_list(db.Model):
    __tablename__ = 'cart_list'
    cart_product_id = db.Column(db.Integer, unique=True, primary_key=True, )
    cart_product_price = db.Column(db.Integer)
    cart_product_name = db.Column(db.CHAR(50))
    quantity = db.Column(db.Integer)

    def __init__(self, cart_product_id, cart_product_price, cart_product_name, quantity):
        self.cart_product_id = cart_product_id
        self.cart_product_price = cart_product_price
        self.cart_product_name = cart_product_name
        self.quantity = quantity
