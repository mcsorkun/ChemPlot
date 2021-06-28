import unittest
from unittest.mock import patch

from chemplot import Plotter
import pandas as pd 
import numpy as np
import os
from scipy import stats
from matplotlib import pyplot
from io import StringIO

class TestVisualizePlot(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.data_LOGS = pd.read_csv("test_data\\R_1291_LOGS.csv") 
        cls.data_BBBP = pd.read_csv("test_data\\C_2039_BBBP_2.csv") 
        
        cls.plotter_pca_LOGS = Plotter.from_smiles(cls.data_LOGS["smiles"], target=cls.data_LOGS["target"], target_type="R", sim_type="tailored")
        cls.plotter_pca_BBBP = Plotter.from_smiles(cls.data_BBBP["smiles"], target=cls.data_BBBP["target"], target_type="C", sim_type="tailored")
        
        cls.plotter_pca_LOGS.pca()
        cls.plotter_pca_BBBP.pca()
        
    def test_default_kind_none(self):
        """
        1. Test checks if default kind is assigned
        """
        result = self.plotter_pca_LOGS.visualize_plot(size=20, remove_outliers=False, is_colored=True, colorbar=False)
        self.assertEqual(result.get_label(), "scatter")
        pyplot.close()
    
    def test_default_kind(self):
        """
        2. Test checks if default kind is assigned with anytext
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='anytext', size=20, remove_outliers=False, is_colored=True, colorbar=False)
        self.assertEqual(result.get_label(), "scatter")
        pyplot.close()
    
    @patch('sys.stdout', new_callable=StringIO)  
    def test_INFO_kind_with_anytext(self, mock_stdout):
        """
        3. Test checks if user is informed about kind
        """
        self.plotter_pca_LOGS.visualize_plot(kind='anytext', size=20, remove_outliers=False, is_colored=True, colorbar=False)
        assert str('kind indicates which type of plot must be visualized. Currently supported static visualization are:\n'+
                   '-scatter plot (scatter)\n'+
                   '-hexagon plot (hex)\n'+
                   '-kernel density estimation plot (kde)\n'+
                   'Please input one between scatter, hex or kde for parameter kind.\n'+
                   'As default scatter has been taken.') in mock_stdout.getvalue()
        pyplot.close()
        
    def test_default_is_colored(self):
        """
        4. Test checks if default is_colored is assigned
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='scatter', size=20, remove_outliers=False, colorbar=False)
        self.assertTrue(len(result.collections)>1)
        pyplot.close()
        
    def test_default_remove_outliers(self):
        """
        5. Test checks if default remove_outliers is assigned
        """
        self.plotter_pca_LOGS.visualize_plot(kind='scatter', size=20, is_colored=True, colorbar=False)
        x = self.plotter_pca_LOGS._Plotter__df_2_components.columns[0]
        y = self.plotter_pca_LOGS._Plotter__df_2_components.columns[1]
        self.assertTrue(self.plotter_pca_LOGS.df_plot_xy.equals(self.plotter_pca_LOGS._Plotter__df_2_components[[x,y]]))
        pyplot.close()
        
    def test_default_size(self):
        """
        6. Test checks if default size is assigned
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='scatter', remove_outliers=False, is_colored=True, colorbar=False)
        self.assertEqual(result.figure.get_size_inches()[0], 20)
        self.assertEqual(result.figure.get_size_inches()[1], 20)
        pyplot.close()
        
    def test_kind_scatter(self):
        """
        7. Test checks if kind is assigned
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True, colorbar=False)
        self.assertEqual(result.get_label(), "scatter")
        pyplot.close()
        
    def test_is_colored_true_scatter(self):
        """
        8. Test checks if is_colored is assigned
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True, colorbar=False)
        self.assertTrue(len(result.collections)>1)
        pyplot.close()
        
    def test_is_colored_false_scatter(self):
        """
        9. Test checks if is_colored is assigned
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='scatter', size=20, remove_outliers=False, is_colored=False, colorbar=False)
        self.assertTrue(len(result.collections) == 1)
        pyplot.close()
        
    def test_remove_outliers_false_scatter(self):
        """
        10. Test checks if remove_outliers is assigned
        """
        self.plotter_pca_LOGS.visualize_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True, colorbar=False)
        x = self.plotter_pca_LOGS._Plotter__df_2_components.columns[0]
        y = self.plotter_pca_LOGS._Plotter__df_2_components.columns[1]
        self.assertTrue(self.plotter_pca_LOGS.df_plot_xy.equals(self.plotter_pca_LOGS._Plotter__df_2_components[[x,y]]))
        pyplot.close()
        
    def test_remove_outliers_true_scatter(self):
        """
        11. Test checks if remove_outliers is assigned
        """
        self.plotter_pca_LOGS.visualize_plot(kind='scatter', size=20, remove_outliers=True, is_colored=True, colorbar=False)
        df_no_outliers = self.plotter_pca_LOGS._Plotter__df_2_components.copy()
        x = self.plotter_pca_LOGS._Plotter__df_2_components.columns[0]
        y = self.plotter_pca_LOGS._Plotter__df_2_components.columns[1]
        df_no_outliers = df_no_outliers[[x,y]]
        df_no_outliers= df_no_outliers[(np.abs(stats.zscore(df_no_outliers))<3).all(axis=1)]
        self.assertTrue(self.plotter_pca_LOGS.df_plot_xy.equals(df_no_outliers))
        pyplot.close()
        
    def test_size_scatter(self):
        """
        12. Test checks if size is assigned
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True, colorbar=False)
        self.assertEqual(result.figure.get_size_inches()[0], 20)
        self.assertEqual(result.figure.get_size_inches()[1], 20)
        pyplot.close()
        
    def test_kind_hex(self):
        """
        13. Test checks if kind is assigned
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='hex', size=20, remove_outliers=False, is_colored=True, colorbar=False)
        self.assertEqual(result.get_label(), "hex")
        pyplot.close()
        
    def test_remove_outliers_false_hex(self):
        """
        14. Test checks if remove_outliers is assigned
        """
        self.plotter_pca_LOGS.visualize_plot(kind='hex', size=20, remove_outliers=False, is_colored=True, colorbar=False)
        x = self.plotter_pca_LOGS._Plotter__df_2_components.columns[0]
        y = self.plotter_pca_LOGS._Plotter__df_2_components.columns[1]
        self.assertTrue(self.plotter_pca_LOGS.df_plot_xy.equals(self.plotter_pca_LOGS._Plotter__df_2_components[[x,y]]))
        pyplot.close()
        
    def test_remove_outliers_true_hex(self):
        """
        15. Test checks if remove_outliers is assigned
        """
        self.plotter_pca_LOGS.visualize_plot(kind='hex', size=20, remove_outliers=True, is_colored=True, colorbar=False)
        df_no_outliers = self.plotter_pca_LOGS._Plotter__df_2_components.copy()
        x = self.plotter_pca_LOGS._Plotter__df_2_components.columns[0]
        y = self.plotter_pca_LOGS._Plotter__df_2_components.columns[1]
        df_no_outliers = df_no_outliers[[x,y]]
        df_no_outliers= df_no_outliers[(np.abs(stats.zscore(df_no_outliers))<3).all(axis=1)]
        self.assertTrue(self.plotter_pca_LOGS.df_plot_xy.equals(df_no_outliers))
        pyplot.close()
        
    def test_size_hex(self):
        """
        16. Test checks if size is assigned
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='hex', size=20, remove_outliers=False, is_colored=True, colorbar=False)
        self.assertEqual(result.figure.get_size_inches()[0], 20)
        self.assertEqual(result.figure.get_size_inches()[1], 20)
        pyplot.close()
        
    def test_kind_kde(self):
        """
        17. Test checks if kind is assigned
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='kde', size=20, remove_outliers=False, is_colored=True, colorbar=False)
        self.assertEqual(result.get_label(), "kde")
        pyplot.close()
        
    def test_remove_outliers_false_kde(self):
        """
        18. Test checks if remove_outliers is assigned
        """
        self.plotter_pca_LOGS.visualize_plot(kind='kde', size=20, remove_outliers=False, is_colored=True, colorbar=False)
        x = self.plotter_pca_LOGS._Plotter__df_2_components.columns[0]
        y = self.plotter_pca_LOGS._Plotter__df_2_components.columns[1]
        self.assertTrue(self.plotter_pca_LOGS.df_plot_xy.equals(self.plotter_pca_LOGS._Plotter__df_2_components[[x,y]]))
        pyplot.close()
        
    def test_remove_outliers_true_kde(self):
        """
        19. Test checks if remove_outliers is assigned
        """
        self.plotter_pca_LOGS.visualize_plot(kind='kde', size=20, remove_outliers=True, is_colored=True, colorbar=False)
        df_no_outliers = self.plotter_pca_LOGS._Plotter__df_2_components.copy()
        x = self.plotter_pca_LOGS._Plotter__df_2_components.columns[0]
        y = self.plotter_pca_LOGS._Plotter__df_2_components.columns[1]
        df_no_outliers = df_no_outliers[[x,y]]
        df_no_outliers= df_no_outliers[(np.abs(stats.zscore(df_no_outliers))<3).all(axis=1)]
        self.assertTrue(self.plotter_pca_LOGS.df_plot_xy.equals(df_no_outliers))
        pyplot.close()
        
    def test_size_kde(self):
        """
        20. Test checks if size is assigned
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='kde', size=20, remove_outliers=False, is_colored=True, colorbar=False)
        self.assertEqual(result.figure.get_size_inches()[0], 20)
        self.assertEqual(result.figure.get_size_inches()[1], 20)
        pyplot.close()
        
    def test_default_colorbar(self):
        """
        21. Test checks if default value of colorbar is assigned
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True)
        self.assertNotIsInstance(result.get_legend(), type(None))
        self.assertEqual(len(result.figure.axes), 1)
        pyplot.close()
        
    def test_colorbar_R_remove_legend(self):
        """
        22. Test checks if colorbar is assigned when target type is R and therefore legend removed
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True, colorbar=True)
        self.assertIsInstance(result.get_legend(), type(None))
        pyplot.close()
        
    def test_colorbar_C_keep_legend(self):
        """
        23. Test checks if colorbar is ignored when target type is C and therefore legend kept
        """
        result = self.plotter_pca_BBBP.visualize_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True, colorbar=True)
        self.assertNotIsInstance(result.get_legend(), type(None))
        pyplot.close()
        
    def test_colorbar_R_add_colorbar(self):
        """
        24. Test checks if colorbar is assigned when target type is R
        """
        result = self.plotter_pca_LOGS.visualize_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True, colorbar=True)
        self.assertTrue(len(result.figure.axes)>=1)
        pyplot.close()
        
    def test_colorbar_C_ignore_colorbar(self):
        """
        25. Test checks if colorbar is ignored when target type is C 
        """
        result = self.plotter_pca_BBBP.visualize_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True, colorbar=True)
        self.assertTrue(len(result.figure.axes)==1)
        pyplot.close()
        
    def test_default_title(self):
        """
        26. Test checks if the default title is assigned
        """
        result = self.plotter_pca_BBBP.visualize_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True, colorbar=True)
        self.assertEqual(result.get_title(), self.plotter_pca_BBBP._Plotter__plot_title)
        pyplot.close()
        
    def test_assigned_title(self):
        """
        27. Test checks if title is assigned
        """
        result = self.plotter_pca_BBBP.visualize_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True, colorbar=True, title="title")
        self.assertTrue(result.get_title()=="title")
        pyplot.close()
     
    @patch('sys.stdout', new_callable=StringIO)  
    def test_INFO_call_without_reduction(self, mock_stdout):
        """
        28. Test checks if user is informed a plot cannot be created without reducing the dimensions first
        """
        data_SAMPL = pd.read_csv("test_data\\R_642_SAMPL.csv") 
        cp = Plotter.from_smiles(data_SAMPL["smiles"], target=data_SAMPL["target"], target_type="R", sim_type="tailored")
        result = cp.visualize_plot()
        assert result is None
        assert 'Reduce the dimensions of your molecules before creating a plot.' in mock_stdout.getvalue()
        
    def test_default_filename_scatter(self):
        """
        29. Test checks if the default value of filename is assigned with scatter
        """
        try:
            os.remove("scatter_test.png")
        except FileNotFoundError:
            pass
        expected = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.plotter_pca_BBBP.visualize_plot(kind='scatter')
        result = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.assertEqual(expected, result)
        pyplot.close()
        
    def test_filename_scatter(self):
        """
        30. Test checks if the value of filename is assigned with scatter
        """
        try:
            os.remove("scatter_test.png")
        except FileNotFoundError:
            pass
        expected = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.plotter_pca_BBBP.visualize_plot(kind='scatter', filename="scatter_test.png")
        result = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.assertEqual(expected, result - 1)
        os.remove("scatter_test.png")
        pyplot.close()
        
    def test_default_filename_hex(self):
        """
        31. Test checks if the default value of filename is assigned with hex
        """
        try:
            os.remove("hex_test.png")
        except FileNotFoundError:
            pass
        expected = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.plotter_pca_BBBP.visualize_plot(kind='hex')
        result = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.assertEqual(expected, result)
        pyplot.close()
        
    def test_filename_hex(self):
        """
        32. Test checks if the value of filename is assigned with hex
        """
        try:
            os.remove("hex_test.png")
        except FileNotFoundError:
            pass
        expected = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.plotter_pca_BBBP.visualize_plot(kind='hex', filename="hex_test.png")
        result = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.assertEqual(expected, result - 1)
        os.remove("hex_test.png")
        pyplot.close()
        
    def test_default_filename_kde(self):
        """
        33. Test checks if the default value of filename is assigned with kde
        """
        try:
            os.remove("kde_test.png")
        except FileNotFoundError:
            pass
        expected = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.plotter_pca_BBBP.visualize_plot(kind='kde')
        result = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.assertEqual(expected, result)
        pyplot.close()
        
    def test_filename_kde(self):
        """
        34. Test checks if the value of filename is assigned with kde
        """
        try:
            os.remove("kde_test.png")
        except FileNotFoundError:
            pass
        expected = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.plotter_pca_BBBP.visualize_plot(kind='kde', filename="kde_test.png")
        result = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.assertEqual(expected, result - 1)
        os.remove("kde_test.png")
        pyplot.close()
        
    
if __name__ == '__main__':
    unittest.main()
    
