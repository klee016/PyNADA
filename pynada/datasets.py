from .commons import *
import requests
import pandas as pd


def list_datasets():
    """
    returns a list of all datasets in the FCV catalog
    Returns: list of datasets
    """
    
    params = {}
    response = make_get_request('datasets', params)
 
    return pd.DataFrame.from_dict(response['datasets']).set_index('id')