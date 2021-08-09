from flask import request, session, redirect, render_template
from bson.objectid import ObjectId

def comment_controller(cursor, post_id):
    user_email = session['email']
    user_name = session['name']
    
    comment = request.form.get('comment')
    
    if len(comment) == 0:
        return render_template(f'post.html{post_id}', people='errro')
    
    post = cursor['posts'].find_one({"_id": ObjectId(post_id)})
    post_comments = post['comments']
    
    new_comments = [*post_comments, {'email': user_email,'name':user_name, 'comment':comment}]
    cursor['posts'].update_one({"_id": ObjectId(post_id)}, {'$set': {"comments": new_comments}})
    
    return redirect(f'/post/{post_id}')