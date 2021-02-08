ChemPlot
===========================================================

In the last decades, Machine Learning (ML) applications have had a great impact on molecular
and material science. However, every ML model requires a definition of its applicability domain.
Chemplot is a python library for chemical space visualization that allows users to plot the 
chemical space of their datasets. Chemplot contains smart algorithms behind which uses both 
structural and tailored similarity. Moreover, it is easy to use even for non-experts.

Installation
------------

There two different options you can follow to install ChemPlot.

Option 1: Use conda (recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The easiest and recommended way to install is using conda. 
To install ChemPlot, at the command line, run::

    conda install -rdkit -chemplot chemplot


Option 2: Use pip
~~~~~~~~~~~~~~~~~
ChemPlot requires RDKit, which cannot be installed using pip. The official RDKit installation documentation can be found `here`_.

After having installed RDKit, ChemPlot can be installed using pip by running::

    pip install chemplot
   
.. _`here`: http://www.rdkit.org/docs/Install.html

How to use ChemPlot
-------------------

ChemPlot is a cheminformatics tool whose purpose is to visualize subsets of the 
chemical space in two dimensions. It uses the `RDKit chemistry framework`_, the
`scikit-learn <http://scikit-learn.org/stable/index.html>`__ API and the `umap-learn <https://github.com/lmcinnes/umap>`__ API.


Getting started
~~~~~~~~~~~~~~~
To demonstrate how to use the functions the library offers we will use a BBBP 
(blood-brain barrier penetration) [1]_ molecular dataset. This is a set of 
molecules encoded as SMILES, which have been assigned a binary label according 
to their permeability properties. In this example the dataset has been 
previously saved locally as a CSV file and is imported with `pandas <https://pandas.pydata.org/pandas-docs/stable/index.html>`__. 
  
.. code:: python3

    import pandas as pd

    data_BBBP = pd.read_csv("BBBP.csv")

    
To visualize the molecules in 2D according to their similarity it is first 
needed to construct a ``Plotter`` object. This is the class containing 
all the functions ChemPlot uses to produce the desired visualizations. A 
``Plotter`` object can be constructed using classmethods, which differentiate 
between the type of input that is feed to the object. In our example we need to 
use the method from_smiles. We pass three parameters: the list of SMILES from 
the BBBP dataset, their target values (the binary labels) and the target type 
(in this case “C”, which stands for “Classification”).  

.. code:: python3

    import chemplot as cp
    
    plotter = cp.Plotter.from_smiles(data_BBBP["smiles"], target=data_BBBP["target"], target_type="C")

Plotting the results
~~~~~~~~~~~~~~~~~~~~

When the ``Plotter`` object was constructed descriptors for each SMILES were 
calculated, using the library `mordred <http://mordred-descriptor.github.io/documentation/v0.1.0/introduction.html>`__, 
and then selected based on the target values. We can now plot the BBBP dataset 
in 2D to visually analyze the data. This is done by reducing the number of 
dimensions for each molecule from the number of descriptors selected to only 2. 
ChemPlot uses three different algorithms in order to achieve this. 
The first figure shows the results obtained by reducing the dimensions of 
features by Principal Component Analysis (PCA) [2]_.

.. code:: python3

    import matplotlib.pyplot as plt
    
    cp.pca()
    plt.show()



The second figure shows the results obtained by reducing the dimensions of features by t-SNE [3]_.

.. code:: python3

    cp.pca()
    plt.show()



The third figure shows the results obtained by reducing the dimensions of features by UMAP [4]_.

.. code:: python3

    cp.pca()
    plt.show()



In each figure the molecules are coloured by class value. 


.. _`RDKit chemistry framework`: http://www.rdkit.org

--------------

.. raw:: html

   <h3>

References:

.. raw:: html

    </h3>
    
.. [1] **Martins, Ines Filipa, et al.** (2012). `A Bayesian approach to in silico blood-brain barrier penetration modeling. <https://pubmed.ncbi.nlm.nih.gov/22612593/>`__ Journal of chemical information and modeling 52.6, 1686-1697
.. [2] **Wold, S., Esbensen, K., Geladi, P.** (1987). `Principal component analysis. <https://www.sciencedirect.com/science/article/abs/pii/0169743987800849>`__ Chemometrics and intelligent laboratory systems. 2(1-3). 37-52.
.. [3] **van der Maaten, Laurens, Hinton, Geoffrey.** (2008). `Viualizingdata using t-SNE. <https://www.jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf?fbclid=IwAR0Bgg1eA5TFmqOZeCQXsIoL6PKrVXUFaskUKtg6yBhVXAFFvZA6yQiYx-M>`__ Journal of Machine Learning Research. 9. 2579-2605.
.. [4] **McInnes, L., Healy, J., Melville, J.** (2018). `Umap: Uniform manifold approximation and projection for dimension reduction. <https://arxiv.org/abs/1802.03426>`__ arXivpreprint arXiv:1802.03426.


