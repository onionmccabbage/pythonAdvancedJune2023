# genertors are built in to Python
# use a generator whenever we need a lot of values  without using lots of memory
my_num_g = (n for n in range(-99, 100))
# my_num_l = [n for n in range(-99, 100)] # careful - this list persists in memory
# we have a generator - the values do NOT persist in memory
print(my_num_g)
# we can apply logic as we generate the values
odd_g = (n for n in range(-99, 100) if n%2==1)

# we can write a custom generator
def my_gen(first=0, last=10*100, step=1):
    '''generate values and yield the results'''
    number = first
    while number<last:
        yield number*number # the yield statement makes this function into a generator
        number += step

if __name__ == '__main__':
    g = my_gen() # we need an instance of our generator
    print( g.__next__() ) # 0
    print( g.__next__() ) # 1
    print( g.__next__() ) # 4
    print( g.__next__() ) # 9
    # we could iterate over every value from the generator
    # ...but when all the values have been used, the generator is exhausted