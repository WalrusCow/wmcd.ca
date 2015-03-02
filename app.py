import json
import os

from bottle import Bottle, request, response, static_file, HTTPError, redirect

import db
import template
from post import Post
from login import loginUser, requiresLogin

PATH_BASE = os.path.dirname(os.path.abspath(__file__))

app = Bottle()

class Error(HTTPError):
    def __init__(self, code, message):
        super().__init__(status=code, body={'message': message})

@app.error(400)
def error400(error):
    response.content_type = 'application/json'
    return json.dumps(error.body)

@app.error(401)
def error401(error):
    return error.body

@app.post('/post')
@requiresLogin
def newPost():
    ''' Create a new post. '''
    post = Post(request.forms)
    if not post.valid:
        return Error(400, 'Required fields missing')
    db.posts.insert(dict(post))
    redirect('/post/' + post.id)

@app.post('/login')
def login():
    user = request.forms.user.lower()
    password = request.forms.password

    session = loginUser(user, password)
    if type(session) == str:
        return Error(401, session)

    # TODO: Use secure=True for prod
    response.set_cookie('id', session.id, path='/', httponly=True)#, secure=True)
    response.set_cookie('user', user, path='/', httponly=True)#, secure=True)
    redirect('/write')

@app.get('/post/<postId>')
@template.file('post.mako')
def postTemplate(postId):
    post = db.posts.find_one({'id': postId})
    return dict(post)

@app.get('/login')
@template.file('login.mako')
@template.title('Sign In')
def loginTemplate():
    return dict()

@app.get('/write')
@template.file('write.mako')
@template.title('New Post')
@requiresLogin
def writeTemplate():
    return dict()

@app.get('<path:path>')
def serveStatic(path):
    ''' Fallback routing to anything under '/static' '''
    return static_file(path, root=os.path.join(PATH_BASE, 'static'))

if __name__ == '__main__':
    try:
        app.run(host='localhost', port=27134)
    finally:
        db.close()
