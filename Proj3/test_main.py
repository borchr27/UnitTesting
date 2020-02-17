import unittest
from main import Interest

class TestInterest(unittest.TestCase):
    def test_simple_interest_type_error(self):
        # Test all arguements of the function to determine that if rouge type is entered that it is caught
        self.assertRaises(TypeError, Interest().simple_interest, 'init amt', 1, 1)
        self.assertRaises(TypeError, Interest().simple_interest, True, .5, 1)
        self.assertRaises(TypeError, Interest().simple_interest, 1+3j, .5, 1)

        self.assertRaises(TypeError, Interest().simple_interest, 100, 'rate', 1)
        self.assertRaises(TypeError, Interest().simple_interest, 100, True, 1)
        self.assertRaises(TypeError, Interest().simple_interest, 100, 1+3j, 1)

        self.assertRaises(TypeError, Interest().simple_interest, 100, .5, 'time')
        self.assertRaises(TypeError, Interest().simple_interest, 100, .5, True)
        self.assertRaises(TypeError, Interest().simple_interest, 100, .5, 1+3j)

    def test_simple_interest_value_error(self):
        # Test all arguments of the function to ensure that negatives, non decimals, and negative time durations dont work
        self.assertRaises(ValueError, Interest().simple_interest, -100, .5, 1)
        self.assertRaises(ValueError, Interest().simple_interest, 100, -.5, 1)
        self.assertRaises(ValueError, Interest().simple_interest, 100, .5, -1)
        self.assertRaises(ValueError, Interest().simple_interest, 100, 1.5, -1)
    
    def test_function_output_correctness(self):
        # Test and make sure the functions are outputting the expected values
        self.assertAlmostEqual(Interest().simple_interest(100, .5, 1), 100 * (.5 * 1 + 1))
        self.assertAlmostEqual(Interest().simple_interest(0, .5, 1), 0 * (.5 * 1 + 1))
        self.assertAlmostEqual(Interest().simple_interest(17659, .03, 10), 17659 * (.03 * 10 + 1))

        
