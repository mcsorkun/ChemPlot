# Authors: Murat Cihan Sorkun <mcsorkun@gmail.com>, Dajt Mullaj <dajt.mullai@gmail.com>, Jackson Warner Burns <jwburns@mit.edu>
#
# License: BSD 3 clause
import re

import pandas as pd
import importlib.resources

from chemplot.parameters import INFO_DATASET, SAMPLE_DATASETS


def _resource_stream(package, resource):
    """
    Helper function to deal with pkg_resources v81 resource_stream deprecation
    
    See: https://github.com/mcsorkun/ChemPlot/issues/33

    :param package: Name of the package where the resource file is located
    :type package: string
    :param resource: Name of the resource file
    :type resource: string
    :returns: A file-like object for the resource
    :rtype: file-like object
    """
    return importlib.resources.open_binary(package, resource)


def load_data(name):
    """
    Returns one of the sample datasets.

    :param name: Name of the sample dataset
    :type name: string
    :returns: The Dataframe of the sample dataset
    :rtype: Dataframe
    """

    name = _select_dataset(name)

    stream = _resource_stream(__name__, f"data/{name}.csv")
    return pd.read_csv(stream)


def _select_dataset(name):
    """
    Returns one of the sample datasets.

    :param name: A version of the name of the sample dataset
    :type name: string
    :returns: The name of the sample dataset file
    :rtype: string
    """

    for key, values in SAMPLE_DATASETS.items():
        if name in values:
            return key

    raise Exception(f'"{name}" cannot be found in the sample datasets')


def info_data():
    """
    Prints the metadata relative to the available sample datasets.
    """

    print(INFO_DATASET)
