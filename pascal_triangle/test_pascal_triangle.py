import unittest
from pascal_triangle import *

class PascalTriangleTestCase(unittest.TestCase):
    def test_pascal_triangle_row(self):
        self.assertEquals(pascal_triangle_row([1,3,3,1]),[1,4,6,4,1],'Triangle array row malformed')
        return True

    def test_triangle_depth_five(self):
        triangle_array = []
        triangle_array.append([1])
        triangle_array.append([1,1])
        triangle_array.append([1,2,1])
        triangle_array.append([1,3,3,1])
        triangle_array.append([1,4,6,4,1])
        triangle_array.append([1,5,10,10,5,1])

        self.assertEquals(pascal_triangle_recursive([],5),triangle_array,'Triangle array malformed for depth 5')
        return True

if __name__ == '__main__':
    unittest.main()


