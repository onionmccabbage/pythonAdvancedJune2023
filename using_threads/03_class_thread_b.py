from threading import Thread
import random
import time

# this class implicitly inherists from object
class MyClass:
    def __call__(self, n):
        for i in range(1, 50):
            print(f'{n} is sleeping')
            time.sleep(random.random()*0.1)

def main():
    start = time.time()
    c1 = MyClass()
    thread_l = []
    for i in range(8):
        thread_l.append( Thread(target=c1, args=(i,)) )
    for thread in thread_l:
        thread.start() # we must start all the threads before we join any thread
    for thread in thread_l:
        thread.join()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Execution took {end-start} sec')