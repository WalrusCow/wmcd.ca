import json
import os

import pymongo
from bottle import Bottle, request, response, HTTPError, redirect
from markdown2 import markdown

import template

import blog.db as db
import blog.posts as posts
from blog.login import loginUser, requiresLogin

PATH_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Bottle()

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
        raise HTTPError(status=400, body='Required fields missing')
    posts.create(post)
    redirect('post/' + post.id)

@app.post('/login')
def login():
    user = request.forms.user.lower()
    password = request.forms.password

    session = loginUser(user, password)
    if type(session) == str:
        raise HTTPError(status=401, body=session)

    prod = not bool(os.environ.get('WMCD_DEV'))
    response.set_cookie('id', session.id, path='/', httponly=True, secure=prod)
    response.set_cookie('user', user, path='/', httponly=True, secure=prod)
    redirect('write')

@app.get('/login')
@template.file('login.mako')
@template.title('Sign In')
def loginTemplate(): return {}

@app.get('/post/<postId>')
@template.file('post.mako')
def postTemplate(postId):
    post = posts.retrieve(postId)
    if post is None:
        raise HTTPError(status=404, body='No matching post found!')
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
def writeTemplate(): return {}

@app.get('/')
@template.file('blogHome.mako')
@template.title("William's Blog")
def indexTemplate():
    POST_LIMIT = 8
    offset = request.query.offset
    offset = int(offset) if offset.isnumeric() else 0

    totalPosts = db.posts.count()
    offset = min(offset, max(0, totalPosts - POST_LIMIT))

    nextOffset = offset + POST_LIMIT
    if nextOffset >= totalPosts:
        nextOffset = None

    if offset > 0:
        prevOffset = max(offset - POST_LIMIT, 0)
    else:
        prevOffset = None
    results = db.posts.find(limit=POST_LIMIT,
                            sort=[('timestamp', pymongo.DESCENDING)],
                            skip=offset)
    return {
        'nextOffset': nextOffset,
        'prevOffset': prevOffset,
        'posts': list(postForTemplate(posts.Post(p)) for p in results)
    }
