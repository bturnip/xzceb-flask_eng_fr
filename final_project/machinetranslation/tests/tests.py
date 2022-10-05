import unittest
import translator

from translator import englishToFrench, frenchToEnglish

class TestMyModule(unittest.TestCase):

    def test_englishToFrench_01(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test_frenchToEnglish_01(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

    def test_englishToFrench_02(self):
        self.assertIsNone(englishToFrench(None))

    def test_frenchToEnglish_02(self):
        self.assertIsNone(frenchToEnglish(None))

if __name__ == '__main__':
    unittest.main()

