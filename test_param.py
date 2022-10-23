"""
Filename: test_param.py
"""
import unittest
from nose2.tools import params
import pandas as pd
from parameterized import parameterized

def compute(a, b):
    return (a + b) / (a * b)

class TestSuite(unittest.TestCase):
    @parameterized.expand(
        [
        #each tuple contains (name, name, a, b, expected_output)
        ("test_int", 1, 1, 2), 
        ("test_float", 1., 1., 2.)
        ]
    )
    def test_compute(self, name, a, b, expected_output):
        assert compute(a, b) == expected_output

if __name__ == '__main__':
    import nose2
    nose2.main()  