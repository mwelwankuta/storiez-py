from flask import session, redirect, url_for

def logout_countroller():
    session.pop('friends')
    session.pop('email')
    session.pop('name')

    return redirect(url_for('login'))