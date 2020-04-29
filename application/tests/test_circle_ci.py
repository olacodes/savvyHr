import unittest

class CircleCiTest(unittest.TestCase):
    def test_circleci(self):
        self.assertEqual(2 + 2, 4)
        
    def test(self):
        self.assertTrue(True)


if __name__ == '__main__': 
    unittest.main() 
