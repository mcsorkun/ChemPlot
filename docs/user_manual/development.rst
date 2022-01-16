Development environment 
=======================

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

    ~$ python -m pytest --pyargs chemplot


On your cloned version of the ChemPlot repository you have two more tests, used
to check performance of the library on your machine and to check the figures 
ChemPlot can generate. You can find these tests inside the performance_tests folder:

::

    ChemPlot
    ├── ...
    ├── performance_tests/          
    │   ├── performanceTest.py
    │   └── visualplotsTest.py
    └── ...

You can run these tests by navigating to the performance_test library:

.. code-block:: bash

    ~/ChemPlot$ cd performance_tests
    ~/ChemPlot/performance_tests$ python performanceTest.py
    ~/ChemPlot/performance_tests$ python visualplotsTest.py

If it doesn't work you might have to change ``python`` with ``python3`` in the command.
``performanceTest.py`` will generate a ``.csv`` file containing all the times taken 
by ChemPlot to run all the dimensionality reduction methods on your machine. It will
use the sample datasets provided with the library. ``visualplotsTest.py`` will instead
create a multipage ``.pdf`` file containing different figures illustrating all plotting
options for ChemPlot. These method as well will use the sample datasets included in 
the library. 