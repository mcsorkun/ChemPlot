import unittest
import pytest

import pandas as pd 

@pytest.mark.usefixtures("logs_plotter")
class TestPCA(unittest.TestCase):

    def test_plot_title(self):
        """
        1. Test checks if correct title is assigned
        """
        self.plotter_tailored_LOGS.pca()
        self.assertEqual(self.plotter_tailored_LOGS._Plotter__plot_title, "PCA plot")
    
    def test_return_dataframe(self):
        """
        2. Test checks if the returned object is a dataframe
        """
        result = self.plotter_tailored_LOGS.pca()
        self.assertTrue(isinstance(result, pd.DataFrame))
        
    def test_shape_target(self):
        """
        3. Test checks if dataframe has correct shape with target
        """
        result = self.plotter_tailored_LOGS.pca()
        self.assertEqual(result.shape[1], 3)
        
    def test_shape_no_target(self):
        """
        4. Test checks if dataframe has correct shape without target
        """
        result = self.plotter_no_target_LOGS.pca()
        self.assertEqual(result.shape[1], 2)
        
    def test_column_labels(self):
        """
        5. Test checks if correct column lables are assigned
        """
        result = self.plotter_tailored_LOGS.pca()
        coverage_components = self.plotter_tailored_LOGS.pca_fit.explained_variance_ratio_
        column_one = "PC-1 (" + "{:.0%}".format(coverage_components[0]) + ")"
        column_two = "PC-2 (" + "{:.0%}".format(coverage_components[1]) + ")"
        column_three = "target"
        self.assertEqual(result.columns[0], column_one)
        self.assertEqual(result.columns[1], column_two)
        self.assertEqual(result.columns[2], column_three)
        
    def test_correct_targets(self):
        """
        6. Test checks if the correct targets are assigned to the returned DataFrame
        """
        result = self.plotter_tailored_LOGS.pca()
        self.assertEqual(list.sort(list(result['target'])), 
                         list.sort(self.plotter_tailored_LOGS._Plotter__target))

if __name__ == '__main__':
    unittest.main()