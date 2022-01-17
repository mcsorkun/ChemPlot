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

.. list-table:: 
   :header-rows: 1

   * - ID
     - Name
     - Type
     - Size
     - Reference
   * - C_1478_CLINTOX_2
     - Clintox (Toxicity)
     - Classification
     - 1478
     - [1]_ [2]_ [3]_ [4]_
   * - C_1513_BACE_2
     - BACE (Inhibitor)
     - Classification
     - 1513
     - [5]_
   * - C_2039_BBBP_2
     - BBBP (Blood-brain barrier penetration)
     - Classification
     - 2039
     - [6]_
   * - C_41127_HIV_3
     - HIV
     - Classification
     - 41127
     - [7]_
   * - R_642_SAMPL
     - SAMPL (Hydration free energy)
     - Regression
     - 642
     - [8]_
   * - R_1513_BACE
     - BACE (Binding affinity)
     - Regression
     - 1513
     - [5]_
   * - R_4200_LOGP
     - LOGP (Lipophilicity)
     - Regression
     - 4200
     - [9]_
   * - R_1291_LOGS
     - LOGS (Aqueous Solubility)
     - Regression
     - 1291
     - [10]_
   * - R_9982_AQSOLDB
     - AQSOLDB (Aqueous Solubility)
     - Regression
     - 9982
     - [11]_

The datasets ID are constructed in the following way:

**Name Formatting:** type_size_name_num_of_classes.csv

- **type:** R->Numerical and C->Categorical
- **size:** Number of instances in the dataset
- **name:** Name of dataset
- **num_of_classes:** Number of classes (Categorical only)

You can retrieve the datasets by passing their ID to ``load_data()``. 

.. note::

   The first 8 datasets in the table are edited versions of the MoleculeNet repository [12]_.

You can print the available sample datasets to console with ChemPlot using the following 
function:

.. code:: python3

    from chemplot import info_data
    
    df = info_data()

--------------

.. raw:: html

   <h3>

References:

.. raw:: html

   </h3>

.. [1] **Gayvert, Kaitlyn M., Neel S. Madhukar, and Olivier Elemento.** (2016) `A data-driven approach to predicting successes and failures of clinical trials.` Cell chemical biology 23.10 1294-1301.
.. [2] **Artemov, Artem V., et al.** (2016) `Integrated deep learned transcriptomic and structure-based predictor of clinical trials outcomes.` bioRxiv 095653.
.. [3] **Novick, Paul A., et al.** (2013) `SWEETLEAD: an in silico database of approved drugs, regulated chemicals, and herbal isolates for computer-aided drug discovery.` PloS one 8.11 e79568.
.. [4] `Aggregate Analysis of ClincalTrials.gov (AACT) Database. <https://www.ctti-clinicaltrials.org/aact-database>`_
.. [5] **Subramanian, Govindan, et al.** (2016) `Computational modeling of β-secretase 1 (BACE-1) inhibitors using ligand based approaches.` Journal of chemical information and modeling 56.10 1936-1949.
.. [6] **Martins, Ines Filipa, et al.** (2014) `A Bayesian approach to in silico blood-brain barrier penetration modeling.` Journal of chemical information and modeling 52.6 (2012): 1686-1697.
.. [7] `AIDS Antiviral Screen Data. <https://wiki.nci.nih.gov/display/NCIDTPdata/AIDS+Antiviral+Screen+Data>`_
.. [8] **Mobley, David L., and J. Peter Guthrie.** `FreeSolv: a database of experimental and calculated hydration free energies, with input files.` Journal of computer-aided molecular design 28.7 711-720.
.. [9] **Hersey, A.** (2015) `ChEMBL Deposited Data Set - AZ dataset <https://doi.org/10.6019/chembl3301361>`_
.. [10] **Huuskonen, J.** (2000) `Estimation of aqueous solubility for a diverse set of organic compounds based on molecular topology.` Journal of Chemical Information and Computer Sciences, 40(3), 773-777.
.. [11] **Sorkun, M. C., Khetan, A., & Er, S.** (2019) `AqSolDB, a curated reference set of aqueous solubility and 2D descriptors for a diverse set of compounds.` Scientific data, 6(1), 1-8.
.. [12] **Wu, Zhenqin, et al.** (2018) `MoleculeNet: a benchmark for molecular machine learning.` Chemical science 9.2 513-530.