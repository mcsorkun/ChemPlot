
## numbering reference
## check the HTML hyperlinks
## citation paper also dim red methods (tsne umap)

How to use ChemPlot
===================

ChemPlot is a cheminformatics tool whose purpose is to visualize subsets of 
the chemical space in two dimensions. It uses the `RDKit chemistry framework`_ and the 
`scikit-learn <http://scikit-learn.org/stable/index.html>`__ API.


Getting started
---------------
In order to demonstrate how to use the functions the library offers we will 
use a BBBP (blood-brain barrier penetration) molecular dataset collected by Martins (2012). 
This is a set of molecules encoded as SMILES, which have been assigned a binary 
label according to their permeability properties. In this example the dataset 
has been previously saved locally as a csv file and is imported with pandas. 

.. code:: python3

    import pandas as pd
    

.. code:: python3

    data_BBBP = pd.read_csv("BBBP.csv")
    data_BBBP.head()

To visualize the molecules in 2D according to their similarity it is first needed 
to construct a Plotter object. The latter is the class containing all the functions 
ChemPlot uses to produce the desired visualizations. 
A Plotter object can be constructed using classmethods, 
which differentiate between the type of input that is feed to the object. 
In our example we need to use the method from_smiles. We pass three parameters: 
the list of SMILES from the BBBP dataset, their target values (the binary labels) 
and the target type (in this case “C”, which stands for “Classification”).  

.. code:: python3

    import chemplot as cp
    
    plotter = cp.Plotter.from_smiles(data_BBBP["smiles"], target=data_BBBP["target"], target_type="C")

Plotting the results
--------------------

When the Plotter object was constructed descriptors for each SMILES were 
calculated, using the library mordred, and then selected based on the target values. 
We can know plot the BBBP dataset in 2D in order to visually analyze the data. 
This is done by reducing the number dimensions for each molecule from the number 
of descriptors selected to only 2. ChemPlot uses three different algorithms in 
order to achieve the latter. 
The first figure shows the results obtained by reducing the dimensions of 
features by Principal Component Analysis (PCA).

.. code:: python3

    import matplotlib.pyplot as plt
    
    cp.pca()
    plt.show()
    
The second figure shows the results obtained by reducing the dimensions of features by t-SNE.

.. code:: python3

    cp.pca()
    plt.show()
    
The third figure shows the results obtained by reducing the dimensions of features by UMAP.

.. code:: python3

    cp.pca()
    plt.show()

In each figure the molecules are colored by class value. 

--------------

.. raw:: html

   <h3>

BBBP data information

.. raw:: html

   </h3>

BBBP data are from:

**Martins, Ines Filipa, et al.** `A Bayesian approach to in silico blood-brain 
barrier penetration modeling <https://pubmed.ncbi.nlm.nih.gov/22612593/>`__ 
Journal of chemical information and modeling 52.6 (2012): 1686-1697


.. _`RDKit chemistry framework`: http://www.rdkit.org

 


