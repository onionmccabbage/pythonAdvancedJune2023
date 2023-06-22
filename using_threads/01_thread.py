from threading import Thread
import random
import time

def myFn(n):
    '''This is a normal function. Like all functions it can be invoked on the main thread
    Also (like all functions) it can be invoked on its own thread'''
    for i in range(1, 10):
        print(f'{n} is sleeping')
        time.sleep( random.random()*0.1) #sleep for up to 1/10 sec

if __name__ == '__main__':
    # this runs on the main thread
    start = time.time()
    # myFn(1) # here it runs onthe main thread
    # myFn(2) # here it runs onthe main thread
    # myFn(3) # here it runs onthe main thread
    # myFn(4) # here it runs onthe main thread
    # we can do this on several threads. Any arguments must be in a tuple
    t1 = Thread(target=myFn, args=(1,)) # a one-member tuple
    t2 = Thread(target=myFn, args=(2,)) # a one-member tuple
    t3 = Thread(target=myFn, args=(3,)) # a one-member tuple
    t4 = Thread(target=myFn, args=(4,)) # a one-member tuple
    t5 = Thread(target=myFn, args=(5,)) # a one-member tuple
    
    t1.start() # this will start our thread on a SEPARATE thread to the main thread
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    # we typically get hte threads to join at the earliest oportunity
    t1.join() # invite the new thread to rejoin the main thread
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    end = time.time()
    print(f'Execution took about {end-start} sec')
