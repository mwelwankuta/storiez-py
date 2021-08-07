from flask import request, render_template, session, redirect, url_for
from secrets import token_urlsafe

def post_controller(cursor):

    # checking if session is empty
    if session.get('email') == False or session.get('email') == None:
        print('email is failed', session.get('email'))
        return redirect(url_for('login'))
    
    # when session is not empty
    if session['email']:        
        
        if request.method == "POST":
            
            user = session['email']
            name = session['name']
        
            text = request.form.get('text')
            image = request.files.get('image')
            
            print(image)
            # if user added an aimage        
            if image:
                # renamed file
                image_to_save = filename(image.filename)

                # if file is converted            
                if isinstance(image_to_save, str):
                    image.save(f'public/uploads/{image_to_save}')

                    post = {
                        "author": user,
                        "name": name,
                        "text": text,
                        "image": f'public/uploads/{image_to_save}'
                    }

                    cursor['posts'].insert_one(post)
                    return redirect(url_for('home'))
            
            if not text:
                return render_template('home.html', form_message="you need to add something to post")
            
            post = {
                "author": user,
                "name": name,
                "text": text
            }

            cursor['posts'].insert_one(post)
            return redirect(url_for('home'))
        
# rename file   
def filename(name):
    file = name.split('.')
    image_extentions = ['jpg','png','jpeg']
    extention = file[len(file) - 1]
    
    if extention not in image_extentions:
        return render_template('post.py',message="the image you uploaded is not supported by storiez")
    
    return f"{token_urlsafe(16)}.{extention}"