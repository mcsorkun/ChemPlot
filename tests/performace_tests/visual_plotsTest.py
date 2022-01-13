"""
Visual Plots Test for ChemPlot

The output of these tests will be a .pdf file containing different plots 
with all possible parameters in order to visually inspect the output of 
ChemPlot.
"""
from chemplot import Plotter
from matplotlib import pyplot
from matplotlib.backends.backend_pdf import PdfPages
from pathlib import Path
import pandas as pd 

THIS_DIR = Path(__file__).parent

class PlotsTest(object):
    
    def __init__(self):
        self.output = PdfPages('Visual_Plots_Test.pdf')
    
    def run(self, reg_data_1, reg_data_2, class_data_1, class_data_2):
        self.plot_regression_data(reg_data_1[0], reg_data_1[1])
        self.plot_regression_data(reg_data_2[0], reg_data_2[1])
        self.plot_classification_data(class_data_1[0], class_data_1[1])
        self.plot_classification_data(class_data_2[0], class_data_2[1])
        
        self.output.close()


    def plot_regression_data(self, reg_data, name_data):
        # Create plotter objects for tailored and structural similarity
        cp_tailored = Plotter.from_smiles(reg_data["smiles"], target=reg_data["target"], target_type="R", sim_type='tailored')
        cp_structural = Plotter.from_smiles(reg_data["smiles"], target=reg_data["target"], target_type="R", sim_type='structural')      
        
        self.generate_plots(cp_tailored, name_data + ' Regression Tailored -')
        self.generate_plots(cp_structural, name_data + ' Regression Structural -')
        
    
    def plot_classification_data(self, class_data, name_data):
        # Create plotter objects for tailored and structural similarity
        cp_tailored = Plotter.from_smiles(class_data["smiles"], target=class_data["target"], target_type="C", sim_type='tailored')
        cp_structural = Plotter.from_smiles(class_data["smiles"], target=class_data["target"], target_type="C", sim_type='structural')      
    
        self.generate_plots(cp_tailored, name_data + ' Classification Tailored -')
        self.generate_plots(cp_structural, name_data + ' Classification Structural -')
        
        
    def generate_plots(self, cp, name):
        size = 20
        cp.pca()
        # Get scatter plots PCA
        plot_pca_scatter = cp.visualize_plot(kind="scatter", size=size, remove_outliers=False, is_colored=True, colorbar=False)
        plot_pca_scatter.set_title(name + " pca scatter plot",fontsize=size*2)
        self.output.savefig(plot_pca_scatter.figure)
        # Get hex plots PCA
        plot_pca_hex = cp.visualize_plot(kind="hex", size=size, remove_outliers=False, is_colored=True, colorbar=False)
        plot_pca_hex.set_title(name + " pca hex plot",fontsize=size*2)
        self.output.savefig(plot_pca_hex.figure)
        # Get kde plots PCA
        plot_pca_kde = cp.visualize_plot(kind="kde", size=size, remove_outliers=False, is_colored=True, colorbar=False)
        plot_pca_kde.set_title(name + " pca kde plot",fontsize=size*2)
        self.output.savefig(plot_pca_kde.figure)
        
        cp.tsne(perplexity=None, random_state=None, pca=False)
        # Get scatter plots t-SNE
        plot_tsne_scatter = cp.visualize_plot(kind="scatter", size=20, remove_outliers=False, is_colored=True, colorbar=False)
        plot_tsne_scatter.set_title(name + " tsne scatter plot",fontsize=size*2)
        self.output.savefig(plot_tsne_scatter.figure)
        # Get hex plots t-SNE
        plot_tsne_hex = cp.visualize_plot(kind="hex", size=20, remove_outliers=False, is_colored=True, colorbar=False)
        plot_tsne_hex.set_title(name + " tsne hex plot",fontsize=size*2)
        self.output.savefig(plot_tsne_hex.figure)
        # Get kde plots t-SNE
        plot_tsne_kde = cp.visualize_plot(kind="kde", size=20, remove_outliers=False, is_colored=True, colorbar=False)
        plot_tsne_kde.set_title(name + " tsne kde plot",fontsize=size*2)
        self.output.savefig(plot_tsne_kde.figure)

        cp.umap(n_neighbors=None, min_dist=None, random_state=None)
        # Get scatter plots UMAP
        plot_umap_scatter = cp.visualize_plot(kind="scatter", size=20, remove_outliers=False, is_colored=True, colorbar=False)
        plot_umap_scatter.set_title(name + " umap scatter plot",fontsize=size*2)
        self.output.savefig(plot_umap_scatter.figure)
        # Get hex plots UMAP
        plot_umap_hex = cp.visualize_plot(kind="hex", size=20, remove_outliers=False, is_colored=True, colorbar=False)
        plot_umap_hex.set_title(name + " umap hex plot",fontsize=size*2)
        self.output.savefig(plot_umap_hex.figure)
        # Get kde plots UMAP
        plot_umap_kde = cp.visualize_plot(kind="kde", size=20, remove_outliers=False, is_colored=True, colorbar=False)
        plot_umap_kde.set_title(name + " umap kde plot",fontsize=size*2)
        self.output.savefig(plot_umap_kde.figure)
        
        pyplot.close('all')
        
        
        
if __name__ == '__main__':
    file_LOGS = THIS_DIR / '..' / 'test_data' / 'R_1291_LOGS.csv'
    file_BACE = THIS_DIR / '..' / 'test_data' / 'R_1513_BACE.csv'
    data_LOGS = pd.read_csv(file_LOGS)
    data_BACE = pd.read_csv(file_BACE)
    
    file_BBBP = THIS_DIR / '..' / 'test_data' / 'C_2039_BBBP_2.csv'
    file_BACE_2 = THIS_DIR / '..' / 'test_data' / 'C_1513_BACE_2.csv'
    data_BBBP = pd.read_csv(file_BBBP)
    data_BACE_2 = pd.read_csv(file_BACE_2)
    
    PlotsTest().run([data_LOGS, 'LOGS'], [data_BACE, 'BACE'], [data_BBBP, 'BBBP'], [data_BACE_2, 'BACE_2'])