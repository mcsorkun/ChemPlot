Installation
============

Installing an official release
------------------------------

There two different options you can follow to install ChemPlot.

Option 1: Use conda
^^^^^^^^^^^^^^^^^^^

You can install ChemPlot using conda. 
To install ChemPlot, at the command line, run::

    conda install -c conda-forge -c chemplot chemplot
    
Option 2: Use pip
^^^^^^^^^^^^^^^^^

An alternative method is to install is using pip::

    pip install chemplot

.. note::

   ChemPlot requires RDKit, which cannot be installed using pip. The official RDKit documentation 
   contains `installation instructions for multiple platforms`_.

Verify Installation
^^^^^^^^^^^^^^^^^^^

You can verify that ChemPlot was installed on your local computer by running:

.. code-block:: bash

    ~$ pip show chemplot
    Name: chemplot
    ...

If instead of what shown above your output is:

.. code-block:: bash

    WARNING: Package(s) not found: chemplot

ChemPlot was not installed correctly or your system cannot find the path to it. 

If ChemPlot is installed correctly you can also test the package by running:

.. code-block:: bash

    ~$ pytest --pyargs chemplot

These will run all the library tests against your installation. For every official 
release from **1.2.0** you can use this command to verify that every function of
your local installation of ChemPlot works as expected.  

Development environment 
-----------------------

The development environment is an installation of ChemPlot on your local computer
which can be used for testing existing features or developing new ones in order 
to contribute to the library.

Start by making sure you have `conda installed <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>`_. 
This is needed since an important dependency of ChemPlot is `RDKit <http://www.rdkit.org/docs>`_, 
which can safely be installed only with conda. 

Then clone your forked GitHub repository of `ChemPlot <https://github.com/mcsorkun/ChemPlot>`_ on your local computer using 
either HTTPS:

.. code-block:: bash

    ~$ git clone https://github.com/<your-username>/ChemPlot.git

Or using SSH:

.. code-block:: bash

    ~$ git clone git@github.com:<your-username>/ChemPlot.git

Then from the terminal navigate to the ChemPlot repository you just created. From
there create a new conda environment with all the dependencies needed to work with 
ChemPlot. Create the environment by running:

.. code-block:: bash

    ~/<PATH-TO-CLONE>/ChemPlot$ conda env create -f requirements_conda.yml

When conda finishes creating the environment, activate it by running:

.. code-block:: bash

    ~/<PATH-TO-CLONE>/ChemPlot$ conda activate chemplot_env

You can now install ChemPlot in editable mode. Editable mode will allow your code
changes to be propagated through the library code without having to reinstall. 

.. code-block:: bash

    ~/<PATH-TO-CLONE>/ChemPlot$ pip install -e .

You are now ready to develop ChemPlot!

Testing 
-------

To run the unit tests for ChemPlot use this command:

.. code-block:: bash

    ~$ pytest --pyargs chemplot

.. code-block:: bash
.. _`installation instructions for multiple platforms`: http://www.rdkit.org/docs/Install.html

    

