Development environment 
=======================

The development environment is an installation of ChemPlot on your local computer
which can be used for testing existing features or developing new ones in order 
to contribute to the library.

Prerequisites
-------------

Start by making sure you have the following installed on your system: 

- **Git**: `Download Git <https://git-scm.com/downloads>`_
- **Python** (version 3.8 or higher): `Download Python <https://www.python.org/downloads/>`_
- **Conda** (optional, if you choose the Conda setup): `Install Conda <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>`_

1. Clone the ChemPlot Repository
--------------------------------

First, clone your forked GitHub repository of `ChemPlot <https://github.com/mcsorkun/ChemPlot>`_ to your local machine using either HTTPS or SSH.

**Using HTTPS:**

.. code-block:: bash

    ~$ git clone https://github.com/<your-username>/ChemPlot.git

**Using SSH:**

.. code-block:: bash

    ~$ git clone git@github.com:<your-username>/ChemPlot.git

Navigate to the cloned repository:

.. code-block:: bash

    ~$ cd ChemPlot

2. Choose Your Environment Setup Method
----------------------------------------

You have two options to set up your development environment:

1. **Using Conda Environment**
2. **Using Python's Built-in Virtual Environment (`venv`)**

Choose the method that best fits your workflow.

Option 1: Using Conda Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Conda is recommended for managing more complex environments. 

.. code-block:: bash

    ~/<PATH-TO-CLONE>/ChemPlot$ conda create -n chemplot

When conda finishes creating the environment, activate it by running:

.. code-block:: bash

    ~/<PATH-TO-CLONE>/ChemPlot$ conda activate chemplot

Option 2: Using Python's Built-in Virtual Environment (`venv`)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you prefer not to use Conda, Python's built-in `venv` provides a lightweight alternative for creating isolated environments.

.. code-block:: bash

    ~/<PATH-TO-CLONE>/ChemPlot$ python -m venv venv

You can then activate the enviroment 

- **On Linux/macOS:**

.. code-block:: bash

    ~/<PATH-TO-CLONE>/ChemPlot$ source venv/bin/activate

- **On Windows:**

.. code-block:: bash

    ~/<PATH-TO-CLONE>/ChemPlot$ venv\Scripts\activate

3. Install ChemPlot for Development
-----------------------------------

You can now install ChemPlot in editable mode. Editable mode will allow your code
changes to be propagated through the library code without having to reinstall. 

.. code-block:: bash

    ~/<PATH-TO-CLONE>/ChemPlot$ pip install -e .

You are now ready to develop and test ChemPlot!

4. Testing
----------

To run the unit tests for ChemPlot use this command:

.. code-block:: bash
    
    ~$ pip install .[test]
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