import os
import json

import pymongo
from bottle import Bottle, request, response, static_file, HTTPError

import db
from makoutil import serveTemplate
from post import Post

PATH_BASE = os.path.dirname(os.path.abspath(__file__))

app = Bottle()

class Error(HTTPError):
    def __init__(self, code, message):
        super().__init__(status=code, body={'message': message})

@app.error(400)
def error400(error):
    response.content_type = 'application/json'
    return json.dumps(error.body)

@app.post('/post')
def newPost():
    ''' Create a new post. '''
    POST_FIELDS = ('body', 'title', 'author')
    post = Post(request.json)
    if not post.valid:
        return Error(400, 'Required fields missing')
    db.posts.insert(dict(post))
    return {'id': post.id}

@app.get('/post/<postId>')
@serveTemplate('post.mako')
def postTemplate(postId):
    post = db.posts.find_one({'id': postId})
    return dict(post)

@app.get('/write')
@serveTemplate('write.mako')
def writeTemplate():
    return {'title': 'Write a post'}

@app.get('<path:path>')
def serveStatic(path):
    ''' Fallback routing to anything under '/static' '''
    return static_file(path, root=os.path.join(PATH_BASE, 'static'))

if __name__ == '__main__':
    try:
        app.run(host='localhost', port=27134)
    finally:
        db.close()
