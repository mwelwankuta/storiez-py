from flask import request, render_template, session, redirect, url_for
from bson.objectid import ObjectId

def home_controller(cursor):
    posts = cursor['posts'].find({})
    if request.method == 'POST':
        return redirect(url_for('login'))
    
    # checking if session is empty
    if session.get('email') == False or session.get('email') == None:
        return redirect(url_for('login'))
    
    # when session is not empty
    if session['email']:
        
        # filtering posts to show
        filtered_posts = []
        for post in posts:
            if post['author'] in session['friends'] or post['author'] == session['email']:
                filtered_posts.append(post)
        return render_template('home.html', posts=filtered_posts)
        