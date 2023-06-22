from threading import Thread
import random
import time

class MyClass(Thread):
    ''' this class inherits from thread'''
    def __init__(self, n):
        # super().__init__(self)
        Thread.__init__(self) # alternative syntax
        self.n = n
    # in order to be runnable we override the 'run' method
    def run(self):
        '''When this (Thread) class is invoked, this method will execute'''
        for i in range(1, 50):
            print(f'{self.n} is sleeping')
            time.sleep(random.random()*0.1)

def main():
    start = time.time()
    thread_l = []
    for i in range(8):
        thread_l.append( MyClass(i) )
    for thread in thread_l:
        thread.start() # we must start all the threads before we join any thread
    for thread in thread_l:
        thread.join()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Execution took {end-start} sec')