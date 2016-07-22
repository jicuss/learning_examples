'''
Original Source of Problem: Cracking the Coding Interview Pg. 91

There are three types of edits that can be performed on strings:
    * insert a character
    * remove a character
    * replace a character.

Given two strings, write a function to check if they are one edit or zero edits away)

Examples:
    pale, ple -> true
    pales, pale -> true
    pale, bale -> true
    pale, bake -> false

'''


import unittest
import pdb

def isOneAway(s1,s2):
    ''' returns true if the strings are one edit away from each other'''
    array_1 = popStringCharacters(s1)
    array_2 = popStringCharacters(s2)
    if len(arrayIntersect(array_1,array_2)) > 0:
        return True

def popStringCharacters(string):
    ''' return all possible combinations of removing a single character from the string, including none '''
    options = []
    options.append(string)
    for i in range(0,len(string)):
        char_array = list(string)
        char_array.pop(i)
        options.append(''.join(char_array))
    return options

def arrayIntersect(array_1,array_2):
    ''' return all intersections of the two arrays '''
    results = []
    for i in array_1:
        if i in array_2:
            results.append(i)
    return results

class OneAwayTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_true(self):
        self.assertTrue(isOneAway('pale','ple'))
        self.assertTrue(isOneAway('pales','pale'))
        self.assertTrue(isOneAway('pale','bale'))

    def test_false(self):
        self.assertFalse(isOneAway('pale','bake'))


if __name__ == '__main__':
    unittest.main()

