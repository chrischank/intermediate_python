import unittest

from divisable import divisable_by

class DivisableTestCase(unittest.TestCase):
    def test_divisable_by(self):
        self.assertTrue(divisable_by(10, 3))
        self.assertFalse(divisable_by(10, 2))

if __name__ == "__main__":
    unittest.main()
