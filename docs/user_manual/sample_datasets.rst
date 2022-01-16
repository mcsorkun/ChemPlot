Sample datasets
===============

ChemPlot provides some sample datasets that can be used to get started right away 
with exploring the libraries features. These datasets can be loaded with the following 
function:

.. code:: python3

    from chemplot import load_data
    
    df = load_data("BBBP")

In these case we are loading the BBBP dataset, used in the previous sections of this
manual. ``load_data()`` returns a pandas DataFrame built using the sample dataset
provided as a parameter.
Chemplot contains the following sample datasets:

.. list-table:: Title
   :header-rows: 1

   * - ID
     - Name
     - Type
     - Size
   * - C_1478_CLINTOX_2
     - Clintox (Toxicity)
     - Classification
     - 1478
   * - C_1513_BACE_2
     - BACE (Inhibitor)
     - Classification
     - 1513
   * - C_2039_BBBP_2
     - BBBP (Blood-brain barrier penetration)
     - Classification
     - 2039
   * - C_41127_HIV_3
     - HIV
     - Classification
     - 41127

   * - R_642_SAMPL
     - SAMPL (Hydration free energy)
     - Regression
     - 642
   * - R_1513_BACE
     - BACE (Binding affinity)
     - Regression
     - 1513
   * - R_4200_LOGP
     - LOGP (Lipophilicity)
     - Regression
     - 4200
   * - R_1291_LOGS
     - LOGS (Aqueous Solubility)
     - Regression
     - 1291
   * - R_9982_AQSOLDB
     - AQSOLDB (Aqueous Solubility)
     - Regression
     - 9982


--------------

.. raw:: html

   <h3>

References:

.. raw:: html

   </h3>