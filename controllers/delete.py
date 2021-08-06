from flask import request, redirect, url_for
from bson.objectid import ObjectId
import os

def delete_controller(cursor, id):
    if request.method == 'POST':
        # remove from db
        post = cursor['posts'].find_one_and_delete({'_id': ObjectId(id)})
        image = post['image']
        
        # remove from directory
        os.remove(image)
        
        return redirect(url_for('home'))