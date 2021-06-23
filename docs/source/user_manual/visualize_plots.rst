Visualize the Chemical Space
============================

ChemPlot can generate two types of plots for a given chemical space: static and
interactive.

For the following examples we will use the BBBP (blood-brain barrier penetration) 
dataset [1]_.. 

.. code:: python3

    import pandas as pd
    import chemplot
    
    data = pd.read_csv("BBBP.csv")
    cp = chemplot.Plotter.from_smiles(data["smiles"], target=data["target"], target_type="C")


Static Plot
-----------

To generate a static plot first reduce the dimensions of the molecules used to
initialize the :class:`Plotter` instance. Then you can use :mod:`visualize_plot()`
to generate a static visualization of the chemical space. 

.. code:: python3
    
    import matplotlib.pyplot as plt
    
    cp.tsne()
    cp.visualize_plot()
    plt.show()

.. image:: images/gs_tsne.png
   :width: 600
   
   
Interactive Plot
----------------

To generate an interactive plot first reduce the dimensions of the molecules used to
initialize the :class:`Plotter` instance. Then you can use :mod:`interactive_plot()`
to generate an interactive visualization of the chemical space. 

.. code:: python3
    
    cp.tsne()
    cp.interactive_plot()
    plt.show()

.. raw:: html
    :file: BBBP.html
    
.. raw:: html   

    <h3> 
    
.. raw:: html

    </h3>
    
    
The interactive plot is generated using the library `bokeh <https://bokeh.org/>`__. 
You can interact with it by using the toolbar displayed on the top right of the 
visualization. You can navigate across the plot, select group of molecules, 
zoom in and out the visualization and save the plot as an image. Furthermore you
can hover over the molecules to see their 2D image.

--------------

.. raw:: html

   <h3>

References:

.. raw:: html

   </h3>

.. [1] **Martins, Ines Filipa, et al.** (2012). `A Bayesian approach to in silico blood-brain barrier penetration modeling. <https://pubmed.ncbi.nlm.nih.gov/22612593/>`__ Journal of chemical information and modeling 52.6, 1686-1697
