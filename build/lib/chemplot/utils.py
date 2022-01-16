# Authors: Murat Cihan Sorkun <mcsorkun@gmail.com>, Dajt Mullaj <dajt.mullai@gmail.com>
#
# License: BSD 3 clause 
import pkg_resources
import pandas as pd
import re

from chemplot.parameters import SAMPLE_DATASETS, INFO_DATASET

def load_data(name):
    """
    Returns one of the sample datasets.
    
    :param name: Name of the sample dataset
    :type name: string
    :returns: The Dataframe of the sample dataset
    :rtype: Dataframe
    """

    name = _select_dataset(name)

    stream = pkg_resources.resource_stream(__name__, f'data/{name}.csv')
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