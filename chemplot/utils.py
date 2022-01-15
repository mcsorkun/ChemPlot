import pkg_resources
import pandas as pd


def load_data(name):
    """
    Returns one of the sample datasets.
    
    :param name: Name of the sample dataset
    :type name: string
    :returns: The Dataframe of the sample dataset
    :rtype: Dataframe
    """
    # This is a stream-like object. If you want the actual info, call
    # stream.read()
    stream = pkg_resources.resource_stream(__name__, f'data/{name}.csv')
    return pd.read_csv(stream)