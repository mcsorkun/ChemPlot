Clustering Data
===============

ChemPlot allows you to identify different clusters in you data by making use of
the KMeans [1]_ algorithm as implemented in `sklearn <https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html>`_.
To illustrate its implementation in ChemPlot we will load the LOGP dataset [2]_,
a dataset about Lipophilicity with continuos targets. Let's load the sample 
dataset and create a ``Plotter`` object.

.. code:: python3

    from chemplot import Plotter, load_data
    
    data = load_data("LOGP")
    cp = Plotter.from_smiles(data["smiles"], target=data["target"], target_type="R")

Let's then reduce the dimensions of the molecular descriptors.

.. code:: python3

    cp.umap(random_state=500)

Now that the dimensions are reduced we can plot the image as shown in the previous 
chapters. We can also, however, identify some clusters in the data by calling this function:

.. code:: python3

    cp.cluster()

``cluster()`` will identify the clusters in our reduced dataset by using KMeans. The 
function takes one parameter ``n_clusters``, identifying the number of clusters we want 
to see. By default ``n_clusters`` is 5. 
Once we clustered the data we can call ``visualize_plot(clusters=True)`` to see the 
plot. Notice how we need to pass a parameter ``clusters`` set to ``True`` in order to 
see the clusters in the resulting image. 

.. code:: python3

    cp.visualize_plot(clusters=True)

.. image:: images/cluster_all.png
   :width: 600

We can however also select a number of clusters we want to highlight. The parameter
``clusters`` in ``visualize_plot()`` can indeed also be a ``list`` of integers or an ``int``
itself. An integer represents one of the clusters identified in the previous steps.
ChemPlot will either read the list or the single number passed as a parameter
and highlight those clusters as selected.

.. code:: python3

    cp.visualize_plot(clusters=0)

.. image:: images/cluster_0.png
   :width: 600

.. code:: python3

    cp.visualize_plot(clusters=[1,2,3])

.. image:: images/cluster_list.png
   :width: 600

We can also use ``interactive_plot()`` to visualize the clusters. In these case pass 
``clusters=True`` to generate a `bokeh <https://bokeh.org/>`__ plot with two tabs. The first tab will contain 
the plot that would have been generated also without clustering. The second tab 
will contain a plot showing the different clusters. Click on the elements of the 
legend to mute a cluster's data points.

.. code:: python3

    cp.interactive_plot(clusters=True)

.. raw:: html
    :file: LOGP.html
    
.. raw:: html   

    <h3> 
    
.. raw:: html

    </h3>

--------------

.. raw:: html

   <h3>

References:

.. raw:: html

   </h3>

.. [1] **Lloyd, Stuart P.** (1982). `Least square quantization in PCM. <https://www.sciencedirect.com/science/article/abs/pii/0169743987800849>`__ IEEE Transactions on Information Theory. 28 (2): 129–137.
.. [2] **Hersey, A.** (2015) `ChEMBL Deposited Data Set - AZ dataset <https://doi.org/10.6019/chembl3301361>`_