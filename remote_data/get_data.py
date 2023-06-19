# in order to grab remote data from an API we use the 'requests' library
# you may need to 'pip install requests'
import requests
# NB older code may use the urllib to make requests
# here we will consume data from https://jsonplaceholder.typicode.com/photos

def getData(n):
    '''retrieve photos from an end-point API'''
    apiURL = f'https://jsonplaceholder.typicode.com/photos/{n}'
    response = requests.get(apiURL) # also put, post, delete etc.
    # we only want the json part of the returned response
    response_j = response.json() # or response.text() or response.xml()
    # the json is automatically parsed into Python structures
    # in this case we end up with a list of dictionaries
    # or else a single dictionary
    return response_j

if __name__ == '__main__':
    n = input('Which photo (1-99)? ') # a string!!!!
    # we ought to validate the number!!!!!
    photos = getData(int(float(n)))
    # print( photos[0] ) # the zeroth member of the list, which is a dictionary
    print(photos)