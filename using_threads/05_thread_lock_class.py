import threading
import time
import random

# a global asset
ticketsAvailable = 100

class TicketSeller(threading.Thread):
    '''Each ticket seller instance will attempt to sell tickets'''
    ticketsSold = 0 # how many tickets has this ticket seller sold
    def __init__(self, lock): # make a global thread lock available
        threading.Thread.__init__(self)
        self.__lock = lock
        print('Ticket seller has started sellnig tickets')
    def run(self):
        global ticketsAvailable
        running = True
        while running: # an endless run-loop
            self.randomDelay() # emulate an arbitrary delay
            try:
                self.__lock.acquire()
                if ( ticketsAvailable <=0 ):
                    running=False # this will end our while loop
                else:
                    self.ticketsSold += 1
                    ticketsAvailable -= 1 # this global asset is exclusively locked by this instance
                self.__lock.release()
            except Exception as err:
                print(f'Problem: {err}')
        print(f'Sold {self.ticketsSold}')
    def randomDelay(self):
        time.sleep(random.randint(0,4)/4) # 0, 0.25, 0.5 or 0.75

def main():
    start = time.time()
    lock = threading.Lock() # a lock shared by all ticket sellers
    sellers_l = []
    for i in range(0, 8):
        seller = TicketSeller(lock)
        sellers_l.append(seller)
        seller.start()
    for seller in sellers_l:
        seller()
    end = time.time()
    print(f'Total time {end-start}')

if __name__ == '__main__':
    main()