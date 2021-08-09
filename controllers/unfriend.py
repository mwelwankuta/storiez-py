from flask import session, redirect, url_for

def unfriend_controller(cursor, id):
    user_email = session['email']
    db_friends = cursor['users'].find_one({"email/phone": user_email})
    
    new_friends = [] 
    friends = db_friends['friends']
    
    # filtering through friends    
    for friend in friends:
        if friend == id:
            continue
        else:
            new_friends.append(friend)
    
    # resetting friends in session
    session['friends'] = new_friends
    
    cursor['users'].update_one({"email/phone": user_email}, {'$set': {"friends": new_friends}})
    return redirect(url_for('people'))