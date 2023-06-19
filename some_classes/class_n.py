
class Several:
    __slots__ = ('x', 'y', 'z') # declare a tuple of permitted slots
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

if __name__ == '__main__':
    s1 = Several(4,3,2)
    print( Several.__dict__ )
    print( Several.__slots__ )
    
    # since we declared 'slots' we cannot add arbitrary properties
    s1.p = 'nope'
