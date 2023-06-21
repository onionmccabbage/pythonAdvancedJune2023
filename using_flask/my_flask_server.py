# we may need to pip install flask
from flask import Flask
import json
import requests

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

@app.route('/latlon')
def latlon():
    '''return some SJON containing latitude and longitude'''
    ll_d = {"geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }}
    ll_j = json.dumps(ll_d)
    return ll_j

@app.route('/greet')
@app.route('/greet/<name>') # this allows a parameter called 'name'
# we could have several parameters, all with defaults in the function definition
def greet(name='Earthling'): # we need a default for 'name'
    '''respond with a generic greeting, or greet the named user'''
    content = f'<h3>Greetings {name}</h3>'
    return content

# sometimes it is useful to have several pathsways to the same content
@app.route('/aluminium')
@app.route('/aluminum')
@app.route('/alluminium')
@app.route('/alumium')
@app.route('/alumnium')
def al():
    return 'the correct spelling is aluminium'

# we can make our server a proxy for other content
# here we will retrieve data from JSONPLACEHOLDER based on the parameters passed in
@app.route('/data/<cat>') # specify a category and return ALL json from that category
@app.route('/data/<cat>/<id>') # sa category and id then return json for unique id
def data(cat='albums', id=''):
    apiUrl = f'https://jsonplaceholder.typicode.com/{cat}/{id}'
    response = requests.get(apiUrl)
    response_j = response.json() # or html, text etc
    # we could do some pre-procesing, e.g. filter, clean, authenticate...
    return response_j



if __name__ == '__main__':
    app.run() # start the flask server