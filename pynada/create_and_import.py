from .manage_and_update import *


def add_survey_dataset(
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
    """Add a new survey dataset to the catalog

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

    assert idno == study_desc["title_statement"]["idno"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/survey/'+idno, data)

    return response
    #return pd.DataFrame.from_dict(response['datasets']).set_index('id')


def add_document_dataset(
        idno=None,
        repositoryid=None,
        published=None,
        overwrite=None,
        metadata_information=None,
        document_description=None,
        tags=None,
        files=None
):
    """Add a new document dataset to the catalog

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

    assert idno == document_description["title_statement"]["idno"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/document/'+idno, data)

    return response


def add_image_dataset(
        idno=None,
        repositoryid=None,
        published=None,
        overwrite=None,
        metadata_information=None,
        image_description=None
):
    """Add a new image dataset to the catalog using the IPTC Photo Metadata Standard 2017

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
    image_description : dict
        Image Description

    Returns
    -------
    DataFrame
        Information on the added image
    """
    data = {
        "repositoryid": repositoryid,
        "published": published,
        "overwrite": overwrite,
        "metadata_information": metadata_information,
        "image_description": image_description
    }

    assert idno == image_description["iptc"]["photoVideoMetadataIPTC"]["digitalImageGuid"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/image/'+idno, data)

    return response


def add_script_dataset(
        idno=None,
        repositoryid=None,
        published=None,
        overwrite=None,
        doc_desc=None,
        project_desc=None
):
    """Add a new script dataset to the catalog

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
    doc_desc : dict
        Script metadata information
    project_desc : dict
        Description of the research project

    Returns
    -------
    DataFrame
        Information on the added script dataset
    """
    data = {
        "repositoryid": repositoryid,
        "published": published,
        "overwrite": overwrite,
        "doc_desc": doc_desc,
        "project_desc": project_desc
    }

    assert idno == project_desc["title_statement"]["idno"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/script/'+idno, data)

    return response


def add_table_dataset(
        idno=None,
        repositoryid=None,
        published=None,
        overwrite=None,
        metadata_information=None,
        table_description=None,
        files=None,
        tags=None,
        additional=None
):
    """Add a new table dataset to the catalog

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
        Table metadata information
    table_description : dict
        Description of the table
    files : list of dict
        Table files
    tags : list of dict
        Tags
    additional : dict
        Additional metadata

    Returns
    -------
    DataFrame
        Information on the added table dataset
    """
    data = {
        "repositoryid": repositoryid,
        "published": published,
        "overwrite": overwrite,
        "metadata_information": metadata_information,
        "table_description": table_description,
        "files": files,
        "tags": tags,
        "additional": additional
    }

    assert idno == table_description["title_statement"]["idno"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/table/'+idno, data)

    return response


def add_visualization_dataset(
        idno=None,
        repositoryid=None,
        published=None,
        overwrite=None,
        metadata_information=None,
        visualization_description=None,
        files=None,
        additional=None
):
    """Add a new visualization dataset to the catalog

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
        Visualization metadata
    visualization_description : dict
        Description of the visualization
    files : list of dict
        Table files
    additional : dict
        Additional metadata

    Returns
    -------
    DataFrame
        Information on the added visualization dataset
    """
    data = {
        "repositoryid": repositoryid,
        "published": published,
        "overwrite": overwrite,
        "metadata_information": metadata_information,
        "visualization_description": visualization_description,
        "files": files,
        "additional": additional
    }

    assert idno == visualization_description["title_statement"]["idno"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/visualization/'+idno, data)

    return response