import unittest
from unittest.mock import patch
import pytest

from chemplot import parameters
import pandas as pd 
from io import StringIO

@pytest.mark.usefixtures("logs_plotter", "logs_structural")
class TesttSNE(unittest.TestCase):

    def test_default_structural_perplexity(self):
        """
        1. Test checks if default structural perplexity is assigned
        """
        self.plotter_structural_LOGS.tsne(random_state=None, pca=False)
        self.assertEqual(self.plotter_structural_LOGS.tsne_fit.get_params(deep=True)['perplexity'], 
                         parameters.perplexity_structural(len(self.plotter_structural_LOGS._Plotter__data)))
    
    def test_default_structural_pca_perplexity(self):
        """
        2. Test checks if default structural pca perplexity is assigned
        """
        self.plotter_structural_LOGS.tsne(random_state=None, pca=True)
        self.assertEqual(self.plotter_structural_LOGS.tsne_fit.get_params(deep=True)['perplexity'], 
                         parameters.perplexity_structural_pca(len(self.plotter_structural_LOGS._Plotter__data)))
        
    def test_default_tailored_perplexity(self):
        """
        3. Test checks if default tailored perplexity is assigned
        """
        self.plotter_tailored_LOGS.tsne(random_state=None, pca=False)
        self.assertEqual(self.plotter_tailored_LOGS.tsne_fit.get_params(deep=True)['perplexity'], 
                         parameters.perplexity_tailored(len(self.plotter_tailored_LOGS._Plotter__data)))
    
    @patch('sys.stdout', new_callable=StringIO)  
    def test_INFO_perplexity_below_5(self, mock_stdout):
        """
        4. Test checks if user is informed about robust perplexities
        """
        self.plotter_tailored_LOGS.tsne(perplexity=2, random_state=None, pca=False)
        assert str('Robust results are obtained for values of perplexity between 5 and 50') in mock_stdout.getvalue()
    
    @patch('sys.stdout', new_callable=StringIO)  
    def test_INFO_perplexity_above_50(self, mock_stdout):
        """
        5. Test checks if user is informed about robust perplexities
        """
        self.plotter_tailored_LOGS.tsne(perplexity=60, random_state=None, pca=False)
        assert str('Robust results are obtained for values of perplexity between 5 and 50') in mock_stdout.getvalue()
        
    def test_perplexity_assigned(self):
        """
        6. Test checks if perplexity is assigned
        """
        self.plotter_tailored_LOGS.tsne(perplexity=30, random_state=None, pca=False)
        self.assertEqual(self.plotter_tailored_LOGS.tsne_fit.get_params(deep=True)['perplexity'], 30)
        
    def test_default_random_state(self):
        """
        7. Test checks if default random_state is assigned
        """
        self.plotter_tailored_LOGS.tsne(perplexity=30, pca=False)
        self.assertIsInstance(self.plotter_tailored_LOGS.tsne_fit.get_params(deep=True)['random_state'], type(None))
        
    def test_random_state(self):
        """
        8. Test checks if random_state is assigned
        """
        self.plotter_tailored_LOGS.tsne(perplexity=30, random_state=1, pca=False)
        self.assertEqual(self.plotter_tailored_LOGS.tsne_fit.get_params(deep=True)['random_state'], 1)
        
    def test_default_pca(self):
        """
        9. Test checks if default pca is assigned
        """
        self.plotter_tailored_LOGS.tsne(perplexity=30, random_state=None)
        df_data_tailored = pd.DataFrame(self.plotter_tailored_LOGS._Plotter__data)
        self.assertEqual(len(df_data_tailored.columns), len(self.plotter_tailored_LOGS._Plotter__df_descriptors.columns))

        self.plotter_structural_LOGS.tsne(perplexity=30, random_state=None)
        df_data_structural = pd.DataFrame(self.plotter_structural_LOGS._Plotter__data)
        self.assertEqual(len(df_data_structural.columns), len(self.plotter_structural_LOGS._Plotter__df_descriptors.columns))
        
    def test_pca(self):
        """
        10. Test checks if pca is assigned
        """
        self.plotter_tailored_LOGS.tsne(perplexity=30, random_state=None, pca=True)
        df_data_tailored = pd.DataFrame(self.plotter_tailored_LOGS._Plotter__data)
        self.assertEqual(len(df_data_tailored.columns), len(self.plotter_tailored_LOGS._Plotter__df_descriptors.columns))

        self.plotter_structural_LOGS.tsne(perplexity=30, random_state=None, pca=True)
        df_data_structural = pd.DataFrame(self.plotter_structural_LOGS._Plotter__data)
        self.assertEqual(len(df_data_structural.columns), 10)

    def test_plot_title(self):
        """
        11. Test checks if correct title is assigned
        """
        self.plotter_tailored_LOGS.tsne()
        self.assertEqual(self.plotter_tailored_LOGS._Plotter__plot_title, "t-SNE plot")
    
    def test_return_dataframe(self):
        """
        12. Test checks if the returned object is a dataframe
        """
        result = self.plotter_tailored_LOGS.tsne()
        self.assertTrue(isinstance(result, pd.DataFrame))
        
    def test_shape_target(self):
        """
        13. Test checks if dataframe has correct shape with target
        """
        result = self.plotter_tailored_LOGS.tsne()
        self.assertEqual(result.shape[1], 3)
        
    def test_shape_no_target(self):
        """
        14. Test checks if dataframe has correct shape without target
        """
        result = self.plotter_no_target_LOGS.tsne()
        self.assertEqual(result.shape[1], 2)
        
    def test_column_labels(self):
        """
        15. Test checks if correct column lables are assigned
        """
        result = self.plotter_tailored_LOGS.tsne()
        column_one = "t-SNE-1"
        column_two = "t-SNE-2"
        column_three = "target"
        self.assertEqual(result.columns[0], column_one)
        self.assertEqual(result.columns[1], column_two)
        self.assertEqual(result.columns[2], column_three)
        
    def test_correct_targets(self):
        """
        16. Test checks if the correct targets are assigned to the returned DataFrame
        """
        result = self.plotter_tailored_LOGS.tsne()
        self.assertEqual(list.sort(list(result['target'])), 
                         list.sort(self.plotter_tailored_LOGS._Plotter__target))
        

    
if __name__ == '__main__':
    unittest.main()
    
