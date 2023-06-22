# in this example two functions will battle over a single asset

import threading
import time
import random

# here is an asset in the global namespace
counter = 0
lock = threading.Lock() # this is a global Lock for threads to share

def workerA():
    '''this worker will access the global counter to increment it'''
    global counter # we now have access to the global asset called counter
    lock.acquire() # this thread will have exclusive acces to the lock
    try:
        while counter <10:
            counter += 1
            print(f'Worker A is increment counter to {counter}')
            time.sleep(random.randint(0,1)) # a random sleep of 0 or 1
    except Exception as err:
        print(f'Problem {err}')
    finally:
        lock.release()

def workerB():
    '''this worker will access the global counter to decrement it'''
    global counter # we now have access to the global asset called counter
    lock.acquire() # this thread will have exclusive acces to the lock
    try:
        while counter >-10:
            counter -= 1
            print(f'Worker B is decrement counter to {counter}')
            time.sleep(random.randint(0,1)) # a random sleep of 0 or 1
    except Exception as err:
        print(f'Problem {err}')
    finally:
        lock.release()

if __name__ == '__main__':
    # initially try working sequentially
    # workerA()
    # workerB()
    # NB a Thread is not an actual system thread, it is a thread access object
    tA = threading.Thread(target=workerA)
    tB = threading.Thread(target=workerB)
    # both threads try to access the SAME asset - this is dangerous and unpredicable
    tB.start() # whichever thread gets the lock first will win
    tA.start()
    tA.join()
    tB.join()