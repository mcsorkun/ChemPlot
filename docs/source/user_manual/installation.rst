Installation
============

There two different options you can follow to install ChemPlot.

Option 1: Use conda (recommended)
---------------------------------

The easiest and recommended way to install is using conda. 
To install ChemPlot, at the command line, run::

    conda install -rdkit -chemplot chemplot


Option 2: Use pip
-----------------

An alternative method is to install using pip::

    pip install chemplot

.. note::

   ChemPlot requires RDKit, which cannot be installed using pip. On the Mac, you can use Homebrew::

       brew tap mcs07/cheminformatics
       brew install rdkit

   The official RDKit documentation has `installation instructions for a variety of platforms`_.
   
   
.. _`installation instructions for a variety of platforms`: http://www.rdkit.org/docs/Install.html
