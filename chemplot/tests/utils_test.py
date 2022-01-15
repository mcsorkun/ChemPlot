import unittest
from unittest.mock import patch
import pytest

from chemplot import load_data, info_data
from chemplot.parameters import SAMPLE_DATASETS, INFO_DATASET
import pandas as pd
from io import StringIO

class TestUtils(unittest.TestCase):
    
    def test_load_name(self):
        """
        1. Test checks if every load parameter is accepted
        """
        for _, values in SAMPLE_DATASETS.items():
            for name in values:
                data = load_data(name)
                assert isinstance(data, pd.DataFrame)
    
    @patch('sys.stdout', new_callable=StringIO)  
    def test_info_data(self, mock_stdout):
        """
        2. Test checks if the info data functions prints the info correctly
        """
        info_data()
        assert INFO_DATASET in mock_stdout.getvalue()
        
    def test_invalid_name(self):
        """
        3. Test checks when loading a non existing dataset an error is raised
        """
        with self.assertRaises(Exception) as context:
            load_data('Invalid_name')
        self.assertTrue('"Invalid_name" cannot be found in the sample datasets' in str(context.exception))
    
        
if __name__ == '__main__':
    unittest.main()

