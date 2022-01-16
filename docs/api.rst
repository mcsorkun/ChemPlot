API documentation
=================

ChemPlot principal class is :class:`Plotter`. It receives a list of molecules 
as a parameter in order to then use different functions for plotting the data
in two dimensions. All the main functions of ChemPlot are part of the :class:`Plotter`.
There are however two more functions outside of :class:`Plotter`, which can be 
used to access the sample datasets.

.. currentmodule:: chemplot

chemplot.Plotter
----------------

.. autoclass:: Plotter

.. autofunction:: Plotter.from_smiles

.. autofunction:: Plotter.from_inchi

.. autofunction:: Plotter.pca

.. autofunction:: Plotter.tsne

.. autofunction:: Plotter.umap

.. autofunction:: Plotter.cluster

.. autofunction:: Plotter.visualize_plot

.. autofunction:: Plotter.interactive_plot

Utils
-----

.. autofunction:: load_data

.. autofunction:: info_data
    
    

