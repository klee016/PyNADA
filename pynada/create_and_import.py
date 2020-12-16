from .manage_and_update import *


def create_collection(
        repository_id
):
    """Create new collection
    
    Parameters
    ----------
    repository_id : str
        Collection's unique IDNo
    """

    data = {}

    response = make_post_request('collections/' + repository_id, data)

    if response['status'] == 'success':
        print("Collection successfully created!")

    return pd.DataFrame.from_dict(response, orient='index')


def add_survey_dataset(
        dataset_id=None,
        repository_id=None,
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
    dataset_id : str
        Dataset IDNo
    repository_id : str
        Collection ID that owns the survey dataset
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
        Any other custom metadata not covered by the schema

    Returns
    -------
    DataFrame
        Added dataset
    """

    data = {
        "repositoryid": repository_id,
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

    assert dataset_id == study_desc["title_statement"]["idno"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/survey/'+dataset_id, data)

    if response['status'] == 'success':
        print("Survey dataset successfully added!")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def add_document_dataset(
        dataset_id=None,
        repository_id=None,
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
    dataset_id : str
        Dataset IDNo
    repository_id : str
        Collection ID that owns the document dataset
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
        "repositoryid": repository_id,
        "published": published,
        "overwrite": overwrite,
        "metadata_information": metadata_information,
        "document_description": document_description,
        "tags": tags,
        "files": files
    }

    assert dataset_id == document_description["title_statement"]["idno"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/document/'+dataset_id, data)

    if response['status'] == 'success':
        print("Document dataset successfully added.")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def add_image_dataset(
        dataset_id=None,
        repository_id=None,
        published=None,
        overwrite=None,
        metadata_information=None,
        image_description=None
):
    """Add a new image dataset to the catalog using the IPTC Photo Metadata Standard 2017

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    repository_id : str
        Collection ID that owns the image dataset
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
        "repositoryid": repository_id,
        "published": published,
        "overwrite": overwrite,
        "metadata_information": metadata_information,
        "image_description": image_description
    }

    assert dataset_id == image_description["iptc"]["photoVideoMetadataIPTC"]["digitalImageGuid"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/image/'+dataset_id, data)

    if response['status'] == 'success':
        print("Image dataset successfully added!")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def add_script_dataset(
        dataset_id=None,
        repository_id=None,
        published=None,
        overwrite=None,
        doc_desc=None,
        project_desc=None
):
    """Add a new script dataset to the catalog

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    repository_id : str
        Collection ID that owns the script dataset
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
        "repositoryid": repository_id,
        "published": published,
        "overwrite": overwrite,
        "doc_desc": doc_desc,
        "project_desc": project_desc
    }

    assert dataset_id == project_desc["title_statement"]["idno"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/script/'+dataset_id, data)

    if response['status'] == 'success':
        print("Script dataset successfully added!")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def add_table_dataset(
        dataset_id=None,
        repository_id=None,
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
    dataset_id : str
        Dataset IDNo
    repository_id : str
        Collection ID that owns the table dataset
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
        Any other custom metadata not covered by the schema

    Returns
    -------
    DataFrame
        Information on the added table dataset
    """

    data = {
        "repositoryid": repository_id,
        "published": published,
        "overwrite": overwrite,
        "metadata_information": metadata_information,
        "table_description": table_description,
        "files": files,
        "tags": tags,
        "additional": additional
    }

    assert dataset_id == table_description["title_statement"]["idno"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/table/'+dataset_id, data)

    if response['status'] == 'success':
        print("Table dataset successfully added!")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def add_visualization_dataset(
        dataset_id=None,
        repository_id=None,
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
    dataset_id : str
        Dataset IDNo
    repository_id : str
        Collection ID that owns the visualization dataset
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
        Any other custom metadata not covered by the schema

    Returns
    -------
    DataFrame
        Information on the added visualization dataset
    """

    data = {
        "repositoryid": repository_id,
        "published": published,
        "overwrite": overwrite,
        "metadata_information": metadata_information,
        "visualization_description": visualization_description,
        "files": files,
        "additional": additional
    }

    assert dataset_id == visualization_description["title_statement"]["idno"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/visualization/'+dataset_id, data)

    if response['status'] == 'success':
        print("Visualization dataset successfully added!")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def add_geospatial_dataset(
        dataset_id=None,
        repository_id=None,
        published=None,
        overwrite=None,
        metadata_maintenance=None,
        dataset_description=None,
        additional=None
):
    """Add a new geospatial dataset to the catalog

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    repository_id : str
        Collection ID that owns the geospatial dataset
    published : int
        Set status for study - 0 = Draft, 1 = Published
    overwrite : str
        Overwrite if a study with the same ID already exists? Valid values "yes", "no"
    metadata_maintenance : dict
        Metadata information for the geospatial dataset
    dataset_description : dict
        Description of the geospatial dataset
    additional : dict
        Any other custom metadata not covered by the schema

    Returns
    -------
    DataFrame
        Information on the added geospatial dataset
    """

    data = {
        "repositoryid": repository_id,
        "published": published,
        "overwrite": overwrite,
        "metadata_maintenance": metadata_maintenance,
        "dataset_description": dataset_description,
        "additional": additional
    }

    assert dataset_id == dataset_description["file_identifier"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/geospatial/'+dataset_id, data)

    if response['status'] == 'success':
        print("Geospatial dataset successfully added!")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def add_timeseries_dataset(
        dataset_id=None,
        repository_id=None,
        access_policy=None,
        data_remote_url=None,
        published=None,
        overwrite=None,
        metadata_creation=None,
        series_description=None,
        additional=None
):
    """Add a new timeseries dataset to the catalog

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    repository_id : str
        Collection that owns the timeseries dataset
    access_policy : str
        Data access policy. Valid values - "direct" "open" "public" "licensed" "remote" "na"
    data_remote_url: str
        Link to the website where the data is available, this is only needed if access_policy is set to "remote"
    published : int
        Set status for study - 0 = Draft, 1 = Published
    overwrite : str
        Overwrite if a study with the same ID already exists? Valid values "yes", "no"
    metadata_creation : dict
        Information on who generated the documentation
    series_description : dict
        Description on the timeseries dataset
    additional : dict
        Any other custom metadata not covered by the schema

    Returns
    -------
    DataFrame
        Information on the added timeseries dataset
    """

    data = {
        "repositoryid": repository_id,
        "access_policy": access_policy,
        "data_remote_url": data_remote_url,
        "published": published,
        "overwrite": overwrite,
        "metadata_creation": metadata_creation,
        "series_description": series_description,
        "additional": additional
    }

    assert dataset_id == series_description["idno"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/timeseries/'+dataset_id, data)

    if response['status'] == 'success':
        print("Timeseries dataset successfully added!")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def add_timeseries_database(
        dataset_id=None,
        repository_id=None,
        published=None,
        overwrite=None,
        database_description=None,
        additional=None
):
    """Add a new timeseries database to the catalog

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    repository_id : str
        Collection that owns the timeseries dataset
    access_policy : str
        Data access policy. Valid values - "direct" "open" "public" "licensed" "remote" "na"
    data_remote_url: str
        Link to the website where the data is available, this is only needed if access_policy is set to "remote"
    published : int
        Set status for study - 0 = Draft, 1 = Published
    overwrite : str
        Overwrite if a study with the same ID already exists? Valid values "yes", "no"
    metadata_creation : dict
        Information on who generated the documentation
    series_description : dict
        Description on the timeseries dataset
    additional : dict
        Any other custom metadata not covered by the schema

    Returns
    -------
    DataFrame
        Information on the added timeseries dataset
    """

    data = {
        "repositoryid": repository_id,
        "access_policy": access_policy,
        "data_remote_url": data_remote_url,
        "published": published,
        "overwrite": overwrite,
        "metadata_creation": metadata_creation,
        "series_description": series_description,
        "additional": additional
    }

    assert dataset_id == series_description["idno"]

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/timeseries/'+dataset_id, data)

    if response['status'] == 'success':
        print("Timeseries database successfully added!")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def add_survey_dataset_by_importing_DDI(
        file=None,
        overwrite=None,
        repository_id=None,
        access_policy=None,
        data_remote_url=None,
        rdf=None,
        published=None
):
    """Add a new survey dataset to the catalog

    Parameters
    ----------
    file : str
        DDI XML file path or URL pointing to the XML file
    overwrite : str
        Valid values: "yes" "no"
    repository_id : str
        Collection identifier where the survey will be added to
    access_policy : str
        Valid values: "open" "direct" "public" "licensed" "enclave" "remote" "other"
    data_remote_url : str
        Link to the website for 'Data available from external repository' section
    rdf : str
        RDF file path or URL to the file
    published : int
        0=draft, 1=published
    """

    if validators.url(file):
        print("You provided a URL for the DDI XML. Processing...")
    elif os.path.exists(file):
        print("You provided a file for the DDI XML. Processing...")
        file = {'file': open(file, 'rb')}
    else:
        raise Exception("The DDI XML file you provided doesn't seem to be a valid file path or URL." 
                        "If it is a file, please check the path."
                        "If it is a URL, make sure to add a proper prefix such as http://")

    if rdf is not None:
        if validator.url(rdf):
            print("You provided a URL for the RDF. Processing...")
        elif os.path.exists(rdf):
            print("You provided a file for the RDF. Processing...")
            rdf = {'file': open(rdf, 'rb')}
        else:
            raise Exception("The RDF file you provided doesn't seem to be a valid file path or URL."
                            "If it is a file, please check the path."
                            "If it is a URL, make sure to add a proper prefix such as http://")

    data = {
        "file": file,
        "overwrite": overwrite,
        "repositoryid": repository_id,
        "access_policy": access_policy,
        "data_remote_url": data_remote_url,
        "rdf": rdf,
        "published": published
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/import_ddi', data)

    return response
    #return pd.DataFrame.from_dict(response['datasets']).set_index('id')


def add_resource_by_importing_RDF(
        dataset_id=None,
        file=None
):
    """Import an RDF file to batch import external resoruces

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    file : str
        Dublin core RDF file (rdf, xml)
    """

    if os.path.exists(file):
        print("You provided a file for Dublin core RDF. Processing...")
        file = {'file': open(file, 'rb')}
    else:
        raise Exception("The RDF file you provided doesn't seem to be a valid file path. Please check the path.")

    data = {
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/resources/import_rdf/'+dataset_id, data, file)

    return response
    #return pd.DataFrame.from_dict(response['datasets']).set_index('id')
