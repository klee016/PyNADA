from .manage_and_update import *


def create_collection(
        repository_id=None,
        title=None,
        short_text=None,
        long_text=None,
        thumbnail_path=None,
        weight=None,
        section=None,
        is_published=None
):
    """Create new collection
    
    Parameters
    ----------
    repository_id : str
        Collection identifier containing numbers and letters only
    title: str
        Collection Title
    short_text: str
        A short description for the collection
    long_text: str
        Detailed collection description. This field supports basic html and image tags.
    thumbnail_path: str
        Upload an image file or provide path/url
    weight: int
        Provide weight to arrange display of collection
    section: int
        2 = Regional collection, 3 = Specialized collection
    is_published: 0
        0= draft, 1=published
    """

    data ={
        'repositoryid': repository_id,
        'title': title,
        'short_text': short_text,
        'long_text': long_text,
        'weight': weight,
        'section': section,
        'ispublished': is_published
    }
    thumbnail_fname = PurePath(thumbnail_path).name
    thumbnail_ext = PurePath(thumbnail_fname).suffix
    if thumbnail_ext == ".jpg":
        thumbnail_format = "jpeg"
    elif thumbnail_ext == ".png":
        thumbnail_format = "png"
    elif thumbnail_ext == ".gif":
        thumbnail_format = "gif"
    else:
        print(
            f"Warning: Thumbnail not uploaded. The {thumbnail_ext} filetype you attempted to upload is not allowed. Allowable file types are .jpg, .png and .gif")
        thumbnail_path = thumbnail_fname = thumbnail_format = files = None

    if thumbnail_path:
        files = [
            ('thumbnail',
             (thumbnail_fname, open(f"{thumbnail_path}", 'rb'), f"image/{thumbnail_format}"))
        ]

    response = make_post_request("collections/" + repository_id, data, files=files)

    if response['status'] == "success":
        print("Collection successfully created.")

    return pd.DataFrame.from_dict(response, orient='index')


def create_entry(**kwargs):
    if 'study_desc' in kwargs:
        return create_survey_dataset(**kwargs)
    elif 'document_description' in kwargs:
        return create_document_dataset(**kwargs)
    elif 'image_description' in kwargs:
        return create_image_dataset(**kwargs)
    elif 'project_desc' in kwargs:
        return create_script_dataset(**kwargs)
    elif 'table_description' in kwargs:
        return create_table_dataset(**kwargs)
    elif 'visualization_description' in kwargs:
        return create_visualization_dataset(**kwargs)
    elif 'dataset_description' in kwargs:
        return create_geospatial_dataset(**kwargs)
    elif 'series_description' in kwargs:
        return create_timeseries_dataset(**kwargs)


