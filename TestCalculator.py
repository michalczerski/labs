import unittest

class MyTest(unittest.TestCase):
    def test_is_equal(self):
        self.assertEqual(4, 4)
    def test_is_not_equal(self):
        self.assertNotEqual(4,4)
