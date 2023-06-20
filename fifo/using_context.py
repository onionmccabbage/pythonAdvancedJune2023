# in Python 3 we have a context manager
from contextlib import contextmanager
import sys

@contextmanager # make our function behave as a context manager
def outputRedirect( newOutput ):
    '''Redirect any printed output to a differnet context'''
    old_stdout = sys.stdout # make a record of the current output stream
    sys.stdout = newOutput  # set eh default output to our new output stream
    yield # our function will yield the next available object to be written
    sys.stdout = old_stdout # return to the previous output stream

if __name__ == '__main__':
    sys.stdout.write('This uses the standard print output stream') # NB no new-line at the end!
    # we can create a different output stream, such as a file accecss object
    with open('my_log.txt', 'a') as fobj: # using 'with' will automatically close the file when done
        with outputRedirect(fobj):
            '''any print statements will be redirected'''
            print('this will be written to the text file')
    print('all output is now returned to the default output stream')