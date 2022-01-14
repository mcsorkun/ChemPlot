import unittest
from unittest.mock import patch
import pytest

from chemplot import parameters
import pandas as pd 
from io import StringIO

@pytest.mark.usefixtures("logs_plotter", "logs_structural")
class TestUMAP(unittest.TestCase):

    def test_default_structural_n_neighbors(self):
        """
        1. Test checks if default structural n_neighbors is assigned
        """
        self.plotter_structural_LOGS.umap(min_dist=0.9, random_state=None, pca=False)
        self.assertEqual(self.plotter_structural_LOGS.umap_fit.n_neighbors, 
                         parameters.n_neighbors_structural(len(self.plotter_structural_LOGS._Plotter__data)))
    
    def test_default_structural_pca_n_neighbors(self):
        """
        2. Test checks if default structural pca n_neighbors is assigned
        """
        self.plotter_structural_LOGS.umap(min_dist=0.9, random_state=None, pca=True)
        self.assertEqual(self.plotter_structural_LOGS.umap_fit.n_neighbors, 
                         parameters.n_neighbors_structural_pca(len(self.plotter_structural_LOGS._Plotter__data)))
        
    def test_default_tailored_n_neighbors(self):
        """
        3. Test checks if default tailored n_neighbors is assigned
        """
        self.plotter_tailored_LOGS.umap(min_dist=0.9, random_state=None, pca=False)
        self.assertEqual(self.plotter_tailored_LOGS.umap_fit.n_neighbors, 
                         parameters.n_neighbors_tailored(len(self.plotter_tailored_LOGS._Plotter__data)))
        
    def test_n_neighbors(self):
        """
        4. Test checks if n_neighbors is assigned
        """
        self.plotter_tailored_LOGS.umap(n_neighbors=15, random_state=None, min_dist=0.9)
        self.assertEqual(self.plotter_tailored_LOGS.umap_fit.n_neighbors, 15)
        
    def test_default_random_state(self):
        """
        5. Test checks if default random_state is assigned
        """
        self.plotter_tailored_LOGS.umap(n_neighbors=15, min_dist=0.9)
        self.assertIsInstance(self.plotter_tailored_LOGS.umap_fit.random_state, type(None))
        
    def test_random_state(self):
        """
        6. Test checks if random_state is assigned
        """
        self.plotter_tailored_LOGS.umap(n_neighbors=15, random_state=1, min_dist=0.9)
        self.assertEqual(self.plotter_tailored_LOGS.umap_fit.random_state, 1)

    def test_default_structural_min_dist(self):
        """
        7. Test checks if default structural min_dist is assigned
        """
        self.plotter_structural_LOGS.umap(n_neighbors=15, random_state=None, pca=False)
        self.assertEqual(self.plotter_structural_LOGS.umap_fit.min_dist, 
                         parameters.MIN_DIST_STRUCTURAL)
    
    def test_default_structural_pca_min_dist(self):
        """
        8. Test checks if default structural pca min_dist is assigned
        """
        self.plotter_structural_LOGS.umap(n_neighbors=15, random_state=None, pca=True)
        self.assertEqual(self.plotter_structural_LOGS.umap_fit.min_dist, 
                         parameters.MIN_DIST_STRUCTURAL_PCA)
        
    def test_default_tailored_min_dist(self):
        """
        9. Test checks if default tailored min_dist is assigned
        """
        self.plotter_tailored_LOGS.umap(n_neighbors=15, random_state=None, pca=False)
        self.assertEqual(self.plotter_tailored_LOGS.umap_fit.min_dist, 
                         parameters.MIN_DIST_TAILORED)
        
    def test_min_dist(self):
        """
        10. Test checks min_dist is assigned
        """
        self.plotter_structural_LOGS.umap(n_neighbors=15, random_state=None, min_dist=0.5)
        self.assertEqual(self.plotter_structural_LOGS.umap_fit.min_dist, 0.5)
        
    @patch('sys.stdout', new_callable=StringIO)  
    def test_INFO_min_dist_above_1(self, mock_stdout):
        """
        11. Test checks if user is informed about min dist
        """
        self.plotter_tailored_LOGS.umap(n_neighbors=15, random_state=None, min_dist=1)
        self.assertEqual(self.plotter_tailored_LOGS.umap_fit.min_dist, 
                         parameters.MIN_DIST_TAILORED)
        assert str('min_dist must range from 0.0 up to 0.99. Default used.') in mock_stdout.getvalue()
    
    @patch('sys.stdout', new_callable=StringIO)  
    def test_INFO_min_dist_below_0(self, mock_stdout):
        """
        12. Test checks if user is informed about min dist
        """
        self.plotter_tailored_LOGS.umap(n_neighbors=15, random_state=None, min_dist=-1)
        self.assertEqual(self.plotter_tailored_LOGS.umap_fit.min_dist, 
                         parameters.MIN_DIST_TAILORED)
        assert str('min_dist must range from 0.0 up to 0.99. Default used.') in mock_stdout.getvalue()
        
    def test_default_pca(self):
        """
        13. Test checks if default pca is assigned
        """
        self.plotter_tailored_LOGS.umap(n_neighbors=15, random_state=None)
        df_data_tailored = pd.DataFrame(self.plotter_tailored_LOGS._Plotter__data)
        self.assertEqual(len(df_data_tailored.columns), len(self.plotter_tailored_LOGS._Plotter__df_descriptors.columns))

        self.plotter_structural_LOGS.umap(n_neighbors=15, random_state=None)
        df_data_structural = pd.DataFrame(self.plotter_structural_LOGS._Plotter__data)
        self.assertEqual(len(df_data_structural.columns), len(self.plotter_structural_LOGS._Plotter__df_descriptors.columns))
        
    def test_pca(self):
        """
        14. Test checks if pca is assigned
        """
        self.plotter_tailored_LOGS.umap(n_neighbors=15, random_state=None, pca=True)
        df_data_tailored = pd.DataFrame(self.plotter_tailored_LOGS._Plotter__data)
        self.assertEqual(len(df_data_tailored.columns), len(self.plotter_tailored_LOGS._Plotter__df_descriptors.columns))

        self.plotter_structural_LOGS.umap(n_neighbors=15, random_state=None, pca=True)
        df_data_structural = pd.DataFrame(self.plotter_structural_LOGS._Plotter__data)
        self.assertEqual(len(df_data_structural.columns), 10)
        
    def test_plot_title(self):
        """
        15. Test checks if correct title is assigned
        """
        self.plotter_tailored_LOGS.umap()
        self.assertEqual(self.plotter_tailored_LOGS._Plotter__plot_title, "UMAP plot")
    
    def test_return_dataframe(self):
        """
        16. Test checks if the returned object is a dataframe
        """
        result = self.plotter_tailored_LOGS.umap()
        self.assertTrue(isinstance(result, pd.DataFrame))
        
    def test_shape_target(self):
        """
        17. Test checks if dataframe has correct shape with target
        """
        result = self.plotter_tailored_LOGS.umap()
        self.assertEqual(result.shape[1], 3)
        
    def test_shape_no_target(self):
        """
        18. Test checks if dataframe has correct shape without target
        """
        result = self.plotter_no_target_LOGS.umap()
        self.assertEqual(result.shape[1], 2)
        
    def test_column_labels(self):
        """
        19. Test checks if correct column lables are assigned
        """
        result = self.plotter_tailored_LOGS.umap()
        column_one = "UMAP-1"
        column_two = "UMAP-2"
        column_three = "target"
        self.assertEqual(result.columns[0], column_one)
        self.assertEqual(result.columns[1], column_two)
        self.assertEqual(result.columns[2], column_three)
        
    def test_correct_targets(self):
        """
        20. Test checks if the correct targets are assigned to the returned DataFrame
        """
        result = self.plotter_tailored_LOGS.umap()
        self.assertEqual(list.sort(list(result['target'])), 
                         list.sort(self.plotter_tailored_LOGS._Plotter__target))
    
if __name__ == '__main__':
    unittest.main()
    
