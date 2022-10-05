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

    # note that the rubric and the instructions do not line
    # up on what test cases to write.  Adding two more 
    # cases to satisfy the assertNotEqual from the rubric
    def test_frenchToEnglish_NotEqual(self):
        self.assertNotEqual(frenchToEnglish('Bojour'),'Hola')
        
    def test_englishToFrench_NotEqual(self):
        self.assertNotEqual(englishToFrench('Goodbye'),'Adios')
  

if __name__ == '__main__':
    unittest.main()

