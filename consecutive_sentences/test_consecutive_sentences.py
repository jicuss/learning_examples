from consecutive_sentences import *
import unittest
import pdb

class TextCleanupTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_multiple_spaces_between_sentences(self):
        self.assertEqual(cleanup_text('This is a sentence.    This is another.'),'This is a sentence. This is another.',msg='needs to be able to remove multiple spaces between sentences')

    def test_newlines_tabs(self):
        self.assertEqual(cleanup_text('This is a sentence.\n\t    This\tis another.'),'This is a sentence. This is another.',msg='needs to be able to remove multiple spaces between sentences')

class SentenceCountTest(unittest.TestCase):
    def setUp(self):
        self.sc = SentenceCount()
        pass

    def tearDown(self):
        pass

    def test_simple(self):
        self.sc.text = '''Black is white.  Day is night.  Understanding is ignorance.
                     Truth is fiction.  Safety is danger.'''
        self.assertEqual(self.sc.find_sentences(15,16),['Black is white.'])
        self.assertEqual(self.sc.find_sentences(17,18),['Truth is fiction.','Safety is danger.'])
        self.assertEqual(self.sc.find_sentences(30,37),['Truth is fiction. Safety is danger.'])
        return True


if __name__ == '__main__':
    unittest.main()