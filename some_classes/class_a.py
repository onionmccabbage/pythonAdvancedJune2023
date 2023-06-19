# classes can encapsulate features and functions
# a class to define a shape

# follow a common style - choose to use brackets (or not) as a consistent style feature
class Shape(): # every class inherits from 'object'
    '''A shape with num sides and colour'''
    def __init__(self, num_sides, colour=''): # every method of a class reqires 'self'
        self.num_sides = num_sides
        self.colour    = colour
    # we often use getter and setter methods
    def sides(self):
        return self.num_sides
    def sides(self, num_sides):
        # here we can validate the num_sides
        if type(num_sides) == int and num_sides > 0:
            self.num_sides = num_sides
        else:
            raise Exception('number of sides must be a positive integer')

if __name__ == '__main__':
    # we can make instances of our class
    s1 = Shape(3)
    # all classes will have intrinsic properties
    print( Shape.__name__ )
    # danger - every property of a class is accessible outside the class
    s1.num_sides = False
    print( s1.num_sides, s1.colour )

