from .commons import *
import pandas as pd


def list_all():
    """Returns a list of all datasets in the catalog

    Returns
    -------
    pd.DataFrame
        dataset information
    """
    
    params = {}
    response = make_get_request('datasets', params)
 
    return pd.DataFrame.from_dict(response['datasets']).set_index('id')


def filter_by_idno(partial_idno):
    """Returns a list of datasets whose idno contains a partial match

    Parameters
    ----------
    partial_idno : str
        Partial text of idno

    Returns
    -------
    pd.DataFrame
        dataset information
    """

    datasets = list_datasets()
    return datasets[datasets['idno'].str.contains(partial_idno)]


def filter_by_title(partial_title):
    """Returns a list of datasets whose title contains a partial match

    Parameters
    ----------
    partial_title : str
        Partial text of title

    Returns
    -------
    pd.DataFrame
        dataset information
    """

    datasets = list_datasets()
    return datasets[datasets['title'].str.contains(partial_title)]


def dataset_info(idno):
    """Returns information of a dataset

    Parameters
    ----------
    idno : str
        Dataset IDNo

    Returns
    -------
    pd.DataFrame
        dataset information
    """

    params = {}
    response = make_get_request('datasets/'+idno, params)

    return response
    # return pd.DataFrame.from_dict(response['dataset']).set_index('id')
