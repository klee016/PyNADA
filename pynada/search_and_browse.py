from .commons import *
import pandas as pd


def list_all_datasets():
    """Returns a list of all datasets in the catalog

    Returns
    -------
    pd.DataFrame
        dataset information
    """
    
    params = {}
    response = make_get_request('datasets', params)
 
    return pd.DataFrame.from_dict(response['datasets']).set_index('id')


def search_by_idno(partial_idno):
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

    datasets = list_all_datasets()
    return datasets[datasets['idno'].str.contains(partial_idno)]


def search_by_title(partial_title):
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

    datasets = list_all_datasets()
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


def list_resources(idno):
    """Get a list of all external resources for a dataset

    Parameters
    ----------
    idno : str
        Dataset IDNo

    Returns
    -------
    pd.DataFrame
        resources information
    """

    params = {}
    response = make_get_request('datasets/'+idno+'/resources', params)

    return response
    #return pd.DataFrame.from_dict(response['resources']).set_index('resource_id')


def list_datafiles(idno):
    """Get a list of all data files for a dataset

    Parameters
    ----------
    idno : str
        Dataset IDNo

    Returns
    -------
    pd.DataFrame
        information on the associated data files
    """

    params = {}
    response = make_get_request('datasets/datafiles/'+idno, params)

    return response
    #return pd.DataFrame.from_dict(response['resources']).set_index('resource_id')



def list_files(idno):
    """Get a list of all files for a dataset

    Parameters
    ----------
    idno : str
        Dataset IDNo

    Returns
    -------
    pd.DataFrame
        information on the associated files
    """

    params = {}
    response = make_get_request('datasets/'+idno+'/files/', params)

    #return response
    return pd.DataFrame.from_dict(response['files'])