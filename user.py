# file name: user.py
# pwd: shoppingMall.zioyou/user.py
'''
Reference:
        쿼리: https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
        쇼핑몰샘플 -- http://sample.zioyou.com/gofruit/index.html

templates: login.html, profile.html, signup.html, forgot-password.html, change-password.html, profile-edit.html,
        setting.html
'''

from flask import Blueprint, redirect, render_template, url_for, session, request
from start_shoppingmall.models.shoppingmall_info import Accounts
from start_shoppingmall import db

bp = Blueprint('bp', __name__, static_folder='static', template_folder='templates', url_prefix='')

# profile Page
@bp.route('/profile')
def profile():
        # if logged in
        if 'logged_in' in session:
                return render_template('profile.html', pass_user_name=session['user_name'], pass_user_email=session['user_email'])
        return redirect(url_for('bp.login'))

# login Page
@bp.route('/login', methods=['POST', 'GET'])
def login():
        # if user not logged in
        if 'logged_in' not in session:
                # check user account with user_email
                if request.method == 'POST':
                        user_email = request.form["user_email"]
                        check_account = Accounts.query.get(user_email)
                        print(check_account)

                        # success to login
                        if check_account is not None:
                                session['logged_in'] = True
                                session['user_email'] = check_account.user_email
                                session['user_name'] = check_account.user_name
                                session['user_password'] = check_account.user_password
                                db.session.remove()
                                print(session['user_password'])
                                print('로그인 성공!')
                                return redirect(url_for('index'))
                        # fail to login
                        else:
                                print('로그인 실패!')
                                db.session.remove()
        # if already logged in
        else:
                print("이미 로그인 되어있습니다. 로그아웃 하신 후 다른 아이디로 로그인 해주세요!")
                return redirect(url_for("index"))
        return render_template("login.html")


# sign up Page
@bp.route('/signup', methods=['POST', 'GET'])
def signup():
        # if user not logged in
        if 'logged_in' not in session:
                # get data from form
                if request.method == 'POST':
                        user_email = request.form['user_email']
                        user_name = request.form['user_name']
                        user_password = request.form['user_password']

                        check_account = Accounts.query.get(user_email)
                        print(check_account)
                        # if email is new
                        if check_account is None:
                                insertUser = Accounts(user_email, user_name, user_password)
                                db.session.add(insertUser)
                                db.session.commit()
                                db.session.remove()
                                print('가입에 성공하셨습니다!')
                                return redirect(url_for('bp.login'))
                        # email already exists
                        else:
                                print('아이디가 중복됩니다!')
        # if already logged in
        else:
                print("로그아웃 후 다시 시도하여주세요")
        return render_template("signup.html")


# forgot-password Page
@bp.route('/forgot-password')
def forgot_password():
        return render_template("forgot-password.html")

# logout Page
@bp.route('/logout')
def logout():
        # logout, all sessions are None
        session.pop("user_email", None)
        session.pop("user_name", None)
        session.pop("user_password", None)
        session.pop("logged_in", None)
        print("로그아웃 하셨습니다")
        # logout then redirect to login page
        return redirect(url_for("bp.login"))


# change user password
@bp.route('/change-password', methods=['POST', 'GET'])
def change_password():
        # if user logged in
        if 'logged_in' in session:
                print('로그인중입니다! 비밀번호를 변경하실 수 있습니다!')
                if request.method == 'POST':
                        updateUser = Accounts.query.get(session['user_email'])
                        print(updateUser)
                        user_password = request.form.get('user_password')
                        new_password = request.form.get('new_password')
                        confirm_new_password = request.form.get('confirm_new_password')

                        if user_password != updateUser.user_password:
                                print("현재 비밀번호가 일치하지 않습니다")
                        elif new_password == user_password:
                                print("새로운 비밀번호가 아닙니다")
                        elif new_password != confirm_new_password:
                                print("새로운 비밀번호가 일치하지 않습니다")
                        else:
                                updateUser.user_password = confirm_new_password
                                db.session.commit()
                                print("비밀번호가 바뀌었습니다!")
                                return redirect(url_for('bp.setting'))
        # if not logged in
        else:
                print("비밀번호를 변경하시려면 먼저 로그인 해주세요!")
        return render_template("change-password.html")

# edit user profile --> Cannot update Primary Key
@bp.route('/profile-edit', methods=['GET', 'POST'])
def profile_edit():
        # if logged in
        if 'logged_in' in session:
                print('로그인중입니다. 프로필을 변경하실 수 있습니다')
                updateUser = Accounts.query.get(session['user_email'])
                print(updateUser)
                if request.method == 'POST':
                        new_name = request.form.get('new_name')
                        new_email = request.form.get('new_email')
                        print(new_name, new_email)
                        updateUser.user_name = new_name
                        updateUser.user_email = new_email
                        db.session.commit()
        # if not logged in
        else:
                print("프로필을 변경하시려면 먼저 로그인 해주세요!")
        return render_template("profile-edit.html", pass_user_name=session['user_name'], pass_user_email=session['user_email'])

# setting page
@bp.route('/setting')
def setting():
        # if logged in
        if 'logged_in' in session:
                return render_template("setting.html", pass_user_name=session['user_name'], pass_user_email=session['user_email'])
        return render_template("setting.html")

