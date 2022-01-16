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

    .. automethod:: from_smiles

    .. automethod:: from_inchi

    .. automethod:: pca

    .. automethod:: tsne

    .. automethod:: umap

    .. automethod:: cluster

    .. automethod:: visualize_plot

    .. automethod:: interactive_plot

Utils
-----

.. autofunction:: load_data

.. autofunction:: info_data
    
    

