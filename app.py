import os

from bottle import Bottle, request, static_file
from mako.template import Template
from mako.lookup import TemplateLookup

from makoutil import serveTemplate

PATH_BASE = os.path.dirname(os.path.abspath(__file__))

app = Bottle()

@app.post('/post')
def newPost():
    ''' Create a new post. '''
    postBody = request.json.get('body')
    print(postBody)

@app.get('/view/<postId>')
def viewPost(postId):
    ''' Retrieve data about a post. '''
    return 'Yes'

@app.get('/post')
@serveTemplate('post.mako')
def postTemplate():
    return {'body': 'Some body', 'title': 'A title'}

@app.get('<path:path>')
def serveStatic(path):
    ''' Fallback routing to anything under '/static' '''
    return static_file(path, root=os.path.join(PATH_BASE, 'static'))

if __name__ == '__main__':
    app.run(host='localhost', port=27134)
