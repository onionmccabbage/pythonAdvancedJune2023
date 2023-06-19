# we can import from other modules
from class_a import Shape

# Rules for name mangling
# begin with double underscore
# DO NOT use trailing double-underscore
# typically use letters and numbers



# we can only inherist from ONE parent class
class Figure(Shape): # this clas inherits everything from Shape
    def __init__(self, n, c, size):
        super().__init__(n, c) # call the __init__ of the parent class
        self.size = size # this will call the setter method
    @property
    def size(self):
        '''this is the getter method for size'''
        return self.__size # return the name-mangled property (not directly accessible)
    @size.setter
    def size(self, size):
        '''this is the setter method for size'''
        # validate that size is a positive number (float or int)
        if (isinstance(size, int) or type(size)==float) and size >0:
            # all good - set the mangled property
            self.__size = size
            # careful - isnumeric checks is a STRING looks like a number...
        else:
            self.__size = 10 # sensible default
    # we could override __str__ to include the size


if __name__ == '__main__':
    hexagon = Shape(6, 'blue')
    print(hexagon)

    pentagon = Figure(5, 'purple', 12.12)
    print(pentagon)