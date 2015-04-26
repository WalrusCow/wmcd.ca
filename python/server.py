import os

from bottle import Bottle, static_file

import blog.app

PATH_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

server = Bottle()

blog.app.error_handler = server.error_handler
server.mount('/blog', blog.app)

def serve_file(filename):
    return static_file(filename, root=os.path.join(PATH_BASE, 'static'))

@app.get('/')
def home():
    return serve_file('home.html')

@server.get('<path:path>')
def serve_static(path):
    ''' Fallback routing to any static files. '''
    return serve_file(path);

#TODO: Error pages
@server.error(400)
def error400(error):
    return 'Invalid request!'

@server.error(401)
def error401(error):
    return 'Deeeeeenied'

@server.error(404)
def error404(error):
    return 'Not found!'

@server.error(500)
def error500(error):
    return 'Something went wrong. My bad.'

if __name__ == '__main__':
    server.run(hostname='localhost', port=27134)
