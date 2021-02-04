import chemplot.descriptors as desc
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import umap
import seaborn as sns
from scipy import stats
import numpy as np
import math
import matplotlib.pyplot as plt

class Plotter(object):
    """
    A class used to plot the ECFP fingerprints of the molecules used to 
    instantiate it.
    """
       
    def __init__(self, encoding_list, target, target_type, sim_type, get_desc, get_fingerprints):
           
        # Error handeling sym_type
        if sim_type != 'structural' and sim_type != 'tailored':
            if len(target) > 0:
                sim_type = 'tailored' 
                print('sim_type indicates the similarity type by which the plots are constructed.\n' +
                      'The supported similarity types are structural and tailored.\n' +
                      'Because a target list has been provided \'tailored\' as been selected as sym_type.')
            else: 
                sim_type = 'structural' 
                print('sim_type indicates the similarity type by which the plots are constructed.\n' +
                      'The supported similarity types are structural and tailored.\n' +
                      'Because no target list has been provided \'structural\' as been selected as sym_type.')
         
        if sim_type == "tailored" and len(target) == 0:
            raise Exception("Target values missing")
        
        self.sim_type = sim_type
        
        # Error handeling target_type
        if len(target) > 0:
            df_target = pd.DataFrame(data=target)
            unique_targets_ratio = 1.*df_target.iloc[:, 0].nunique()/df_target.iloc[:, 0].count() < 0.05
            if target_type == 'R' and unique_targets_ratio:
                print('Input received is \'R\' for target values that seem not continuous.')
            if target_type != 'R' and target_type != 'C':
                if unique_targets_ratio:
                    self.target_type = 'C'
                    print('target_type indicates if the target is a continuous variable or a class label.\n'+
                          'R stands for regression and C for classification. Input R as target type for continuous variables and C for class labels.\n'+
                          'From analysis of the target, C has been selected for target_type.')
                else:
                    self.target_type = 'R'
                    print('target_type indicates if the target is a continuous variable or a class label.\n'+
                          'R stands for regression and C for classification. Input R as target type for continuous variables and C for class labels.\n'+
                          'From analysis of the target, R has been selected for target_type.')
            else:
                self.target_type = target_type
        else:
            self.target_type = None
          
        # Instantiate Plotter class
        if sim_type == "tailored":
            df_descriptors = get_desc(encoding_list)
            self.df_descriptors, self.target = desc.select_descriptors_lasso(df_descriptors,target,kind=target_type)
        else:
            self.df_descriptors, self.target = get_fingerprints(encoding_list,target,2,2048)
            
    
    @classmethod        
    def from_smiles(cls, smiles_list, target=[], target_type=None, sim_type=None):
        """
        Class method to construct a Plotter object from a list of SMILES.
        
        :param smile_list: List of the SMILES representation of the molecules to plot.
        :type smile_list: dict
        :param target: target values
        :type target: dict
        :param target_type: target type R (regression) or C (classificatino)
        :type target_type: string
        :param sim_type: similarity type structural or tailored
        :type sim_type: string
        :returns: A Plotter object for the molecules given as input.
        :rtype: Plotter
        """
            
        return cls(smiles_list, target, target_type, sim_type, desc.get_mordred_descriptors, desc.get_ecfp)
            

    @classmethod
    def from_inchi(cls, inchi_list, target=[], target_type=None, sim_type=None):
        """
        Class method to construct a Plotter object from a list of InChi.
        
        :param inchi_list: List of the InChi representation of the molecules to plot.
        :type inchi_list: dict
        :param target: target values
        :type target: dict
        :param target_type: target type R (regression) or C (classificatino)
        :type target_type: string
        :param sim_type: similarity type structural or tailored
        :type sim_type: string
        :returns: A Plotter object for the molecules given as input.
        :rtype: Plotter
        """
                
        return cls(inchi_list, target, target_type, sim_type, desc.get_mordred_descriptors_from_inchi, desc.get_ecfp_from_inchi)
        
    
    def pca(self, kind="scatter", size=20, remove_outliers=False, is_colored=True, colorbar=False):
        """
        Calculates the first 2 PCA components of ECFP fingerprints and plots
        the data based on the result.
        
        :param kind: Type of plot (default is scatter plot)
        :type kind: string
        :param size: Size of the plot (default size)
        :type size: int
        :param remove_outliers: Boolean value indicating if the outliers must be identified and removed (default False)
        :type remove_outliers: boolean
        :returns: The matplotlib axes containing the plot.
        :rtype: Axes
        """
        
        # Scale the data
        if self.sim_type == "tailored":
            data = StandardScaler().fit_transform(self.df_descriptors.values.tolist())
        else:
            data = self.df_descriptors.values.tolist()

        # Linear dimensionality reduction to 2 components by PCA
        pca = PCA(n_components=2)
        first2ecpf_components = pca.fit_transform(data)
        coverage_components = pca.explained_variance_ratio_
        
        # Create labels for the plot
        first_component = "PC-1 (" + "{:.0%}".format(coverage_components[0]) + ")"
        second_component = "PC-2 (" + "{:.0%}".format(coverage_components[1]) + ")"
        # Create a dataframe containinting the first 2 PCA components of ECFP 
        self.df_2_components = pd.DataFrame(data = first2ecpf_components
             , columns = [first_component, second_component])
        
        # Create a plot based on the PCA model 
        pca_plot = self.construct_plot(first_component, second_component, size, kind, "PCA plot", remove_outliers, is_colored, colorbar)
        return pca_plot
    
    
    def tsne(self, perplexity=None, random_state=None, pca=False, kind="scatter", size=20, remove_outliers=False, is_colored=True, colorbar=False):
        """
        Calculates the first 2 t-SNE components of ECFP fingerprints and plots
        the data based on the result.
        
        :param perplexity: perplexity value for the t-SNE model
        :type perplexity: int
        :param pca_preprocessing_components: Number of components the PCA preprocessing will identify. By default the preprocessing is not used.
        :type pca_preprocessing_components: int
        :param kind: Type of plot (default is scatter plot)
        :type kind: string
        :param size: Size of the plot (default size)
        :type size: int
        :param remove_outliers: Boolean value indicating if the outliers must be identified and removed (default False)
        :type remove_outliers: boolean
        :returns: The matplotlib axes containing the plot.
        :rtype: Axes
        """
        
        # Scale the data
        if self.sim_type == "tailored":
            self.data = StandardScaler().fit_transform(self.df_descriptors.values.tolist())
        else:
            self.data = self.df_descriptors.values.tolist()
        
        plot_title = "t-SNE plot"
        # Preprocess the data with PCA
        if pca and self.sim_type == "structural":
            pca = PCA(n_components=30, random_state=random_state)
            self.data = pca.fit_transform(self.data)
            plot_title = "t-SNE plot from components with cumulative variance explained " + "{:.0%}".format(sum(pca.explained_variance_ratio_))
        
        # Define the perplexity of the model
        if perplexity == None:
            perplexity_value = max(5, min(math.sqrt(len(self.data)), 50))
        else:
            if perplexity<5 or perplexity>50:
                print('The perplexity is related to the number of nearest neighbors that is used in other manifold learning algorithms./n'+
                      'Robust results are obtained for values of perplexity between 5 and 50. The inputed value is outside that range.\n'+
                      'Therefore the closest value between 5 and 50 to the parameter inputed has been used in the method.')
            perplexity_value = max(5, min(perplexity, 50))
        # Embed the data in two dimensions
        self.tsne_fit = TSNE(n_components=2, perplexity=perplexity_value, random_state=random_state)
        ecfp_tsne_embedding = self.tsne_fit.fit_transform(self.data)
        # Create a dataframe containinting the first 2 TSNE components of ECFP 
        self.df_2_components = pd.DataFrame(data = ecfp_tsne_embedding
             , columns = ['t-SNE-1', 't-SNE-2'])
            
        # Create a plot based on the TSNE model 
        tsne_plot = self.construct_plot('t-SNE-1', 't-SNE-2', size, kind, plot_title, remove_outliers, is_colored, colorbar)
        return tsne_plot
        
        
    def umap(self, n_neighbors=None, min_dist=None, random_state=None, kind="scatter", size=20, remove_outliers=False, is_colored=True, colorbar=False):
        """
        Calculates the first 2 UMAP components of ECFP fingerprints and plots
        the data based on the result.
        
        :param num_neighbors: Number of neighbours used in the UMAP madel.
        :type num_neighbors: int
        :param kind: Type of plot (default is scatter plot)
        :type kind: string
        :param size: Size of the plot (default size)
        :type size: int
        :param remove_outliers: Boolean value indicating if the outliers must be identified and removed (default False)
        :type remove_outliers: boolean
        :returns: The matplotlib axes containing the plot.
        :rtype: Axes
        """
            
        # Scale the data
        if self.sim_type == "tailored":
            self.data = StandardScaler().fit_transform(self.df_descriptors.values.tolist())
        else:
            self.data = self.df_descriptors.values.tolist()
        
        if n_neighbors == None:
            n_neighbors = max(2, min(15, len(self.data)//4))
        else:
            if n_neighbors<2 or n_neighbors>(len(self.data)//4):
                print('n_neighbors represents the size of the local neighborhood UMAP will look at when attempting to learn the manifold structure of the data./n'+
                      'Robust results are obtained for values of n_neighbors between 2 up to a quarter of the data. The inputed value is outside that range.\n'+
                      'Therefore the closest value, between 2 and a quarter of the data, to the parameter inputed has been used in the method.')
            n_neighbors = max(2, min(n_neighbors, len(self.data)//4))
            
        if min_dist == None:
            min_dist = 0.9
        else:
            if min_dist<0.0 or min_dist>0.99:
                print('min_dist controls how tightly UMAP is allowed to pack points together../n'+
                      'The value of min_dist can range from 0.0 up to 0.99. The inputed value is outside that range.\n'+
                      'Therefore the closest value between 0.0 and 0.99 to the parameter inputed has been used in the method.')
            min_dist = max(0.0, min(min_dist, 0.99))
            
        # Embed the data in two dimensions
        self.umap_fit = umap.UMAP(n_neighbors=n_neighbors, min_dist=min_dist, random_state=random_state, n_components=2)
        ecfp_umap_embedding = self.umap_fit.fit_transform(self.data)
        # Create a dataframe containinting the first 2 UMAP components of ECFP 
        self.df_2_components = pd.DataFrame(data = ecfp_umap_embedding
             , columns = ['UMAP-1', 'UMAP-2'])
        
        # Create a plot based on the TSNE model 
        umap_plot = self.construct_plot('UMAP-1', 'UMAP-2', size, kind, "UMAP plot", remove_outliers, is_colored, colorbar)
        return umap_plot
    
    
    def tmap():
        """
        Calculates and plots the TMAP based on ECFP fingerprints.
        
        :returns: plot object
        """
        pass

    
    def construct_plot(self, x, y, size, kind, title, remove_outliers, is_colored, colorbar):
        """
        Generates a plot for the given molecules embedded in two dimensions.
        
        :param df_2_components: The molecules to plot
        :type df_2_components: Dataframe
        :param x: The first column of the dataframe containing the molecules
        :type x: string
        :param y: The second column of the dataframe containing the molecules
        :type y: string
        :param size: Size of the plot
        :type size: int
        :param kind: Type of plot 
        :type kind: string
        :param title: Title of the plot
        :type title: string
        :param remove_outliers: Boolean value indicating if the outliers must be identified and removed 
        :type remove_outliers: boolean
        :param is_colored: Indicates if the points must be colored according to target 
        :type is_colored: boolean
        :returns: The matplotlib axes containing the plot.
        :rtype: Axes
        """
        
        if kind != 'scatter' and kind != 'hex' and kind != 'kde':
            kind = 'scatter'
            print('kind indicates which type of plot must be visualized. Currently supported visualization are:\n'+
                             '-scatter plot (scatter)\n'+
                             '-hexagon plot (hex)\n'+
                             '-kernel density estimation plot (kde)\n'+
                             'Please input one between scatter, hex or kde for parameter kind.\n'+
                             'As default scatter has been taken.')
            
        df_2_components = self.df_2_components
        
        # Define colors 
        hue = None
        palette = None
        if len(self.target) == 0:
            is_colored = False;
        else:
            if is_colored:
                df_2_components = df_2_components.assign(target=self.target)
                hue = 'target'
                if self.target_type == "R":
                    palette = sns.color_palette("inferno", as_cmap=True)
        
        # Remove outliers (using Z-score)
        if remove_outliers:
            z_scores = stats.zscore(df_2_components[[x,y]])
            abs_z_scores = np.abs(z_scores)
            filtered_entries = (abs_z_scores < 3).all(axis=1)
            df_2_components = df_2_components[filtered_entries]
            
        # Define plot looks parameters
        sns.set_style("dark")
        sns.set_context("notebook", font_scale=size*0.15)
        fig, ax = plt.subplots(figsize=(size,size))
        
        # Create a plot based on the PCA components 
        if kind == "scatter":
            plot = sns.scatterplot(x=x, y=y, hue=hue, palette=palette, data=df_2_components, s=80)
            plot.set_label("scatter")
            axis = plot
            # Add colorbar
            if self.target_type == "R" and colorbar:
                plot.get_legend().remove()
                norm = plt.Normalize(df_2_components['target'].min(), df_2_components['target'].max())
                cm = plt.cm.ScalarMappable(cmap="inferno", norm=norm)
                cm.set_array([])
                plot.figure.colorbar(cm)
        elif kind == "hex":
            plot = ax.hexbin(df_2_components[x], df_2_components[y], gridsize=40, cmap='Blues')
            fig.colorbar(plot, ax=ax)
            ax.set_label("hex")
            axis = ax
        elif kind == "kde":
            plot = sns.kdeplot(x=x, y=y, shade=True, data=df_2_components)
            plot.set_label("kde")
            axis = plot
             
        # Remove units from axis
        axis.set(yticks=[])
        axis.set(xticks=[])
        # Add labels
        axis.set_title(title,fontsize=size*2)
        axis.set_xlabel(x,fontsize=size*2)
        axis.set_ylabel(y,fontsize=size*2)
        
        #Do not stretch image
        #plot.axis('square')
        
        self.df_plot_xy = df_2_components[[x,y]]
        
        return axis