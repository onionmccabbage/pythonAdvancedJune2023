# classes can encapsulate features and functions
# a class to define a shape

# follow a common style - choose to use brackets (or not) as a consistent style feature
class Shape(): # every class inherits from 'object'
    '''A shape with num sides and colour'''
    def __init__(self, num_sides, colour='red'): # every method of a class reqires 'self'
        # we use name-mangling to 'hide' properties of the class
        # optionally we can call our setter method in the init method
        # self.__num_sides = num_sides # careful - this will not validate
        # or 
        self.sides  = num_sides # double-underscore makes this hidden
        self.colour = colour # mangle the colour name
    # we often use getter and setter methods (and decorators)
    @property # this makes the next fubnvction into a 'getter'
    def sides(self):
        return self.__num_sides
    @sides.setter  # this makes the next function into a 'setter'
    def sides(self, num_sides):
        # here we can validate the num_sides
        if type(num_sides) == int and num_sides > 0:
            self.__num_sides = num_sides
        else:
            raise Exception('number of sides must be a positive integer')
    @property
    def colour(self):
        return self.__colour
    # @property get/set methods for colour
    @colour.setter
    def colour(self, colour):
        # validate as a non-empty string
        if type(colour) == str and len(colour)>0:
            self.__colour = colour
        else:
            raise Exception('Colour must be a non-empty string')
    # we can write a __str__ method for peinting this class
    def __str__(self): # here we are overriding the build-in __str__ method
        '''this function will be called whenever this class is printed'''
        return f'Shape has {self.sides} sides and is {self.colour}'
    # we can also override the built-in method __repr__
    # __repr__ is used in immediate mode
    def __repr__(self): # here we are overriding the build-in __repr__ method
        '''this function will be called whenever this class is output in immediate mode'''
        return f'Shape has {self.sides} sides and is {self.colour}'

if __name__ == '__main__':
    # we can make instances of our class
    s1 = Shape(3)
    # all classes will have intrinsic properties
    print( Shape.__name__ )
    # danger - every property of a class is accessible outside the class
    s1.__num_sides = False # this is NOT the mangled property it is just a abstract property
    print( s1.__num_sides, s1.sides, s1.colour ) # .sides and .colour will call the getter method

    s2 = Shape(6, 'green')
    print(f'This shape has {s2.sides} sides and is {s2.colour}')

    print(s2) # any print call that prints just the class instance will use the __str__ method
    print(s2.__repr__()) # we can call it, but its purpose is for immediate mode python
    # s3 = Shape(4, True) # throws an exception


