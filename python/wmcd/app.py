from bottle import Bottle

import template

app = Bottle()

@app.get('/')
@template.file('home.mako')
@template.title('William McDonald')
def homeTemplate(): return {}

@app.get('/code')
@template.file('code.mako')
@template.title('Code')
def codeTemplate(): return {}

@app.get('/code/tetvas')
@template.file('tetvas.mako')
@template.title('Tetvas')
def tetvasTemplate(): return {}

@app.get('/code/life')
@template.file('life.mako')
@template.title('Game of Life')
def lifeTemplate(): return {}

@app.get('/code/snake')
@template.file('snake.mako')
@template.title('Snake')
def snakeTemplate(): return {}
