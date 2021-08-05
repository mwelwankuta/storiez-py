from flask import request, render_template, session, redirect, url_for

def login_controller(cursor):
    if request.method == 'GET':
        # checking if session is empty
        if session.get('email') == False or session.get('email') == None:
            return render_template("auth/login.html")
        # when session is not empty
        else:
            if session['email']:
                return render_template('post.html')     
        
    
    # get login values
    email = request.form.get('email')
    password = request.form.get('password')

    # find document with similar values
    user = cursor['users'].find_one({"email/phone": email})
   
    # found matching document
    if user and password == user['password']:
        # set values to session
        session['name'] = user['name']
        session['friends'] = user['friends']
        session['email'] = user['email/phone']
        print('logged in by email')
        return redirect(url_for('home'))
    
    # passwords did not match
    elif user and password != user['password']:
        return render_template("auth/login.html", error="your email/phone or password do not match, try again", email_value=email)
    
    # no mathing document found
    elif user == None:
        return render_template("auth/login.html", error="there was problem finding your account")