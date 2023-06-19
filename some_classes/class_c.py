
# there is an abstract-base-class (abc) library in Python
from abc import ABCMeta

# but this is not rigorously enforced
class Abstract(metaclass=ABCMeta):
    '''This is the most generic class possible'''
    
class Basic(Abstract):
    def __init__(self, x, y):
        self.x = x # we are not obliged to use get/set methods
        self.y = y # careful -these proiperties are directly mutable outside the class

class Concrete(Basic):
    '''this is a concrete implementation of abstract classes'''
    count = 0 # here is a class property
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        Concrete.count += 1 # incrememnt the class property
    @classmethod # the following method belongs to the class
    def howMany(cls): # NB class methods do NOT take self
        return f'There are {cls.count} instances of this class'

if __name__ == '__main__':
    s1 = Concrete(1,2,3)
    s2 = Concrete('a','b','c')
    s3 = Concrete([], (), {})
    print( Concrete.howMany() ) # we can call class methods on the class or on an instance

    # we can explore intrinsics...
    print( f'Class name is {Concrete.__name__}' )
    print( f'Class docstring is {Concrete.__doc__}' )
    print( f'Class dictionary is {Concrete.__dict__}' )
    print( f'Class bases are {Concrete.__bases__} and {Abstract.__bases__}' )







