class Point():
    '''define a point in 2-d space represented by x and y
    Also enable moveBy to change x and y'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x) in (int, float):
            self.__x = new_x
        else:
            raise TypeError
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, new_y):
        if type(new_y) in (int, float):
            self.__y = new_y
        else:
            raise TypeError
    def moveBy(self, dx, dy):
        self.x += dx
        self.y += dy
    def display(self):
        return (self.x, self.y)
    def hypot(self):
        ''' derive the hypotenuse from x and y'''
        h = (self.x**2 + self.y**2)**0.5 # NB remember these will call the getter methods
        return h
    
if __name__ == '__main__':
    p1 = Point(5, 7)
    print( p1.display() ) # (5, 7)
    # p1.moveBy(-2, -3)
    print( p1.display() ) # (3, 4)
    print( p1.hypot() ) # 5.0
    # p2 = Point(True, False)