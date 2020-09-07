# pip install virtualenv
# python -m virtualenv bin
# cd bin\Scripts
# activate
# pip install flask flask-sqlalchemy flask-login
# set FLASK_APP=app.py # linux: export FLASK_APP=app.py
# set FLASK_DEBUG=True # export FLASK_DEBUG=True
# python
# from app import db
# db.create_all()
# flask run
# https://sqlitebrowser.org/dl/
# https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/

from flask import Flask, redirect, render_template, request
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SECRET_KEY'] = '000000'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))


@login_manager.user_loader
def get(id):
    return User.query.get(id)


@app.route('/', methods=['GET'])
@login_required
def get_home():
    return render_template('home.html')


@app.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route('/signup', methods=['GET'])
def get_signup():
    return render_template('signup.html')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']

    if not email or not password:
        return redirect('login') 

    user = User.query.filter_by(email=email).first()
    if check_password_hash(user.password, password):
        login_user(user)
        return redirect('/')
    else:
        return redirect('login')


@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    if not username and not email and not password:
        _hashed_password = generate_password_hash(password)
        user = User(username=username, email=email, password=_hashed_password)
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(email=email).first()
        login_user(user)
        return redirect('/')
    else:
        return redirect("signup")


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect('/login')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
