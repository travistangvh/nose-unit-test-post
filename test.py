"""
Filename: test.py
"""

import unittest
import pandas as pd

grade_list = [44, 64, -5, 101]

"""
The TestPassed class iterates through the list of grades. 
For each grade, it checks if it is between 0 and 100. 
If not, it fails the test.
"""
class TestPassed(unittest.TestCase):
    def test_grade_between_0_and_100(self):
        # Iterate through grade_list
        for grade in grade_list:

            # subTest divides one unit test into smaller tests.
            with self.subTest(i=grade): 

                # checks if grades is between 0 and 100 (inclusive)
                self.assertEqual(grade >= 0 and grade <= 100,  
                                True) 
 
""" The main function that tells python to run the test"""
if __name__ == '__main__':
    import nose2
    nose2.main()  