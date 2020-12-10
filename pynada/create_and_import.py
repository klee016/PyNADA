from .commons import *


def add_survey(
        idno=None,
        repositoryid=None,
        access_policy=None,
        published=None,
        overwrite=None,
        doc_desc=None,
        study_desc=None,
        data_files=None,
        variables=None,
        variable_groups=None,
        additional=None
):
    """Add a new survey

    Parameters
    ----------
    idno : str
        Dataset IDNo
    repositoryid : str
        Collection ID that owns the survey
    access_policy : str
        Data access policy. Valid values - "open" "direct" "public" "licensed" "enclave" "remote" "other"
    published : int
        Set status for study - 0 = Draft, 1 = Published
    overwrite : str
        Overwrite if a study with the same ID already exists? Valid values "yes", "no"
    doc_desc : dict
        Document description
    study_desc : dict
        Study Description
    data_files : list of dict
        Data files
    variables : list of dict
        List of variables and metadata
    variable_groups : list of dict
        List of variable groups
    additional : dict
        Additional metadata

    Returns
    -------
    DataFrame
        Added dataset
    """
    data = {
        "repositoryid": repositoryid,
        "access_policy": access_policy,
        "published": published,
        "overwrite": overwrite,
        "doc_desc": doc_desc,
        "study_desc": study_desc,
        "data_files": data_files,
        "variables": variables,
        "variable_groups": variable_groups,
        "additional": additional
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/survey/'+idno, data)

    return response
    #return pd.DataFrame.from_dict(response['datasets']).set_index('id')


def add_document(
        idno=None,
        repositoryid=None,
        published=None,
        overwrite=None,
        metadata_information=None,
        document_description=None,
        tags=None,
        files=None
):
    """Add a new document

    Parameters
    ----------
    idno : str
        Dataset IDNo
    repositoryid : str
        Collection ID that owns the survey
    published : int
        Set status for study - 0 = Draft, 1 = Published
    overwrite : str
        Overwrite if a study with the same ID already exists? Valid values "yes", "no"
    metadata_information : dict
        Document metadata information
    document_description : dict
        Document Description
    tags : list of dict
        Tags
    files : list of dict
        Files

    Returns
    -------
    DataFrame
        Information on the added document
    """
    data = {
        "repositoryid": repositoryid,
        "published": published,
        "overwrite": overwrite,
        "metadata_information": metadata_information,
        "document_description": document_description,
        "tags": tags,
        "files": files
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/document/'+idno, data)

    return response
