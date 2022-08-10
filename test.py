import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(3,5),8)

    def test_pow(self):
         self.assertEqual(main.pow(2,4),16)

if __name__ == '__main__':
    unittest.main()
    
