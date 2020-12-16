from .commons import *
import sys
import pandas as pd


def list_collections():
    """Returns a list of all collections in the catalog

    Returns
    -------
    pd.DataFrame
        collection information
    """

    params = {}
    response = make_get_request('collections', params)

    return pd.DataFrame.from_dict(response, orient='index')


def get_collection_info(repositoryId):
    """Returns information on a collection

    Parameters
    ----------
    repositoryId : str
        Collection's unique IDNo

    Returns
    -------
    pd.DataFrame
        collection information
    """

    params = {}
    response = make_get_request('collections/'+repositoryId, params)

    #return response
    return pd.DataFrame.from_dict(response, orient='index')


def list_datasets():
    """Returns a list of all datasets in the catalog

    Returns
    -------
    pd.DataFrame
        dataset information
    """
    
    params = {}
    response = make_get_request('datasets', params)
 
    return pd.DataFrame.from_dict(response['datasets']).set_index('id')


def search_dataset_by_idno(partial_idno):
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


def search_dataset_by_title(partial_title):
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


def get_dataset_info(idno):
    """Returns information on a dataset

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

    #return response
    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def get_dataset_info_by_numid(numeric_id):
    """Returns information on single dataset

    Parameters
    ----------
    numeric_id : int
        Dataset numeric id

    Returns
    -------
    pd.DataFrame
        dataset information
    """

    params = {}
    response = make_get_request('datasets/find_by_id/'+numeric_id, params)

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def list_tags(idno):
    """Get a list of all tags for a dataset

    Parameters
    ----------
    idno : str
        Dataset IDNo

    Returns
    -------
    pd.DataFrame
        tags
    """

    params = {}
    response = make_get_request('datasets/tags/'+idno, params)

    return pd.DataFrame(response['records'])


def list_aliases(idno):
    """Get a list of all aliases for a dataset

    Parameters
    ----------
    idno : str
        Dataset IDNo

    Returns
    -------
    pd.DataFrame
        aliases
    """

    params = {}
    response = make_get_request('datasets/aliases/'+idno, params)

    return pd.DataFrame(response['records'])


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


def get_resource_info(datasetIDNo, resourceId):
    """Returns information on a resource

    Parameters
    ----------
    datasetIDNo : str
        Dataset IDNo
    resourceId : int
        Resource ID

    Returns
    -------
    pd.DataFrame
        resource information
    """

    params = {}
    response = make_get_request('datasets/'+datasetIDNo+'/resources/'+resourceId, params)

    #return response
    return pd.DataFrame.from_dict(response['resource'], orient='index')


def list_datafiles(idno):
    """Get a list of all data files for a survey

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


def list_variables(idno):
    """Get a list of variables for a dataset

    Parameters
    ----------
    idno : str
        Dataset IDNo

    Returns
    -------
    pd.DataFrame
        information on the variables
    """

    params = {}
    response = make_get_request('datasets/variables/'+idno, params)

    #return response
    return pd.DataFrame(response['variables'])


def list_variables_by_file(idno, file_id):
    """Get a list of variables for a dataset

    Parameters
    ----------
    idno : str
        Dataset IDNo
    file_id : str
        File ID

    Returns
    -------
    pd.DataFrame
        information on the variables
    """

    params = {}
    response = make_get_request('datasets/variables/'+idno+'/'+file_id, params)

    #return response
    return pd.DataFrame(response['variables'])


def get_variable_info(idno, var_id):
    """Returns information on a variable

    Parameters
    ----------
    idno : str
        Dataset IDNo
    var_id : str
        Variable ID IDNo

    Returns
    -------
    pd.DataFrame
        variable information
    """

    params = {}
    response = make_get_request('datasets/variable/'+idno+'/'+var_id, params)

    #return response
    return pd.DataFrame.from_dict(response['variable'], orient='index')


def list_citations():
    """list all citations

    Returns
    -------
    pd.DataFrame
        citation information
    """

    params = {}
    response = make_get_request('citations', params)
    return pd.DataFrame.from_dict(response['citations']).set_index('id')


def get_citation_info(uuid):
    """Returns information on a citation

    Parameters
    ----------
    uuid : str
        citation ID

    Returns
    -------
    pd.DataFrame
        citation information
    """

    params = {}
    response = make_get_request('citation/'+uuid, params)

    return response
    # return pd.DataFrame.from_dict(response['dataset']).set_index('id')


def search_citation_by_study(idno):
    """Returns a list of publications that cite the dataset

    Parameters
    ----------
    idno : str
        Dataset IDNo

    Returns
    -------
    pd.DataFrame
        citation information
    """

    params = {}
    response = make_get_request('citations/by_dataset/' + idno, params)

    return response
    # return pd.DataFrame.from_dict(response['dataset']).set_index('id')