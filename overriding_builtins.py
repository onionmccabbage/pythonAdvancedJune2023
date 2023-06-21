
class Word():
    '''This class overrides the equality operator to ignore case'''
    def __init__(self, text):
        self.text = text # we could use property get/set methods
    def __eq__(self, other):
        '''this will override the normal equality operator'''
        answer = self.text.lower() == other.text.lower()
        return answer

# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# other 'magic methods'
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object





if __name__ == '__main__':
    # normal comparison operator
    w1 = 'Hello'
    w2 = 'hello'
    print( w1 == w2 ) # False
    # our custom 'Word' class
    word1 = Word('Hello')
    word2 = Word('hello')
    print( word1 == word2 ) # True

    # python 'multiply' for strings
    s = 'doobie do '
    print( s*3 )