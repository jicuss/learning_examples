'''
Objective: Write a program that prints the numbers from 1 to 100.
        For multiples of three print Fizz instead of the number and for the multiples of five print Buzz.
        For numbers which are multiples of both three and five print FizzBuzz.
        Print a new line after each string or number.
'''

import unittest

class FizBuzz:
    def response(self,number):
        ''' use the modulo operator to look at the remainder of the integer when divided by 5 & 3.
        If the remainder is 0, output a string appropriate otherwise return the integer '''
        if number%5 == 0 and number%3 == 0:
            return 'fizzbuzz'
        elif number%5 == 0:
            return 'buzz'
        elif number%3 == 0:
            return 'fizz'
        else:
            return number

class FizbuzzTests(unittest.TestCase):
    def setUp(self):
        self.fizbuzz = FizBuzz()
        pass

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

    def test_integer(self):
        self.assertEqual(self.fizbuzz.response(1),1)
        return True

    def test_fizz(self):
        self.assertEqual(self.fizbuzz.response(3),'fizz')
        return True

    def test_buzz(self):
        self.assertEqual(self.fizbuzz.response(5),'buzz')
        return True

    def test_fizzbuzz(self):
        self.assertEqual(self.fizbuzz.response(15),'fizzbuzz')
        return True

if __name__ == '__main__':
    unittest.main()
    fz = FizBuzz()
    for i in range(1,101):
        print fz.response(i)


