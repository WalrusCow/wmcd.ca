from bottle import Bottle, request, static_file

app = Bottle()


@app.post('/post')
def newPost():
    """ Create a new post. """
    postBody = request.json.get('body')
    print(postBody)

@app.get('/view/<postId>')
def viewPost(postId):
    """ Retrieve data about a post. """
    return 'Yes'

@app.get('/<filePath:path>')
def serve(filePath):
    return static_file(filePath, root='.')

app.run(host='localhost', port=27134)
