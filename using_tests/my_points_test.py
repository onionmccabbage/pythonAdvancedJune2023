import unittest
from my_points import Point

# we use the word 'test' in our test class
class testPoint(unittest.TestCase):
    # set up before each test
    def setUp(self):
        ''' this will run before each test'''
        self.point = Point(3, 5)
    # declare individual unit tests
    def testMoveBy_A(self):
        self.point.moveBy(5, 2)
        self.assertEqual(self.point.x, 8)
        self.assertEqual(self.point.y, 7)
    def testMoveBy_B(self):
        self.point.moveBy(-5, -2)
        self.assertEqual( self.point.display(), (-2, 3) )
    def testNonNumeric(self):
        with self.assertRaises(TypeError):
            Point('3', 4)
        with self.assertRaises(TypeError):
            self.point.y = True
    def testHypot(self):
        self.point.moveBy(0, -1)
        r = self.point.hypot()
        self.assertAlmostEqual(r, 5.00, places=2)
    def pos_neg_hypot(self):
        self.p_pos = Point(3,4)
        self.p_neg = Point(-3,-4)
        self.assertAlmostEqual( self.p_pos.hypot(), self.p_neg.hypot() )

if __name__ == '__main__':
    unittest.main() # this will run all our tests