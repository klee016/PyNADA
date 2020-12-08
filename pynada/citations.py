from .commons import *
import requests
import pandas as pd


def list_citations():
    """
    Returns a list of citations
    Returns: list of citations
    """
    
    params = {}
    response = make_get_request('citations', params)
    return pd.DataFrame.from_dict(response['citations']).set_index('id')


def citation_info(uuid):
    """
    returns a single citation by UUID
    Returns: Single citation by UUID
    """
    
    params = {}
    response = make_get_request('citations/' + uuid, params)
 
    return response