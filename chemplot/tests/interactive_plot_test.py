import unittest
from unittest.mock import patch
from chemplot.utils import load_data
import pytest

import bokeh
import pandas as pd 
import numpy as np
import base64
import os, os.path
import re
from chemplot import Plotter
from chemplot import parameters
from bokeh.models import Tabs
from bokeh.plotting.figure import Figure
from scipy import stats
from rdkit.Chem import Draw
from io import StringIO
from PIL import Image
from io import BytesIO
from pathlib import Path

@pytest.mark.usefixtures("visualize_data")
class TestInteractivePlot(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("test_filename.html")
        except:
            pass
        
    def test_default_kind_none(self):
        """
        1. Test checks if default kind is assigned
        """
        result = self.plotter_pca_LOGS.interactive_plot(size=20, remove_outliers=False, is_colored=True)
        self.assertTrue(isinstance(result.renderers[0].glyph, bokeh.models.markers.Circle))
    
    def test_default_kind(self):
        """
        2. Test checks if default kind is assigned with anytext
        """
        result = self.plotter_pca_LOGS.interactive_plot(kind='anytext', size=20, remove_outliers=False, is_colored=True)
        self.assertTrue(isinstance(result.renderers[0].glyph, bokeh.models.markers.Circle))
        assert len(result.renderers) == 1
    
    @patch('sys.stdout', new_callable=StringIO)  
    def test_INFO_kind_with_anytext(self, mock_stdout):
        """
        3. Test checks if user is informed about kind
        """
        self.plotter_pca_LOGS.interactive_plot(kind='anytext', size=20, remove_outliers=False, is_colored=True)
        assert str('kind indicates which type of plot must be visualized. Currently supported interactive visualization are:\n'+
                  '-scatter plot (scatter)\n'+
                  '-hexagon plot (hex)\n'+
                  'Please input one between scatter, hex or kde for parameter kind.\n'+
                  'As default scatter has been taken.') in mock_stdout.getvalue()
        
    def test_default_is_colored(self):
        """
        4. Test checks if default is_colored is assigned
        """
        result = self.plotter_pca_LOGS.interactive_plot(kind='scatter', size=20, remove_outliers=False)
        self.assertEqual(result.renderers[0].glyph.line_color['field'], 'target')
        self.assertTrue(isinstance(result.renderers[0].glyph.line_color['transform'], bokeh.models.mappers.LinearColorMapper))
        self.assertEqual(result.right[0].color_mapper, result.renderers[0].glyph.line_color['transform'])
        
        result = self.plotter_pca_BBBP.interactive_plot(kind='scatter', size=20, remove_outliers=False)
        self.assertEqual(result.renderers[0].glyph.line_color['field'], 'target')
        self.assertTrue(isinstance(result.renderers[0].glyph.line_color['transform'], bokeh.models.mappers.CategoricalColorMapper))
        self.assertEqual(result.legend.location,"top_left")
        self.assertEqual(len(result.legend.items), 2)
        
    def test_default_remove_outliers(self):
        """
        5. Test checks if default remove_outliers is assigned
        """
        self.plotter_pca_LOGS.interactive_plot(kind='scatter', size=20, is_colored=True)
        x = self.plotter_pca_LOGS._Plotter__df_2_components.columns[0]
        y = self.plotter_pca_LOGS._Plotter__df_2_components.columns[1]
        self.assertTrue(self.plotter_pca_LOGS.df_plot_xy.equals(self.plotter_pca_LOGS._Plotter__df_2_components[[x,y]]))
        
    def test_default_size(self):
        """
        6. Test checks if default size is assigned
        """
        result = self.plotter_pca_LOGS.interactive_plot(kind='scatter', remove_outliers=False, is_colored=True)
        self.assertEqual(result.plot_width, 700)
        self.assertEqual(result.plot_height, 700)
        
    def test_kind_scatter(self):
        """
        7. Test checks if kind is assigned
        """
        result = self.plotter_pca_LOGS.interactive_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True)
        self.assertTrue(isinstance(result.renderers[0].glyph, bokeh.models.markers.Circle))
        
    def test_is_colored_true_scatter(self):
        """
        8. Test checks if is_colored is assigned
        """
        result = self.plotter_pca_LOGS.interactive_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True)
        self.assertEqual(result.renderers[0].glyph.line_color['field'], 'target')
        self.assertTrue(isinstance(result.renderers[0].glyph.line_color['transform'], bokeh.models.mappers.LinearColorMapper))
        self.assertEqual(result.right[0].color_mapper, result.renderers[0].glyph.line_color['transform'])
        
        result = self.plotter_pca_BBBP.interactive_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True)
        self.assertEqual(result.renderers[0].glyph.line_color['field'], 'target')
        self.assertTrue(isinstance(result.renderers[0].glyph.line_color['transform'], bokeh.models.mappers.CategoricalColorMapper))
        self.assertEqual(result.legend.location,"top_left")
        self.assertEqual(len(result.legend.items), 2)
        
    def test_is_colored_false_scatter(self):
        """
        9. Test checks if is_colored is assigned
        """
        result = self.plotter_pca_LOGS.interactive_plot(kind='scatter', size=20, remove_outliers=False, is_colored=False)
        self.assertTrue(isinstance(result.renderers[0].glyph.line_color, str))
        
        result = self.plotter_pca_BBBP.interactive_plot(kind='scatter', size=20, remove_outliers=False, is_colored=False)
        self.assertTrue(isinstance(result.renderers[0].glyph.line_color, str))
        
    def test_remove_outliers_false_scatter(self):
        """
        10. Test checks if remove_outliers is assigned
        """
        self.plotter_pca_LOGS.interactive_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True)
        x = self.plotter_pca_LOGS._Plotter__df_2_components.columns[0]
        y = self.plotter_pca_LOGS._Plotter__df_2_components.columns[1]
        self.assertTrue(self.plotter_pca_LOGS.df_plot_xy.equals(self.plotter_pca_LOGS._Plotter__df_2_components[[x,y]]))
        
    def test_remove_outliers_true_scatter(self):
        """
        11. Test checks if remove_outliers is assigned
        """
        self.plotter_pca_LOGS.interactive_plot(kind='scatter', size=20, remove_outliers=True, is_colored=True)
        df_no_outliers = self.plotter_pca_LOGS._Plotter__df_2_components.copy()
        x = self.plotter_pca_LOGS._Plotter__df_2_components.columns[0]
        y = self.plotter_pca_LOGS._Plotter__df_2_components.columns[1]
        df_no_outliers = df_no_outliers[[x,y]]
        df_no_outliers= df_no_outliers[(np.abs(stats.zscore(df_no_outliers))<3).all(axis=1)]
        self.assertTrue(self.plotter_pca_LOGS.df_plot_xy.equals(df_no_outliers))
        
    def test_size_scatter(self):
        """
        12. Test checks if size is assigned
        """
        result = self.plotter_pca_LOGS.interactive_plot(kind='scatter', size=20, remove_outliers=False, is_colored=True)
        self.assertEqual(result.plot_width, 20)
        self.assertEqual(result.plot_height, 20)
        
    def test_kind_hex(self):
        """
        13. Test checks if kind is assigned
        """
        result = self.plotter_pca_LOGS.interactive_plot(kind='hex', size=20, remove_outliers=False, is_colored=True)
        self.assertTrue(isinstance(result.renderers[0].glyph, bokeh.models.glyphs.HexTile))
        
    def test_remove_outliers_false_hex(self):
        """
        14. Test checks if remove_outliers is assigned
        """
        self.plotter_pca_LOGS.interactive_plot(kind='hex', size=20, remove_outliers=False, is_colored=True)
        x = self.plotter_pca_LOGS._Plotter__df_2_components.columns[0]
        y = self.plotter_pca_LOGS._Plotter__df_2_components.columns[1]
        self.assertTrue(self.plotter_pca_LOGS.df_plot_xy.equals(self.plotter_pca_LOGS._Plotter__df_2_components[[x,y]]))
        
    def test_remove_outliers_true_hex(self):
        """
        15. Test checks if remove_outliers is assigned
        """
        self.plotter_pca_LOGS.interactive_plot(kind='hex', size=20, remove_outliers=True, is_colored=True)
        df_no_outliers = self.plotter_pca_LOGS._Plotter__df_2_components.copy()
        x = self.plotter_pca_LOGS._Plotter__df_2_components.columns[0]
        y = self.plotter_pca_LOGS._Plotter__df_2_components.columns[1]
        df_no_outliers = df_no_outliers[[x,y]]
        df_no_outliers= df_no_outliers[(np.abs(stats.zscore(df_no_outliers))<3).all(axis=1)]
        self.assertTrue(self.plotter_pca_LOGS.df_plot_xy.equals(df_no_outliers))
        
    def test_size_hex(self):
        """
        16. Test checks if size is assigned
        """
        result = self.plotter_pca_LOGS.interactive_plot(kind='hex', size=20, remove_outliers=False, is_colored=True)
        self.assertEqual(result.plot_width, 20)
        self.assertEqual(result.plot_height, 20)
        
    def test_tools_scatter(self):
        """
        17. Test checks if the tools are set correctly for scatter
        """
        expected = [bokeh.models.tools.PanTool,
                    bokeh.models.tools.LassoSelectTool,
                    bokeh.models.tools.WheelZoomTool,
                    bokeh.models.tools.HoverTool,
                    bokeh.models.tools.SaveTool,
                    bokeh.models.tools.ResetTool]
        result = self.plotter_pca_LOGS.interactive_plot(kind='scatter')
        self.assertEqual(len(result.tools), len(expected))
        for expected_tool in expected:
            self.assertTrue(any(isinstance(tool, expected_tool) for tool in result.tools))
            
    def test_tools_hex(self):
        """
        18. Test checks if the tools are set correctly for hex
        """
        expected = [bokeh.models.tools.PanTool,
                    bokeh.models.tools.WheelZoomTool,
                    bokeh.models.tools.HoverTool,
                    bokeh.models.tools.SaveTool,
                    bokeh.models.tools.ResetTool]
        result = self.plotter_pca_LOGS.interactive_plot(kind='hex')
        self.assertEqual(len(result.tools), len(expected))
        for expected_tool in expected:
            self.assertTrue(any(isinstance(tool, expected_tool) for tool in result.tools))
            
    def test_tooltips_scatter(self):
        """
        19. Test checks if the tooltips are set correctly for scatter
        """
        result = self.plotter_pca_LOGS.interactive_plot(kind='scatter')
        for tool in result.tools:
            if isinstance(tool, bokeh.models.tools.HoverTool):
                self.assertEqual(tool.tooltips, parameters.TOOLTIPS_TARGET)
                
        data_SAMPL = load_data('R_642_SAMPL') 
        cp_SAMPL = Plotter.from_smiles(data_SAMPL["smiles"], sim_type="structural")
        cp_SAMPL.pca()
        result = cp_SAMPL.interactive_plot(kind='scatter')
        for tool in result.tools:
            if isinstance(tool, bokeh.models.tools.HoverTool):
                self.assertEqual(tool.tooltips, parameters.TOOLTIPS_NO_TARGET)
                
    def test_tooltips_hex(self):
        """
        20. Test checks if the tooltips are set correctly for hex
        """
        result = self.plotter_pca_LOGS.interactive_plot(kind='hex')
        for tool in result.tools:
            if isinstance(tool, bokeh.models.tools.HoverTool):
                self.assertEqual(tool.tooltips, [("count", "@c")])
                
    def test_imgs(self):
        """
        21. Test checks if the images for the tooltips are correctly set
        """
        expected=[]
        for mol in self.plotter_pca_LOGS._Plotter__mols:
            try:
                png = Draw.MolToImage(mol)
                out = BytesIO()
                png.save(out, format='png')
                png = out.getvalue()
                url = 'data:image/png;base64,' + base64.b64encode(png).decode('utf-8')
            except:
                url = None
            expected.append(url)
        result = self.plotter_pca_LOGS.interactive_plot(kind='scatter')
        self.assertEqual(list.sort(list(result.renderers[0].data_source.data['imgs'])),
                         list.sort(expected))
        
    def test_default_filename(self):
        """
        22. Test checks if the default value of filename is assigned
        """
        try:
            os.remove("test_filename.html")
        except FileNotFoundError:
            pass
        expected = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.plotter_pca_LOGS.interactive_plot()
        result = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.assertEqual(expected, result)
        
    def test_filename(self):
        """
        23. Test checks if the value of filename is assigned
        """
        try:
            os.remove("test_filename.html")
        except FileNotFoundError:
            pass
        expected = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.plotter_pca_LOGS.interactive_plot(filename="test_filename.html")
        result = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.assertEqual(expected, result - 1)
        os.remove("test_filename.html")
        
    def test_default_show_plot(self):
        """
        24. Test checks if the default value of show_plot is assigned
        """
        self.plotter_pca_LOGS.interactive_plot()
        self.assertTrue(not(self.plotter_pca_LOGS._Plotter__open_plot.has_been_called))
        
    def test_show_plot(self):
        """
        25. Test checks if the value of show_plot is assigned
        """
        self.plotter_pca_LOGS.interactive_plot(show_plot=True)
        self.assertTrue(self.plotter_pca_LOGS._Plotter__open_plot.has_been_called)
        
    def test_default_title(self):
        """
        26. Test checks if the default value of title is assigned
        """
        result = self.plotter_pca_LOGS.interactive_plot(kind="scatter")
        self.assertTrue(result.title.text, self.plotter_pca_BBBP._Plotter__plot_title)
        
    def test_title(self):
        """
        27. Test checks if the value of title is assigned
        """
        result = self.plotter_pca_LOGS.interactive_plot(kind="scatter", title="title")
        self.assertTrue(result.title.text, "title")
        
    @patch('sys.stdout', new_callable=StringIO)  
    def test_INFO_call_without_reduction(self, mock_stdout):
        """
        28. Test checks if user is informed a plot cannot be created without reducing the dimensions first
        """
        result = self.plotter_sampl.interactive_plot()
        assert result is None
        assert 'Reduce the dimensions of your molecules before creating a plot.' in mock_stdout.getvalue()
        
    # Clustering 
    
    @patch('sys.stdout', new_callable=StringIO)  
    def test_INFO_cluster_call_without_clusters(self, mock_stdout):
        """
        29. Test checks if user is informed a cluster plot cannot be created without reducing the dimensions first
        """
        self.plotter_pca_LOGS.interactive_plot(clusters=True)
        assert 'Call cluster() before visualizing a plot with clusters.' in mock_stdout.getvalue()
        
    def test_clusters_default(self):
        """
        30. Test if default value of clusters is assigned
        """
        self.plotter_pca_BBBP.cluster(n_clusters=5)
        result = self.plotter_pca_BBBP.interactive_plot()
        assert isinstance(result, Figure)
        assert not isinstance(result, Tabs)
        
    def test_clusters_true(self):
        """
        31. Test to check if the cluster panel is correctly set up
        """
        self.plotter_pca_BBBP.cluster(n_clusters=5)
        result = self.plotter_pca_BBBP.interactive_plot(clusters=True)
        assert isinstance(result, Tabs)
        tab1 = result.tabs[0]
        tab2 = result.tabs[1]
        assert result.active == 0
        assert tab1.title == 'Plot'
        assert tab2.title == 'Clusters'
        assert isinstance(tab1.child, Figure)
        assert isinstance(tab2.child, Figure)
    
    def test_clusters_groups(self):
        """
        31. Test to check if all clusters group are added to the figure
        """
        data = self.plotter_pca_BBBP.cluster(n_clusters=5)
        result = self.plotter_pca_BBBP.interactive_plot(clusters=True)
        figure = result.tabs[1].child
        assert len(figure.renderers) == 5
        self.plotter_pca_BBBP.cluster(n_clusters=3)
        result = self.plotter_pca_BBBP.interactive_plot(clusters=True)
        figure = result.tabs[1].child
        assert len(figure.renderers) == 3
        total = 0
        for marker in figure.renderers:
            self.assertTrue(isinstance(marker.glyph, bokeh.models.markers.Circle))
            assert marker.muted_glyph.fill_color == '#717375'
            total += marker.data_source.data['clusters'].size
        assert total == len(data)

    def test_clusters_legend(self):
        """
        32. Test to check if the legend is set correctly when clusters is True
        """
        self.plotter_pca_BBBP.cluster(n_clusters=5)
        result = self.plotter_pca_BBBP.interactive_plot(clusters=True)
        legend = result.tabs[1].child.legend
        assert legend.location == "top_left"
        assert legend.title == "Clusters"
        assert legend.click_policy == "mute"
        assert len(legend.items) == 5
        indeces = ['0', '1', '2', '3', '4']
        total = 0
        for item in legend.items:
            digits = re.search(r'^Cluster (\d) - (\d\d?\d?)%', item.label['value']).groups()
            assert digits[0] in indeces
            indeces.remove(digits[0])
            total += int(digits[1])
        assert len(indeces) == 0
        assert total == 100
    
    def test_tooltips_cluster(self):
        """
        33. Test to check if the tooltips for cluster plots are set correctly
        """
        self.plotter_pca_BBBP.cluster(n_clusters=5)
        result = self.plotter_pca_BBBP.interactive_plot(clusters=True)
        for tool in result.tabs[1].child.tools:
            if isinstance(tool, bokeh.models.tools.HoverTool):
                self.assertEqual(tool.tooltips, parameters.TOOLTIPS_CLUSTER)
    
if __name__ == '__main__':
    unittest.main()
    
