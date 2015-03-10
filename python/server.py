import os

from bottle import Bottle, static_file

import blog.app
import wmcd.app

PATH_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

server = Bottle()

@server.get('<path:path>')
def serveStatic(path):
    ''' Fallback routing to anything under '/static' '''
    return static_file(path, root=os.path.join(PATH_BASE, 'static'))

if __name__ == '__main__':
    server.mount('/blog', blog.app)
    server.merge(wmcd.app)
    server.run(hostname='localhost', port=27134)
