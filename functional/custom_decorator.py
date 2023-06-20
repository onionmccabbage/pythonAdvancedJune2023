# decorators add something to what we already have

# maybe we need to examine what the incoming positonal and keyword arguments are
def showArgs(f): # here we expect a function to be passed in to this function
    '''This will be a decorator for other functions
       Reveal the positional and keyword arguments of any decorated function'''
    def newFunc(*args, **kwargs):
        print(f'Running a function called {f.__name__}')
        print(f'The positional arguments are {args}')
        print(f'The keyword arguments are {kwargs}')
        # we must return the original function beign decorated
        return f(*args, **kwargs)
    return newFunc # NB no brackets - we are not calling it here

@showArgs # apply our decorator to ANY function
def raisePower(m, n):
    '''raise m to the power of n'''
    return m**n

@showArgs
def squareIt(x):
    '''return the square of a number'''
    return x*x

@showArgs
def addThem(x, y):
    '''return the sum of two numbers'''
    return x+y

@showArgs
def isOdd(n):
    '''return True or False depending on if the value is odd'''
    return n%2 !=0

if __name__ == '__main__':
    r = raisePower(10, n=3)
    print(r)
    addThem(x=3, y=5)
    squareIt(999)
