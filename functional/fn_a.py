# only use classes if the built in structures are unsuitable
flag = True # boolean is handy
age = 37 # numbers are fine
greet = 'hello there' # string can easily hold collections of characters
# tuple, list, set and dictionary all have their place

def squareIt(x):
    '''return the square of a number'''
    return x*x

def addThem(x, y):
    '''return the sum of two numbers'''
    return x+y

def isOdd(n):
    '''return True or False depending on if the value is odd'''
    return n%2 !=0

if __name__ == '__main__':
    ''''''