import unittest
from unittest.mock import patch
import pytest

from chemplot import Plotter
import pandas as pd
from io import StringIO
    
@pytest.mark.usefixtures("logs_plotter")
class TestCluster(unittest.TestCase):
    
    def test_default_n_cluster(self):
        """
        1. Test checks if default n_cluster is assigned
        """
        self.plotter_tailored_LOGS.pca()
        result = self.plotter_tailored_LOGS.cluster()
        assert 'clusters' in result.columns
        assert len(set(result['clusters'])) == 5
        
    def test_return_dataframe(self):
        """
        2. Test checks if the returned object is a dataframe
        """
        result = self.plotter_tailored_LOGS.cluster()
        self.assertTrue(isinstance(result, pd.DataFrame))
        
    def test_n_cluster(self):
        """
        3. Test checks if default n_cluster is assigned
        """
        self.plotter_tailored_LOGS.pca()
        result = self.plotter_tailored_LOGS.cluster(n_clusters=3)
        assert len(set(result['clusters'])) == 3
        result = self.plotter_tailored_LOGS.cluster(n_clusters=8)
        assert len(set(result['clusters'])) == 8
    
    
    @patch('sys.stdout', new_callable=StringIO)  
    def test_error_no_dim_red(self, mock_stdout):
        """
        4. Test checks if user is informed clusters cannot be created without reducing the dimensions first
        """
        result = self.plotter_no_target_LOGS.cluster()
        assert result is None
        assert 'Reduce the dimensions of your molecules before clustering.' in mock_stdout.getvalue()
        
        
if __name__ == '__main__':
    unittest.main()

