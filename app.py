from flask import Flask
from flask.wrappers import Response

app = Flask(__name__)

# Hello world
@app.route('/')
def hello_world():
    return Response("{'demo': 'successful!'}", status=200, mimetype='application/json')

@app.route('/hello/<myname>')
def hello_name(myname):
    return Response("{'YourName': '" + str(myname) + "'}", status=200, mimetype='application/json')

# Make the app run
if __name__ == '__main__':
    app.run()
