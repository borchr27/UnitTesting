import unittest
from main import Interest

class TestInterest(unittest.TestCase):
    def test_simple_interest_values(self):
        # Test all arguements of the function to determine that if rouge type is entered that it is caught
        self.assertRaises(TypeError, Interest().simple_interest, 'init amt', 1, 1)
        self.assertRaises(TypeError, Interest().simple_interest, (True, 1, 1))
        self.assertRaises(TypeError, Interest().simple_interest, (1+3j, 1, 1))

        self.assertRaises(TypeError, Interest().simple_interest, (100, 'rate', 1))
        self.assertRaises(TypeError, Interest().simple_interest, (100, True, 1))
        self.assertRaises(TypeError, Interest().simple_interest, (100, 1+3j, 1))

        self.assertRaises(TypeError, Interest().simple_interest, (100, 1, 'time'))
        self.assertRaises(TypeError, Interest().simple_interest, (100, 1, True))
        self.assertRaises(TypeError, Interest().simple_interest, (100, 1, 1+3j))

    def test_simple_interest_types(self):
        pass
