from flask import request, render_template, session, redirect, url_for


def post_controller(cursor):

    # checking if session is empty
    if session.get('email') == False or session.get('email') == None:
        print('email is failed', session.get('email'))
        return redirect(url_for('login'))
    # when session is not empty
    else:
        if session['email']:
            user = session['email']
            name = session['name']
            caption = request.form.get('caption')
            image = request.files.get('image')

            if request.method == "GET":
                return render_template('post.html')

            if not image:
                return render_template('post.html', message="you didn't not add an image")
            
            image.save(f'public/uploads/{image.filename}')

            post = {
                "author": user,
                "name": name,
                "caption": caption,
                "image": f'public/uploads/{image.filename}'
            }

            cursor['posts'].insert_one(post)
            return redirect(url_for('home'))
