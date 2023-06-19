from functools import reduce

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
    '''use the functions'''
    # many coding solutions do not ned classes, just tidy functions
    # a 'pure' function is entirely predictable for given inputs
    print( squareIt(4), addThem(3, 6), isOdd(3) )
    # we can use a range and apply our function to every member
    sq_t = tuple( map(squareIt, range(1, 12)) )
    print(sq_t)
    # but what if we need a huuuuuuuuuuuge range of values
    sq_g = map( squareIt, range(1, 10**2) ) # we now have a generator
    print( sq_g ) # the values do not persist in memory
    # we can yield the next available members like this
    print( sq_g.__next__() ) # 1
    print( sq_g.__next__() ) # 4
    print( sq_g.__next__() ) # 9
    print( sq_g.__next__() ) # 16
    # we have an iterable object
    for item in sq_g:
        print(item, end=', ')

    # functiomal programming often uses filter...
    odd_l = list( filter( isOdd, range(-27, 28) ) )
    print( odd_l )
    # or we can make a generator
    odd_g = filter( isOdd, range( -10**10, 10**10 ) )
    print( odd_g.__next__() )
    print( odd_g.__next__() )
    print( odd_g.__next__() )
    print( odd_g.__next__() )
    # we can iterate...

    # we can use 'reduce' like this
    r = reduce( addThem, odd_g )
    print(r)
