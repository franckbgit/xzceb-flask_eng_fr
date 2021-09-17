import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(''), '') # test null input
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test translation of Hello to French


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(''), '') # test null input
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test translation of Bonjour to English

unittest.main()