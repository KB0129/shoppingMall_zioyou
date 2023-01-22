# file name: index.py
# pwd: shoppingMall_zioyou/index.py

'''
templates: index.html, introduction.html
'''

from start_shoppingmall import app
from flask import render_template, session
from user import bp
from cart import bp2
from product import bp3
from start_shoppingmall.models.shoppingmall_info import Product

# register blueprints
app.register_blueprint(bp)
app.register_blueprint(bp2)
app.register_blueprint(bp3)

# index page
@app.route("/index")
def index():
    # show products on index page
    all_data = Product.query.order_by(Product.product_price.asc()).all()
    if 'logged_in' in session:
        return render_template("index.html", all_data=all_data, pass_user_name=session['user_name'], pass_user_email=session['user_email'])
    return render_template("index.html")

# introduction page
@app.route('/')
def introduction():
    if 'logged_in' in session:
        return render_template("introduction.html", pass_user_name=session['user_name'])
    return render_template("introduction.html")

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)




