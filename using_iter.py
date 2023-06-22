# we can make our own classes iterable (so they can be looped over)
class ShowEvenNums():
    '''This iterable class will let us isterate over the even numbers from zero'''
    def __init__(self, limit):
        self.limit = limit
        self.val = 0
    def __iter__(self):
        '''to make a class iterable, simply override hte __iter__ method'''
        return self
    def __next__(self):
        if self.val > self.limit:
            raise StopIteration # we have exhausted ou iterator
        else:
            rval = self.val
            self.val += 2
            return rval

if __name__ == '__main__':
    e = ShowEvenNums(6)
    print(e.__next__()) # 0
    print(e.__next__()) # 2
    for i in ShowEvenNums(12):
        print(i)