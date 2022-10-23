"""
Filename: test_param.py
"""
import unittest
from nose2.tools import params
import pandas as pd
from parameterized import parameterized

def compute(a, b):
    return (a + b) / (a * b)

def load_test_cases():
    """ Create test cases in the format of a dataframe. """
    df = pd.DataFrame.from_dict({
                 # Each row contains 
                 # [name                , a     , b     , expected_output   , expected_error    ]
         'test_1': ['negative_int_test' , -2    , 2     , 0                 , None              ], 
         'test_2': ['positive_int_test' , 2     , 2     , 1                 , None              ],
         'test_3': ['decimal_test'      , .5    , .4    , 4.5               , None              ],
         'test_4': ['none_type_test'    , None  , 2     , None              , TypeError         ],
         'test_5': ['string_type_test'  , '10'  , 1     , None              , TypeError         ],
         'test_6': ['zero_division_test', 0     , 2     , None              , ZeroDivisionError ]
         },
        orient='index'
    )

    df.columns = ['name','a','b','expected_output', 'expected_error']
    
    return list(df.itertuples(index=False, name=None)) # return dataframe as a list of tuples.
        
class TestSuite(unittest.TestCase):
    @parameterized.expand(
        #each tuple contains (name, a, b, expected_output, expected_error)
        load_test_cases()
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

if __name__ == '__main__':
    import nose2
    nose2.main()  