from flask import Flask 
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return 'Your browser is %s' % user_agent

@app.route('/user/<name>')
def user_index(name):
    return 'Hello %s ' % name

if __name__=='__main__':
    app.run(debug=True)