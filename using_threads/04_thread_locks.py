# in this example two functions will battle over a single asset

import threading
import time
import random

# here is an asset in the global namespace
counter = 0

def workerA():
    '''this worker will access the global counter to increment it'''
    global counter # we now have access to the global asset called counter
    try:
        while counter <100:
            counter += 1
            print(f'Worker A is increment counter to {counter}')
            time.sleep(random.randint(0,1)) # a random sleep of 0 or 1
    except Exception as err:
        print(f'Problem {err}')

def workerB():
    '''this worker will access the global counter to decrement it'''
    global counter # we now have access to the global asset called counter
    try:
        while counter >-100:
            counter -= 1
            print(f'Worker B is decrement counter to {counter}')
            time.sleep(random.randint(0,1)) # a random sleep of 0 or 1
    except Exception as err:
        print(f'Problem {err}')


if __name__ == '__main__':
    # initially try working sequentially
    workerA()
    workerB()