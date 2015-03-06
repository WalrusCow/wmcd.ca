import json
import os

import pymongo
from bottle import Bottle, request, response, static_file, HTTPError, redirect
from markdown2 import markdown

import db
import posts
import template
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
    # Map form fields to post fields
    postData = {
        'body': request.forms['body'],
        'title': request.forms['title'],
        'author': request.forms['author']
    }
    post = posts.Post(postData)
    if not post.valid:
        return Error(400, 'Required fields missing')
    posts.create(post)
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

@app.get('/login')
@template.file('login.mako')
@template.title('Sign In')
def loginTemplate():
    return dict()

@app.get('/post/<postId>')
@template.file('post.mako')
def postTemplate(postId):
    post = posts.retrieve(postId)
    if post is None:
        return Error(404, 'No matching post found!')
    prevPost = posts.previousPost(post)
    nextPost = posts.nextPost(post)
    return {
        'title': post.title,
        'post': postForTemplate(post),
        'prevPost': postForTemplate(prevPost) if prevPost else None,
        'nextPost': postForTemplate(nextPost) if nextPost else None
    }

def postForTemplate(post):
    if not post: return dict()
    return {
        'body': markdown(post.body),
        'title': post.title,
        'author': post.author,
        'id': post.id,
        'timestamp': post.timestamp.strftime('%B %d, %Y')
    }

@app.get('/write')
@template.file('write.mako')
@template.title('New Post')
@requiresLogin
def writeTemplate():
    return dict()

@app.get('/')
@template.file('home.mako')
@template.title("William's Blog")
def indexTemplate():
    results = db.posts.find(limit=5, sort=[('timestamp', pymongo.DESCENDING)])
    return {'posts': list(postForTemplate(posts.Post(p)) for p in results)}

@app.get('<path:path>')
def serveStatic(path):
    ''' Fallback routing to anything under '/static' '''
    return static_file(path, root=os.path.join(PATH_BASE, 'static'))

if __name__ == '__main__':
    try:
        app.run(host='localhost', port=27134)
    finally:
        db.close()