def create_survey_dataset(
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
        'repositoryid': repository_id,
        'access_policy': access_policy,
        'published': published,
        'overwrite': overwrite,
        'doc_desc': doc_desc,
        'study_desc': study_desc,
        'data_files': data_files,
        'variables': variables,
        'variable_groups': variable_groups,
        'additional': additional
    }

    assert dataset_id == study_desc['title_statement']['idno']

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("datasets/create/survey/"+dataset_id, data)

    if response['status'] == "success":
        print("Survey dataset successfully added to the catalog.")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def create_document_dataset(
        dataset_id=None,
        repository_id=None,
        published=None,
        overwrite=None,
        metadata_information=None,
        document_description=None,
        tags=None,
        resources=None,
        files=None  # deprecated - use resources
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
    resources : list of dict
        Resources
    files : list of dict
        Files

    Returns
    -------
    DataFrame
        Information on the added document
    """

    data = {
        'repositoryid': repository_id,
        'published': published,
        'overwrite': overwrite,
        'metadata_information': metadata_information,
        'document_description': document_description,
        'tags': tags,
        'resources': resources,
        'files': files
    }

    assert dataset_id == document_description['title_statement']['idno']

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("datasets/create/document/"+dataset_id, data)

    if response['status'] == "success":
        # for old codes that use files parameter instead of resources parameter
        if resources is None and files is not None and len(files) > 0:
            for file in files:
                add_resource(
                    dataset_id=dataset_id,
                    dctype="Document [doc/oth]",
                    title=PurePath(file['file_uri']).stem,
                    filename=file['file_uri'],
                    overwrite=overwrite
                )
        print("Document dataset successfully added to the catalog.")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def create_image_dataset(
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
        'repositoryid': repository_id,
        'published': published,
        'overwrite': overwrite,
        'metadata_information': metadata_information,
        'image_description': image_description
    }

    assert dataset_id == image_description['iptc']['photoVideoMetadataIPTC']['digitalImageGuid']

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("datasets/create/image/"+dataset_id, data)

    if response['status'] == "success":
        if 'files' in image_description and len(image_description['files']) > 0:
            for file in image_description['files']:
                add_resource(
                    dataset_id=dataset_id,
                    dctype="Document [doc/oth]",
                    title=PurePath(file['file_uri']).stem,
                    filename=file['file_uri'],
                    overwrite=overwrite
                )
        print("Image dataset successfully added to the catalog.")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def create_script_dataset(
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
        'repositoryid': repository_id,
        'published': published,
        'overwrite': overwrite,
        'doc_desc': doc_desc,
        'project_desc': project_desc
    }

    assert dataset_id == project_desc['title_statement']['idno']

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("datasets/create/script/"+dataset_id, data)

    if response['status'] == 'success':
        if 'scripts' in project_desc and len(project_desc['scripts'] > 0):
            for script in project_desc['scripts']:
                add_resource(
                    dataset_id = dataset_id,
                    dctype = "Document [doc/oth]",
                    title = script['title'],
                    filename = script['file_name'],
                    overwrite = overwrite
                )
        print("Script dataset successfully added to the catalog.")


    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def create_table_dataset(
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
        'repositoryid': repository_id,
        'published': published,
        'overwrite': overwrite,
        'metadata_information': metadata_information,
        'table_description': table_description,
        'files': files,
        'tags': tags,
        'additional': additional
    }

    assert dataset_id == table_description['title_statement']['idno']

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("datasets/create/table/"+dataset_id, data)

    if response['status'] == "success":
        if files is not None and len(files) > 0:
            for file in files:
                add_resource(
                    dataset_id=dataset_id,
                    dctype="Document [doc/oth]",
                    title=PurePath(file['file_uri']).stem,
                    filename=file['file_uri'],
                    overwrite=overwrite
                )
        print("Table dataset successfully added to the catalog.")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def create_visualization_dataset(
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
        'repositoryid': repository_id,
        'published': published,
        'overwrite': overwrite,
        'metadata_information': metadata_information,
        'visualization_description': visualization_description,
        'files': files,
        'additional': additional
    }

    assert dataset_id == visualization_description['title_statement']['idno']

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("datasets/create/visualization/"+dataset_id, data)

    if response['status'] == "success":
        if files is not None and len(files) > 0:
            for file in files:
                add_resource(
                    dataset_id=dataset_id,
                    dctype="Document [doc/oth]",
                    title=PurePath(file['file_uri']).stem,
                    filename=file['file_uri'],
                    overwrite=overwrite
                )
        print("Visualization dataset successfully added to the catalog.")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def create_geospatial_dataset(
        dataset_id=None,
        repository_id=None,
        published=None,
        overwrite=None,
        description=None,
        tags=None,
        provenance=None,
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
    description : dict
        Dataset description following ISO 19115 / ISO 19119 / ISO/TS 19139 metadata standard
    tags : list of dict
        Tags
    provenance : list of dict
        Provenance of metadata based on the OAI provenance schema (http://www.openarchives.org/OAI/2.0/provenance.xsd)
    additional : dict
        Any other custom metadata not covered by the schema

    Returns
    -------
    DataFrame
        Information on the added geospatial dataset
    """

    data = {
        'repositoryid': repository_id,
        'published': published,
        'overwrite': overwrite,
        'description': description,
        'tags': tags,
        'provenance': provenance,
        'additional': additional
    }

    assert dataset_id == description['idno']

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("datasets/create/geospatial/"+dataset_id, data)

    if response['status'] == "success":
        print("Geospatial dataset successfully added to the catalog.")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def create_timeseries_dataset(
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
        'repositoryid': repository_id,
        'access_policy': access_policy,
        'data_remote_url': data_remote_url,
        'published': published,
        'overwrite': overwrite,
        'metadata_creation': metadata_creation,
        'series_description': series_description,
        'additional': additional
    }

    assert dataset_id == series_description['idno']

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("datasets/create/timeseries/"+dataset_id, data)

    if response['status'] == "success":
        print("Timeseries dataset successfully added to the catalog.")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def create_timeseries_database(
        published=None,
        overwrite=None,
        database_description=None,
        additional=None
):
    """Add a new timeseries database to the catalog

    Parameters
    ----------
    published : int
        Set status for study - 0 = Draft, 1 = Published
    overwrite : str
        Overwrite if a study with the same ID already exists? Valid values "yes", "no"
    database_description : dict
        Metadata for the database
    additional : dict
        Any other custom metadata not covered by the schema

    Returns
    -------
    DataFrame
        Information on the added database
    """

    data = {
        'published': published,
        'overwrite': overwrite,
        'database_description': database_description,
        'additional': additional
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("datasets/create/timeseriesdb", data)

    if response['status'] == "success":
        print("Timeseries database successfully added to the catalog.")

    return response
    #return pd.DataFrame.from_dict(response['dataset'], orient='index')


def import_DDI(
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
    elif Path(file).exists():
        print("You provided a file for the DDI XML. Processing...")
        file = {'file': open(Path(file), 'rb')}
    else:
        raise Exception("The DDI XML file you provided doesn't seem to be a valid file path or URL." 
                        "If it is a file, please check the path."
                        "If it is a URL, make sure to add a proper prefix such as http://")

    if rdf is not None:
        if validators.url(rdf):
            print("You provided a URL for the RDF. Processing...")
        elif Path(rdf).exists():
            print("You provided a file for the RDF. Processing...")
            rdf = {'file': open(Path(rdf), 'rb')}
        else:
            raise Exception("The RDF file you provided doesn't seem to be a valid file path or URL."
                            "If it is a file, please check the path."
                            "If it is a URL, make sure to add a proper prefix such as http://")

    data = {
        # 'file': file,
        'overwrite': overwrite,
        'repositoryid': repository_id,
        'access_policy': access_policy,
        'data_remote_url': data_remote_url,
        'rdf': rdf,
        'published': published,
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("datasets/import_ddi", data, file)

    if response['status'] == "success":
        print("Survey dataset successfully added to the catalog.")

    return response['survey']


def import_RDF(
        dataset_id=None,
        file=None
):
    """Import an RDF file to batch import external resources

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    file : str
        Dublin core RDF file (rdf, xml)
    """

    if Path(file).exists():
        print("You provided a file for Dublin core RDF. Processing...")
        file = {'file': open(Path(file), 'rb')}
    else:
        raise Exception("The RDF file you provided doesn't seem to be a valid file path. Please check the path.")

    data = {
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("datasets/"+dataset_id+"/resources/import_rdf", data, file)

    if response['status'] == "success":
        print("Resource(s) successfully added to the dataset.")

    return response

def upload_video(
        idno,
        metadata=None,
        published=None,
        overwrite=None,
        thumbnail=None,
        tags=None,
        repositoryid=None
):
    """Add a video to the catalog
    Returns
    -------
    :param  thumbnail: str. path to thumbnail
    :param  idno: str. Unique video identifier. Required
    :param  metadata: obj. contains the following
            title: str. Title. Required
            alt_title: str. Alternate title or other title
            description: str. Description
            genre: str. Genre
            keywords: str. Keywords
            topics_list: array. Topic Classification formatted as [{"topic":"","vocab":"", "uri":""}]
            persons_list: array. Persons, formatted as [{"name":"", "role":""}]. Required
            main_entity:str. Primary entity described in the video
            video_provider: str. Video provider e.g. youtube, vimeo, facebook
            video_url: str. Video URL
            embed_url: str. Video embed URL
            encoding_format: str. Encoding format (string). Media type using a MIME format
            duration: str. The duration of the video in ISO 8601 date time format -hh:mm:ss
            content_location: str. Location depicted or described in the video
            spatial_coverage: str. Place(s) which are the focus of the content
            content_reference_time: str. Specific time described by a creative work, for works that emphasize a particular moment within an Event
            temporal_coverage: str. Period that the content applies to using ISO 8601 date time format
            audience: str. Intended audience
            country: str.
            language: str.
            creator: str. Author
            publisher: str. Publisher
            contributor: str. Contributor
            funder: str. Funder
            translator: str. Organization or person who adapts a creative work to different languages
            rights: str. Rights
            copyright_holder: str. The party holding the legal copyright
            copyright_notice: str. Text of a notice describing the copyright
            copyright_year: str. Year during which claimed copyright for the video was first asserted
            date_created: str. Date of creation (YYYY-MM-DD)
            date_published: str. Date published (YYYY-MM-DD)
            version: str. Version
            status: str. Status of a creative work in terms of its stage in lifecycle. e.g. incomplete, draft, published,obsolete
            is_based_on: str. A resource from which this work is derived or from which it is a modification or adaption
            metadata_information: obj. {"producers":[{"name":""}],"production_date":"","version_date":"YYYY-MM-DD"}
    :param  tags: array. Tags formatted as [{"tag":"", "tag_group":""}]
    :param  repositoryid: str. Repository ID
    :param  published: int. Draft=0, Published=1
    :param  overwrite: str. values: "yes"/"no"
    """
    data = {
        "repositoryid": repositoryid,
        "published": published,
        "overwrite": overwrite,
        "video_description": metadata['video_description'],
        "tags": tags,
        "additional": metadata['metadata_information]
    }
    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/create/video/', data)

    if response['status'] == 'success':
        print("Video successfully added to the catalog.")
    if thumbnail:
        upload_thumbnail(idno, thumbnail)
