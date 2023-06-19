# as well as positional arguments, python can handle keyword arguments
def doStuff(**kwargs): # double-asterisk indicate a dict of keyword arguments
    '''here we expect keyword aruments'''
    print(kwargs) # all the keyword args will be in a dictionary

def seeBoth(*args, **kwargs):
    print( f'positional args: {args} \nkeyword arguments: {kwargs} ' )

if __name__ == '__main__':
    doStuff()
    doStuff(x=1)
    doStuff(x=1, y=2)
    doStuff(x=1, y=2, z=True)
    doStuff(x=1, y=2, z=True, f=doStuff)

    seeBoth()
    seeBoth(4,3,2,{}, [], s=True, w=doStuff, nnn='this is clever')

    