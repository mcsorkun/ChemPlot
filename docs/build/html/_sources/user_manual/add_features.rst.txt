Additional Features
===================

ChemPlot offers additional features for chemical space visualization which can 
improve the understanding of the underlying similarities between the investigated
molecules. 

Using the ``Plotter`` object it is possible to create two different kind plots of 
the chemical space, aside from the scatterplots showed in the previous sections.
These plots investigate the density distribution of the chemical space an are 
hexagonal bin plot and the kernel density estimate plot.

To show the before mentioned features we will use the BBBP 
(blood-brain barrier penetration) dataset [1]_, already mentioned in the 
previous section: 

.. code:: python3

    import pandas as pd
    import chemplot as cp
    
    data_BBBP = pd.read_csv("BBBP.csv")
    cp_BBBP = cp.Plotter.from_smiles(data_BBBP["smiles"], target=data_BBBP["target"], target_type="C")
    
Hexagonal Bin Plot
------------------

In a hexagonal bin plot points are binned into hexagons, which in turn are 
coloured depending on the count of observations they cover. To create a 
hexagonal bin plot we need to pass the keyword “hex” as the ``kind`` 
parameter when calling one of the dimensionality reduction and plotting 
functions.  

.. code:: python3
    
    cp_BBBP.tsne(kind="hex", random_state=0)
    plt.show()

.. image:: images/tsne_hex.png
   :width: 600
   
   
Kernel Density Estimate Plot
----------------------------

In a kernel density estimate plot, the data distribution is visualized by a 
continuous probability density curve which in our case is in 2 dimensions. To 
create a kernel density estimate plot we need to pass the keyword “kde” as the 
``kind`` parameter when calling one of the dimensionality reduction and 
plotting functions.  

.. code:: python3
    
    cp_BBBP.tsne(kind="kde", random_state=0)
    plt.show()

.. image:: images/tsne_kde.png
   :width: 600
     
    
--------------

.. raw:: html

   <h3>

References:

.. raw:: html

    </h3>
    
.. [1] **Martins, Ines Filipa, et al.** (2012). `A Bayesian approach to in silico blood-brain barrier penetration modeling. <https://pubmed.ncbi.nlm.nih.gov/22612593/>`__ Journal of chemical information and modeling 52.6, 1686-1697
