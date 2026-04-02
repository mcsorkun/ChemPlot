# Authors: Murat Cihan Sorkun <mcsorkun@gmail.com>, Dajt Mullaj <dajt.mullai@gmail.com>, Jackson Warner Burns <jwburns@mit.edu>
#
# License: BSD 3 clause
import re
import sys
from importlib.resources import files

import pandas as pd

from chemplot.parameters import INFO_DATASET, SAMPLE_DATASETS


def load_data(name):
    """
    Returns one of the sample datasets using modern importlib.resources.
    """
    name = _select_dataset(name)
    source = files('chemplot').joinpath(f"data/{name}.csv")
    with source.open("rb") as stream:
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
