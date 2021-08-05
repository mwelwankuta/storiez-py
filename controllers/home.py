from flask import request, render_template, session, redirect, url_for

def home_controller(cursor):
    posts = cursor['posts'].find()
    if request.method == 'POST':
        return redirect(url_for('login'))
    
    else:
        # checking if session is empty
        if session.get('email') == False or session.get('email') == None:
            return redirect(url_for('login'))
        # when session is not empty
        else:
            if session['email']:
                return render_template('home.html', posts=posts)
        

        
    
    