from flask import render_template
from bson.objectid import ObjectId


def view_post_controller(cursor, id):
    post = cursor['posts'].find_one({'_id': ObjectId(id)})

    data = {
        'author': post['author'],
        'name': post['name'],
        'text': '',
        'image': '',
        'id': id,
        'comments': post['comments']
    }

    # try to include text
    try:
        post_text = post['text']
        if post_text:
            data['text'] = post_text
    except:
        pass

    # try to include image
    try:
        post_image = post['image']
        if post['image']:
            data['image'] = post_image
    except:
        pass

    return render_template('post.html', data=data)
