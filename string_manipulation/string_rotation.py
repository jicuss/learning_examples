'''
Original Source: Cracking the Coding Interview
Question: Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call
eg. waterbottle is a rotation of erbottlewat

'''

import unittest
import pdb

def isSubstring(s1,s2):
    if s1 in findRotations(s2):
        return True

def findRotations(string):
    '''  return all possible rotations '''
    rotations = []
    l = len(string)
    for i in range(0,l + 1):
        beginning = string[i:l + 1] # grabs the current index to the end of the string
        ending = string[0:i]
        rotations.append(beginning + ending)

    return rotations

class StringRotationTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isSubstring(self):
        self.assertTrue(isSubstring('waterbottle','erbottlewat'))

    def test_findRotations(self):
        self.assertIn('erbottlewat',findRotations('waterbottle'))


if __name__ == '__main__':
    unittest.main()