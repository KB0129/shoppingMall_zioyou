# file name: product.py
# pwd: shoppingMall_zioyou/product.py
'''
Reference:

templates: all-products.html, all-products-list.html, product-details.html
'''

from flask import Blueprint, request, render_template, session
from start_shoppingmall.models.shoppingmall_info import Product

# blueprint
bp3 = Blueprint('bp3', __name__, static_folder='static', template_folder='templates', url_prefix='')

# search the product
@bp3.route('/search_product', methods=['POST', 'GET'])
def search_product():
    search_product_name = request.form['search_product_name']
    searchItem = Product.query.filter(Product.product_name.contains(search_product_name))
    return render_template("search-result.html", searchItem=searchItem)

# list page
@bp3.route('/all-products')
def all_product():
    # list product order by price(ascending)
    all_data = Product.query.order_by(Product.product_price.asc()).all()
    return render_template('all-products.html', all_data=all_data, pass_user_name=session['user_name'], pass_user_email=session['user_email'])

# show all products on the list
@bp3.route('/all-products-list')
def all_product_list():
    # list product order by price(ascending)
    all_data = Product.query.order_by(Product.product_price.asc()).all()
    return render_template('all-products-list.html', all_data=all_data, pass_user_name=session['user_name'], pass_user_email=session['user_email'])

# show the details of product
@bp3.route('/product-details/<product_id>')
def product_details(product_id):
    # detail information
    details_data = Product.query.get(product_id)
    return render_template("product-details.html", details_data=details_data, pass_user_name=session['user_name'], pass_user_email=session['user_email'])

# add, update, delete product
@bp3.route('/add_product')
def add_product():
    # detail information
    # details_data = Product.query.get(product_id)
    return render_template("product.html")