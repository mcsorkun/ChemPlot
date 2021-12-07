import unittest

from chemplot import Plotter
import pandas as pd 
import os

class TestPCA(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        file_LOGS = os.path.join('tests', 'test_data', 'R_1291_LOGS.csv')
        cls.data_LOGS = pd.read_csv(file_LOGS) 
        cls.plotter_target_LOGS = Plotter.from_smiles(cls.data_LOGS["smiles"], target=cls.data_LOGS["target"], target_type="R")
        cls.plotter_no_target_LOGS = Plotter.from_smiles(cls.data_LOGS["smiles"], target_type="R", sim_type="structural")
        
    def test_plot_title(self):
        """
        1. Test checks if correct title is assigned
        """
        self.plotter_target_LOGS.pca()
        self.assertEqual(self.plotter_target_LOGS._Plotter__plot_title, "PCA plot")
    
    def test_return_dataframe(self):
        """
        2. Test checks if the returned object is a dataframe
        """
        result = self.plotter_target_LOGS.pca()
        self.assertTrue(isinstance(result, pd.DataFrame))
        
    def test_shape_target(self):
        """
        3. Test checks if dataframe has correct shape with target
        """
        result = self.plotter_target_LOGS.pca()
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
        result = self.plotter_target_LOGS.pca()
        coverage_components = self.plotter_target_LOGS.pca_fit.explained_variance_ratio_
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
        result = self.plotter_target_LOGS.pca()
        self.assertEqual(list.sort(list(result['target'])), 
                         list.sort(self.plotter_target_LOGS._Plotter__target))

if __name__ == '__main__':
    unittest.main()