"""
Filename: test_param_with_error.py
"""
import unittest
from nose2.tools import params
import pandas as pd
from parameterized import parameterized

def compute(a, b):
    return (a + b) / (a * b)

"""
The TestSuite class checks treats each test case in the 
decorator @params as an individual test case.  
For test case, it checks if the actual output matches the expected output.
If not, the test fails.
"""
class TestSuite(unittest.TestCase):
    @parameterized.expand(
        [
        #each tuple contains (name, a, b, expected_output, expected_error)
        ("test_divisionbyzero", 0,  0,  None, ZeroDivisionError),                              
        ("test_int",            1,  1,  2),
        ("test_float",          1., 1., 2.)
        ]
    )
    def test_compute(self, name, a, b, expected_output, expected_error=None):
        # If no error is expected from the test case, 
        # check if the actual output matches the expected output
        if expected_error is None:
            assert compute(a, b) == expected_output
        
        # If an error is expected from the test case,
        # check if the actual error matches the expected error
        else:
            with self.assertRaises(expected_error):
                compute(a, b)

 
""" The main function that tells python to run the test"""
if __name__ == '__main__':
    import nose2
    nose2.main()  