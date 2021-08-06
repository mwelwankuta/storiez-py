# module imports
from flask import render_template

# controller imports
from controllers.create_account import create_account_controller
from controllers.login import login_controller
from controllers.home import home_controller
from controllers.people import people_controller
from controllers.post import post_controller
from controllers.post import post_controller
from controllers.logout import logout_countroller
from controllers.delete import delete_controller

# endpoints
def endpoints(app, cursor):
    
    @app.route('/', methods=['POST', 'GET'])
    def home():
        return home_controller(cursor)

    @app.route('/login', methods=['POST', 'GET'])
    def login():
        return login_controller(cursor)

    @app.get('/logout')
    def logout():
        return logout_countroller()

    @app.route('/create-account', methods=['POST', 'GET'])
    def create_account():
        return create_account_controller(cursor)

    @app.route('/post', methods=['POST', 'GET'])
    def post():
        return post_controller(cursor)

    @app.route('/people', methods=['POST', 'GET'])
    def people():
        return people_controller(cursor)

    @app.route('/created-account')
    def created_account():
        return render_template("auth/created-account.html")

    @app.route('/delete/<string:id>', methods=['POST'])
    def delete(id):
        return delete_controller(cursor, id)
    
    return home, login,logout, create_account, post, people, create_account, created_account ,delete