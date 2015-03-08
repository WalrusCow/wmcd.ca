from bottle import Bottle
from app import app

if __name__ == '__main__':
    server = Bottle()
    server.mount('/blog', app)
    server.run(hostname='localhost', port=27134)
