Installation
============

Installing an official release
------------------------------

There two different options you can follow to install ChemPlot.

Option 1: Use conda
^^^^^^^^^^^^^^^^^^^

You can install ChemPlot using conda. 
To install ChemPlot, at the command line, run::

    ~$ conda install -c conda-forge -c chemplot chemplot
    
Option 2: Use pip
^^^^^^^^^^^^^^^^^

An alternative method is to install is using pip::

    ~$ pip install chemplot

.. note::

   ChemPlot requires RDKit, which cannot be installed using pip. The official RDKit documentation 
   contains `installation instructions for multiple platforms`_.

Verify Installation
-------------------

You can verify that ChemPlot was installed on your local computer by running:

.. code-block:: bash

    ~$ pip show chemplot
    >>> Name: chemplot
    >>> ...

If instead of what is shown above your output is:

.. code-block:: bash

    >>> WARNING: Package(s) not found: chemplot

ChemPlot was not installed correctly or your system cannot find the path to it. 
If ChemPlot is installed correctly you can also test the package by running:

.. code-block:: bash

    ~$ python -m pytest --pyargs chemplot

These will run all the library tests against your installation. For every official 
release from **1.2.0** you can use this command to verify that every function of
your local installation of ChemPlot works as expected.  

.. _`installation instructions for multiple platforms`: http://www.rdkit.org/docs/Install.html

    

