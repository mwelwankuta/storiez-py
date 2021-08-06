from flask import request, render_template, session, redirect, url_for

def people_controller(cursor):
    
    if request.method == 'GET':
         # checking if session is empty
        if session.get('email') == False or session.get('email') == None:
            return redirect(url_for('login'))
        
        # when session is not empty
        my_email = session['email']
        db_my = cursor['users'].find_one({"email/phone": my_email}) 
        
        if session['email']:
            return render_template('people.html', friends=db_my['friends'])
        
    my_email = session['email']
    friend_email = request.form.get('friend')
    
    db_my = cursor['users'].find_one({"email/phone": my_email})
    db_friend = cursor['users'].find({"email/phone": friend_email})

    # checking if friend exists
    if db_friend.count() == 0:
        print('db_friend',db_friend)
        return render_template('people.html', message="User does not exist")

    # checking in already friends
    if friend_email in db_my['friends']:
        return render_template('people.html', message=f"{db_friend[0]['name']} is already your friend")
    
    # reject adding self as friend
    elif my_email == friend_email:
        return render_template('people.html', message="you can not be friends with your self")
    
    # adding friend
    else:
        # insert friend email 
        cursor['users'].update_one({"email/phone": my_email}, {
                                '$set': {"friends": [*db_my['friends'], friend_email]}})
        
        # insert user email in friend
        cursor['users'].update_one({"email/phone": friend_email}, {
                                '$set': {"friends": [*db_friend[0]['friends'], my_email]}})
        
        # reset friends in session 
        session['friends'] = db_my['friends']
        
        return render_template('people.html', message=f"you and {db_friend[0]['name']} are now friends")