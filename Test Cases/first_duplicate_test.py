import unittest
from first_duplicate import *
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(first_duplicate([2, 1, 3, 5, 3, 2]), 4)
# Test cases
