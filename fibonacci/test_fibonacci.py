import unittest
from fibonacci import *

class FibonacciTestCase(unittest.TestCase):

    def test_fib_sequence_five(self):
        ''' test that the fib class returns all correct elements through n '''
        self.assertEquals(fibonacci_loop(5),[0, 1, 1, 2, 3, 5],'Not returning the correct array for 5')
        return True

    def test_fib_sequence_twentyone(self):
        ''' test that the fib class returns all correct elements through n '''
        self.assertEquals(fibonacci_loop(21),[0, 1, 1, 2, 3, 5, 8, 13, 21],'Not returning the correct array for 21')
        return True

class FibonacciRecurseTestCase(unittest.TestCase):

    def test_fib_sequence_five(self):
        results = []
        ''' test that the fib class returns all correct elements through n '''
        self.assertEquals(fibonacci_recurse(5,[]),[0, 1, 1, 2, 3, 5],'Not returning the correct array for 5')
        return True

    def test_fib_sequence_twentyone(self):
        ''' test that the fib class returns all correct elements through n '''
        self.assertEquals(fibonacci_recurse(21,[]),[0, 1, 1, 2, 3, 5, 8, 13, 21],'Not returning the correct array for 21')
        return True

if __name__ == '__main__':
    unittest.main()
