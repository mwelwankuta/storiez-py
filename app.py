from flask import Flask, render_template, redirect, url_for, session
from flask_cors import CORS
from pymongo import MongoClient

# controller imports
from controllers.create_account import create_account_controller
from controllers.login import login_controller
from controllers.home import home_controller
from controllers.people import people_controller
from controllers.post import post_controller

# init app
app = Flask(__name__, static_folder="public")
app.secret_key = "ThDda4jd1-23;123=30k"
CORS(app)

db = MongoClient('mongodb://localhost:27017')
cursor = db['storiez']


@app.route('/', methods=['POST', 'GET'])
def home():
    return home_controller(cursor)


@app.route('/login', methods=['POST', 'GET'])
def login():
    return login_controller(cursor)


@app.get('/logout')
def logout():
    session.pop('friends')
    session.pop('email')
    session.pop('name')

    return redirect(url_for('login'))


@app.route('/create-account', methods=['POST', 'GET'])
def create_account():
    return create_account_controller(cursor)


@app.route('/post', methods=['POST', 'GET'])
def post():
    return post_controller(cursor)


@app.route('/people', methods=['POST', 'GET'])
def people():
    return people_controller(cursor)


@app.get('/created-account')
def created_account():
    return render_template("auth/created-account.html")


# @app.get('/delete')
# def delete():
#     cursor['posts'].remove()
#     return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
