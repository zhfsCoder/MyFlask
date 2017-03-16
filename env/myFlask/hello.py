from flask import Flask 
from flask import request
from flask.ext.script import Manager

app = Flask(__name__)


manager = Manager(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return 'Your browser is %s' % user_agent

@app.route('/user/<name>')
def user_index(name):
    return 'Hello %s ' % name

if __name__=='__main__':
    manager.run()