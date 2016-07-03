import unittest
from string_examples import *

class StringExamplesTestCase(unittest.TestCase):

    def test_if_first_non_repeated_character_in_a_string(self):
        self.assertEqual(find_first_non_repeated_character_in_a_string('hhellioo'),'e',msg='Not grabbing correct first non repeating character')
        return True

    def test_if_you_can_reverse_a_string_iteratively(self):
        self.assertEqual(reverse_a_string_iteratively('josh'),'hsoj',msg='unable to reverse string iterativly')
        return True

    def test_if_you_can_reverse_a_string_iteratively_recursively(self):
        self.assertEqual(reverse_a_string_recursively('josh',[]),'hsoj',msg='unable to reverse string recursively')
        return True

    def test_if_2_strings_are_anagrams(self):
        self.assertTrue(determine_if_strings_are_anagrams('josh','hsoj'),msg='unable to determine if strings are anagrams')
        self.assertFalse(determine_if_strings_are_anagrams('josh','catherine'),msg='unable to determine if strings are anagrams')
        return True

    def test_if_string_is_a_palindrome(self):
        self.assertTrue(determine_if_string_is_palindrome('madam'),msg='unable to determine if strings is palendrome')
        self.assertTrue(determine_if_string_is_palindrome('nurses run'),msg='unable to determine if strings is palendrome')
        self.assertFalse(determine_if_string_is_palindrome('josh'),msg='unable to determine if strings are palendrome')
        return True

    def test_if_a_string_is_composed_of_all_unique_characters(self):
        self.assertTrue(determine_if_string_is_all_unique_characters('abcde'),msg='unable to determine if strings are all unique characters')
        self.assertFalse(determine_if_string_is_all_unique_characters('aab'),msg='unable to determine if strings are all unique characters')

        return True

    def test_if_a_string_is_an_int_or_a_double(self):
        self.assertEqual(determine_if_string_is_a_int_or_double('2'),'int',msg='unable to determine if string is int or double')
        self.assertEqual(determine_if_string_is_a_int_or_double('2.5'),'double',msg='unable to determine if string is int or double')
        self.assertEqual(determine_if_string_is_a_int_or_double('hello'),'neither',msg='unable to determine if string is int or double')

        return True



if __name__ == '__main__':
    unittest.main()



