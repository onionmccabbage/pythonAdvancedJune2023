# we may need to pip install flask
from flask import Flask

# Flask is a basic simple web server
# NB use Django for a fully-fledged web content management server

# flask is a proepr web server, handling basic HTML requests
app = Flask(__name__) # any name will do

# next we declare routes, which are http pathways to content
@app.route('/') # this is the ROOT of our service
def root():
    '''here we decide what content will be returned from the root of our service'''
    return 'Welcome to this flask server'

@app.route('/home')
def home():
    '''return some basic HTML'''
    content = '<h2>Here is the home page</h2>'
    return content


if __name__ == '__main__':
    app.run() # start the flask server