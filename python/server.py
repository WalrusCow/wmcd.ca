import os

from bottle import Bottle, static_file

import blog.app
import wmcd.app

PATH_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

server = Bottle()

blog.app.error_handler = server.error_handler
wmcd.app.error_handler = server.error_handler
server.mount('/blog', blog.app)
server.merge(wmcd.app)

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

@server.get('<path:path>')
def serveStatic(path):
    ''' Fallback routing to anything under '/static' '''
    return static_file(path, root=os.path.join(PATH_BASE, 'static'))

if __name__ == '__main__':
    server.run(hostname='localhost', port=27134)
