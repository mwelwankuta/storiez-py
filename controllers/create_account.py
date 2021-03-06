from flask import request, render_template, session, redirect, url_for

def create_account_controller(cursor):
    if request.method == "GET":
              # checking if session is empty
        if session.get('email') == False or session.get('email') == None:
            print('email is failed',session.get('email'))
            return render_template("auth/create-account.html")
        
        # when session is not empty
        if session['email']:
            return render_template('home.html')
        
        
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm')

    user = {
        "name": name,
        "email/phone": email,
        "password": password,
        "friends": []
    }
    
    session['email'] = email
    session['friends'] = []
    session['name'] = name

    if cursor['users'].find_one({"email/phone": email}):
        return render_template('auth/create-account.html', error="the email/phone you entered is already being used")
    elif confirm_password != password:
        return render_template('auth/create-account.html', error="your password do not match")

    cursor['users'].insert_one(user)
    return redirect(url_for("created_account"))
    