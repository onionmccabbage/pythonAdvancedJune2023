import doctest # built in to Python

# doctest lets us write tests inside the docstring
def cube(x):
    '''return the cube of x
    >>> cube(2)
    8
    >>> cube(9)
    729                                                      
    >>> cube(-3)
    -27
    >>> cube(-1) 
    -1
    '''
    return x**3

def squares(a, b):
    '''return the square of every number from a to b
    >>> squares(1, 6)
    [1, 4, 9, 16, 25]
    >>> squares(1, 11)
    [1, 4, ..., 100] # doctest: +ELLIPSIS
    '''
    answer_l = []
    for i in range(a, b):
        answer_l.append(i**2)
    return answer_l


if __name__ == '__main__':
    # print( cube(2) ) # 8
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE, verbose=True)