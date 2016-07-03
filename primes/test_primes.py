import unittest
from primes import is_prime,return_primes_through_n

class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))

    def test_is_four_non_prime(self):
        """Is four correctly determined not to be prime?"""
        self.assertFalse(is_prime(4), msg='Four is not prime!')

    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        self.assertFalse(is_prime(0))

    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index),msg='{} should not be determined to be prime'.format(index))

class PrimesArrayTestCase(unittest.TestCase):
    """Tests for primes.py."""

    def test_prime_array_for_four(self):
        '''  should return [3] '''
        self.assertEqual(return_primes_through_n(4),[3], msg='For the range of four its not returning [3]')

if __name__ == '__main__':
    unittest.main()