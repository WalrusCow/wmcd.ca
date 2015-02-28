import os
import json

import pymongo
from bottle import Bottle, request, response, static_file, HTTPError

import db
from makoutil import serveTemplate

PATH_BASE = os.path.dirname(os.path.abspath(__file__))

app = Bottle()

class Error(HTTPError):
    def __init__(self, code, message):
        super().__init__(status=code, body={'error':message})

@app.error(400)
def error400(error):
    response.content_type = 'application/json'
    return json.dumps(error.body)

@app.post('/post')
def newPost():
    ''' Create a new post. '''
    POST_FIELDS = ('body', 'title')
    post = {k : request.json.get(k) for k in POST_FIELDS}
    if any(v is None for v in post.values()):
        # Error: Missing required fields
        raise Error(400, 'Required fields missing')
    return 'Good to go'

@app.get('/view/<postId>')
def viewPost(postId):
    ''' Retrieve data about a post. '''
    return

@app.get('/post')
@serveTemplate('post.mako')
def postTemplate():
    return {'body': 'Some body', 'title': 'A title'}

@app.get('<path:path>')
def serveStatic(path):
    ''' Fallback routing to anything under '/static' '''
    return static_file(path, root=os.path.join(PATH_BASE, 'static'))

if __name__ == '__main__':
    try:
        app.run(host='localhost', port=27134)
    finally:
        db.close()
