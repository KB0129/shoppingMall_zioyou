'''
Reference:

지오유 홈페이지 샘플 -- http://sample.zioyou.com/gofruit/cart.html

cart.html, checkout.html, my-order.html, thankyou.html, checkout.html

quantity calculator: https://stackoverflow.com/questions/58160356/how-to-perform-calculation-on-a-for-loop-jinja-template-field-using-javascript
                    https://www.jqueryscript.net/form/Do-Calculations-Form-Fields-AutoCalc.html
'''
# file name: cart.py
# pwd: shoppingMall_zioyou/cart.py

from flask import Blueprint, request, render_template, redirect, url_for, session
from start_shoppingmall.models.shoppingmall_info import Cart_list, Product
from start_shoppingmall import db

# blueprint
bp2 = Blueprint('bp2', __name__, static_folder='static', template_folder='templates', url_prefix='')

# add item in cart
@bp2.route('/add_cart/<product_id>', methods=['POST', 'GET'])
def add_cart(product_id):
    # if user logged in
    if 'logged_in' in session:
        if request.method == 'POST':
            # get data from DB(table: products)
            product = Product.query.get(product_id)
            product_name = product.product_name
            product_price = product.product_price
            quantity = 1 # quantity is "1" at first

            # insert data(table: cart_list)
            inputItem = Cart_list(product_id, product_price, product_name, quantity)
            db.session.add(inputItem)
            db.session.commit()
    # user should logged in to add cart
    else:
        print("로그인이 필요합니다!")
    return redirect(url_for('bp2.cart_list'))

# delete item in cart
@bp2.route('/delete_cart/<product_id>')
def delete_cart(product_id):
    # if user logged in
    if 'logged_in' in session:
        # delete item from DB(table: cart_list)
        deleteItem = Cart_list.query.get(product_id)
        db.session.delete(deleteItem)
        db.session.commit()
    # user should logged in to delete item from cart
    else:
        print("로그인이 필요합니다!")
    return redirect(url_for('bp2.cart_list'))

# cart page
@bp2.route('/cart', methods=['GET', 'POST'])
def cart_list():
    # list products in cart
    all_data = Cart_list.query.order_by(Cart_list.cart_product_price.asc()).all()
    return render_template('cart.html',  all_data=all_data, pass_user_name=session['user_name'], pass_user_email=session['user_email'])

# check out page
@bp2.route('/checkout')
def check_out():
    return render_template('checkout.html')

# my order page
@bp2.route('/my-order')
def my_order():
    return render_template('my-order.html')
# thank you page
@bp2.route('/thank_you')
def thank_you():
    return render_template('thankyou.html')