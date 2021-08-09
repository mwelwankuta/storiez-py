from flask import session, url_for, redirect
from bson.objectid import ObjectId

def like_controller(cursor, id):
    user_email = session['email']
    post = cursor['posts'].find_one({"_id": ObjectId(id)})
    post_likes = post['likes']
    
    if user_email not in post_likes:
        new_likes = [*post_likes, user_email]
        cursor['posts'].update_one({"_id": ObjectId(id)}, {'$set': {"likes": new_likes}})
        return redirect(url_for('home'))

    new_likes = [] 
    likes = post_likes
    
    for like in likes:
        if like == user_email:
            continue
        else:
            new_likes.append(like)
    
            
    cursor['posts'].update_one({"_id": ObjectId(id)}, {'$set': {"likes": new_likes}})
    return redirect(url_for('home'))