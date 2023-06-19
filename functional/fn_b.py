# Python does not have the concept of 'overloading'
# but we can do something very similar

# in Python a leading single asterisk means 'positional arguments'
def likeOverload(*args): # all the positional arguments are collected into a tuple
    '''this function will behave differently depending on the number of arguments'''
    if len(args) == 0:
        '''run the zero-argument version of this function'''
        print('there are no arguments')
    elif len(args) == 1:
        print(f'The only argument is {args[0]}')
    elif len(args) == 2:
        print(f'We have {args[0]} and {args[1]}')

if __name__ == '__main__':
    likeOverload()
    likeOverload('A')
    likeOverload(True, 'wow')