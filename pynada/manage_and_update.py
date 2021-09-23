from .search_and_browse import *
from pathlib import Path, PurePath
import validators


def delete_dataset(dataset_id):
    """Delete dataset

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    """

    response = make_delete_request("datasets/" + dataset_id)

    if response['status'] == "success":
        print("Dataset successfully deleted from the catalog.")


def upload_file(dataset_id, file_path):
    """upload a single file and attach it to a dataset.

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    file_path : str
        path and file name to be uploaded
    """

    data = {}
    if Path(file_path).exists():
        print("Uploading the file...")
        file = {'file': open(Path(file_path), 'rb')}
    else:
        raise Exception("The file you provided doesn't seem to be a valid file. Please check the path.")

    response = make_post_request("datasets/" + dataset_id + "/files", data, file)

    #print(response)
    if response['status'] == "success":
        print("File successfully uploaded.")


def delete_file(dataset_id, file_name):
    """delete a single file from a dataset.

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    file_name : str
        file name
    """

    df_files = list_files(dataset_id)
    base64 = df_files[df_files['name'] == file_name]['base64'].values[0]

    #print('datasets/' + idno + '/files/' + base64)
    response = make_delete_request("datasets/" + dataset_id + "/files/" + base64)

    #print(response)
    if response['status'] == "success":
        print("File successfully deleted.")


def upload_thumbnail(dataset_id, file_path):
    """Add or update thumbnail for a dataset

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    file_path : str
        path and file name to be uploaded, Supported formats are jpg, jpeg and png
    """

    data = {}
    if Path(file_path).exists():
        print("Uploading thumbnail...")
        file = {'file': open(Path(file_path), 'rb')}
    else:
        raise Exception("The thumbnail file you provided doesn't seem to be a valid file. Please check the path.")

    response = make_post_request("datasets/thumbnail/" + dataset_id, data, file)

    #print(response)
    if response['status'] == "success":
        print("Thumbnail successfully uploaded.")


def add_resource(
        dataset_id=None,
        dctype=None,
        dcformat=None,
        title=None,
        author=None,
        dcdate=None,
        country=None,
        language=None,
        contributor=None,
        publisher=None,
        rights=None,
        description=None,
        abstract=None,
        toc=None,
        filename=None,
        created=None,
        changed=None,
        overwrite=None
):
    """Add an external resource to a dataset

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    dctype : str
        Document types for external resource
    dcformat : str
        Document file format
    title: str
        Title of the source
    author : str
        Author of the source
    dcdate : str
        Date
    country : str
        country
    language : str
        language
    contributor : str
        contributor
    publisher : str
        publisher
    rights : str
        rights
    description : str
        Description of the source
    abstract : str
        Abstract of the source
    toc : str
        toc
    filename : str
        File name or URL. For uploading files, use the 'upload_file' function and make sure the file name is exactly the same.
    created : str
        Creation date-time of the resource
    changed : str
        Modification date-time of the resource
    """

    if validators.url(filename):
        print("You provided a resource URL. Processing...")
    elif Path(filename).exists():
        print("You provided a resource file. Processing...")
        upload_file(dataset_id, filename)
    else:
        raise Exception("The filename you provided doesn't seem to be a valid file path or URL." 
                        "If it is a file, please check the path."
                        "If it is a URL, make sure to add a proper prefix such as http://")

    data = {
        'dctype': dctype,
        'dcformat': dcformat,
        'title': title,
        'author': author,
        'dcdate': dcdate,
        'country': country,
        'language': language,
        'contributor': contributor,
        'publisher': publisher,
        'rights': rights,
        'description': description,
        'abstract': abstract,
        'toc': toc,
        'filename': filename,
        'created': created,
        'changed': changed,
        'overwrite': overwrite
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("datasets/"+dataset_id+"/resources", data)

    if response['status'] == "success":
        print("Resource successfully added to the dataset.")


def delete_variables_by_file(dataset_id, file_id):
    """Batch delete all variables from a datafile or Dataset.

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    file_id : str
        file IDNo
    """

    response = make_delete_request("datasets/batch_delete_vars/" + dataset_id + "/" + file_id)

    if response['status'] == "success":
        print("Files successfully deleted.")


def update_survey_dataset(
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
    """Update survey's full or partial metadata. Only the fields provided are updated.

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
        Updated dataset
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
    response = make_post_request("datasets/update/survey/"+dataset_id, data)

    if response['status'] == "success":
        print("Survey dataset successfully updated.")

    return pd.DataFrame.from_dict(response['dataset'], orient='index')


def add_variables(
        dataset_id=None,
        file_id=None,
        vid=None,
        name=None,
        labl=None,
        var_intrvl=None,
        var_dcml=None,
        var_wgt=None,
        var_start_pos=None,
        var_end_pos=None,
        var_width=None,
        var_imputation=None,
        var_security=None,
        var_respunit=None,
        var_qstn_preqtxt=None,
        var_qstn_qstnlit=None,
        var_qstn_postqtxt=None,
        var_qstn_ivulnstr=None,
        var_universe=None,
        var_sumstat=None,
        var_txt=None,
        var_catgry=None,
        var_codinstr=None,
        var_concept=None,
        var_format=None,
        var_notes=None
):
    """Create a new variable for a data file.

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    file_id : str
        File to which the variable belongs
    vid : str
        Unique variable ID
    name : str
        Variable name
    labl : str
        Variable label
    var_intrvl : str
        Indicates the interval type; options are discrete or continuous. Valid values: "discrete" "contin"
    var_dcml : str
        Number of decimal points in the variable
    var_wgt : int
        indicates whether the variable is a weight. Default: 0
    var_start_pos : int
        Variable start position
    var_end_pos : int
        Variable end position
    var_width : int
        Variable width
    var_imputation : str
        Imputation
    var_security : str
        Security
    var_respunit : str
        Source of information
    var_qstn_preqtxt : str
        Text describing a set of conditions under which a question might be asked.
    var_qstn_qstnlit : str
        Literal question
    var_qstn_postqtxt : str
        Post-question text
    var_qstn_ivulnstr : str
        Interviewer instructions
    var_universe : str
        Universe
    var_sumstat : list of dict
        One or more statistical measures that describe the responses to a particular variable and may include one or more standard summaries
    var_txt : str
        Variable description
    var_catgry : list of dict
        Category
    var_codinstr : str
        Recoding and derivation
    var_concept : list of dict
        Concept
    var_format : dict
        The technical format of the variable in question.
    var_notes : str
        Variable notes

    Returns
    -------
    DataFrame
        Information on the added variable
    """

    data = {
        'file_id': file_id,
        'vid': vid,
        'name': name,
        'labl': labl,
        'var_intrvl': var_intrvl,
        'var_dcml': var_dcml,
        'var_wgt': var_wgt,
        'var_start_pos': var_start_pos,
        'var_end_pos': var_end_pos,
        'var_width': var_width,
        'var_imputation': var_imputation,
        'var_security': var_security,
        'var_respunit': var_respunit,
        'var_qstn_preqtxt': var_qstn_preqtxt,
        'var_qstn_qstnlit': var_qstn_qstnlit,
        'var_qstn_postqtxt': var_qstn_postqtxt,
        'var_qstn_ivulnstr': var_qstn_ivulnstr,
        'var_universe': var_universe,
        'var_sumstat': var_sumstat,
        'var_txt': var_txt,
        'var_catgry': var_catgry,
        'var_codinstr': var_codinstr,
        'var_concept': var_concept,
        'var_format': var_format,
        'var_notes': var_notes
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/variables/'+dataset_id+'/'+file_id, data)

    if response['status'] == "success":
        print("Variable successfully added to the survey dataset.")

    return pd.DataFrame(response, orient='index')
    #return pd.DataFrame.from_dict(response['variable'], orient='index')


def set_dataset_options(
        dataset_id=None,
        access_policy=None,
        data_remote_url=None,
        published=None,
        tags=None,
        aliases=None,
        owner_collection=None,
        linked_collections=None,
        link_study=None,
        link_indicator=None
):
    """Set various options for dataset

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    access_policy : str
        Data access policy. Valid values - "open" "direct" "public" "licensed" "enclave" "remote" "other"
    data_remote_url : str
        Link to the website where the data is available for 'Data available from remote repository'
    published : int
        Set project publish status. 0=draft, 1=published
    tags : list of str
        Tags
    aliases : list of str
        Aliases
    owner_collection : str
        Collection that owns the dataset
    linked_collections str
        Display in other collections
    link_study : str
        URL for study website
    link_indicator : str
        URL to the indicators website

    Returns
    -------
    DataFrame
        Dataset options
    """

    data = {
        'access_policy': access_policy,
        'data_remote_url': data_remote_url,
        'published': published,
        'tags': tags,
        'aliases': aliases,
        'owner_collection': owner_collection,
        'linked_collections': linked_collections,
        'link_study': link_study,
        'link_indicator': link_indicator
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_put_request("datasets/"+dataset_id, data)

    if response['status'] == "success":
        print("Dataset options successfully set.")

    return pd.DataFrame(response, orient='index')
    #return pd.DataFrame.from_dict(response['dataset'], orient='index')


def delete_DDI_metadata(
        dataset_id=None,
        options=None
):
    """Remove metadata from the DDI file

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    options : str
        Options for removing metadata elements. Valid options are "summary_stats", "variables", "keep_basic"
    """

    data = {
        'dataset_id': dataset_id,
        'options': options
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_put_request("datasets/strip_ddi/"+dataset_id+"/"+options, data)

    if response['status'] == "success":
        print("DDI metadata successfully removed.")


def set_dataset_numid(
        dataset_id=None,
        new_numid=None
):
    """Change the dataset internal numeric database ID

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    new_numid : int
        New numeric id
    """

    data = {
        'dataset_id': dataset_id,
        'new_id': new_numid
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_put_request("datasets/update_id/"+dataset_id+"/"+str(new_numid), data)

    if response['status'] == "success":
        print("Dataset numeric ID successfully changed.")


def generate_metadata_PDF(
        dataset_id=None,
        variable_toc=None,
        variable_description=None,
        include_resources=None,
        language=None
):
    """Generate PDF documentation for surveys

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    variable_toc : int
        Include table of contents for variables? 0=No, 1=Yes
    variable_description : int
        Generate variable descriptions? 0=No, 1=Yes
    include_resources : int
        Include external resources? 0=No, 1=Yes
    language : str
        Set the language for the PDF report e.g., en - English, fr - French, ar - Arabic
    """

    data = {
        'dataset_id': dataset_id,
        'variable_toc': variable_toc,
        'variable_description': variable_description,
        'include_resources': include_resources,
        'language': language
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_put_request("datasets/generate_pdf/"+dataset_id, data)

    if response['status'] == "success":
        print("PDF metadata documentation successfully generated.")


def upload_widget(
        widget_id=None,
        title=None,
        file_path=None,
        thumbnail=None,
        description=None,
):
    """Upload a widget (ex: chart, map, diagram) to the catalog

    Parameters
    ----------
    widget_id : str
        Widget UUID
    title : str
        Title of the graphic
    file_path : str
        Path and file name of a zip file containing HTML, CSS, JS, etc.
    thumbnail : str
        Name of the image file to use as thumbnail
    description: : str
        Description of the widget
    """

    if Path(file_path).exists() and PurePath(file_path).suffix == ".zip":
        print("You provided a zip file. Processing...")
        file = {'file': open(Path(file_path), 'rb')}
    else:
        raise Exception("The file_path you provided doesn't seem to be a valid file path or a zip file.")

    data = {
        'title': title
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("widgets/"+widget_id, data, file)

    if response['status'] == "success":
        print("Widget successfully uploaded to the catalog.")

    return pd.DataFrame.from_dict(response)


def attach_widget(
        dataset_id=None,
        widget_id=None
):
    """Attach a widget (ex: chart, map, diagram) to a dataset

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    widget_id : str
        Widget UUID
    """

    data = {
        'idno': dataset_id,
        'uuid': widget_id
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request("widgets/attach_to_study", data)

    if response['status'] == "success":
        print("Widget successfully attached to the dataset.")

    return pd.DataFrame.from_dict(response)


def update_collection(
        repository_id=None,
        title=None,
        short_text=None,
        long_text=None,
        thumbnail_path=None,
        weight=None,
        section=None,
        is_published=None
):
    """Update existing collection

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

    data = {
        'repositoryid': repository_id,
        'title': title,
        'short_text': short_text,
        'long_text': long_text,
        'weight': weight,
        'section': section,
        'ispublished': is_published
    }
    data = {key: value for key, value in data.items() if value is not None}

    thumbnail_fname = PurePath(thumbnail_path).name
    thumbnail_ext = PurePath(thumbnail_fname).suffix
    if thumbnail_ext == ".jpg":
        thumbnail_format = "jpeg"
    elif thumbnail_ext == ".png":
        thumbnail_format = "png"
    elif thumbnail_ext == ".gif":
        thumbnail_format = "gif"
    else:
        print(f"The {thumbnail_ext} filetype you attempted to upload is not allowed. Allowable file types are .jpg, .png and .gif")

    if thumbnail_path:
        files = [
            ('thumbnail',
             (thumbnail_fname, open(f"{thumbnail_path}", 'rb'), f"image/{thumbnail_format}"))
        ]
    else:
        files = None

    response = make_post_request("collections/update/"+repository_id, data, files=files)

    if response['status'] == "success":
        print("Collection successfully updated.")

    return pd.DataFrame.from_dict(response, orient='index')


def rename_collection(
        old_repository_id=None,
        new_repository_id=None
):
    """Update existing collection

    Parameters
    ----------
    old_repository_id : str
        Collection identifier containing numbers and letters only
    new_repository_id:str
    """

    data = {'old_repositoryid': old_repository_id,
            'new_repositoryid': new_repository_id}
    # files=[]
    # response = requests.request("POST", url, headers=headers, data=payload, files=files)
    response = make_post_request("collections/rename/", data)

    if response['status'] == "success":
        print("Collection ID successfully renamed.")

    return pd.DataFrame.from_dict(response, orient='index')


def delete_collection(
        repository_id=None
):
    """Update existing collection

    Parameters
    ----------
    repository_id : str
        Collection identifier containing numbers and letters only
    """

    response = make_delete_request("collections/" + repository_id)

    if response['status'] == "success":
        print(f"Collection {repository_id} successfully deleted.")

    return pd.DataFrame.from_dict(response, orient='index')


def attach_dataset(
        dataset_id=None,
        owner_collection=None,
        link_collections=None,
        mode=None
):
    """Replace or attach a dataset to collection(s)

    Parameters
    ----------
    dataset_id: str
        Dataset IDNo - Required
    owner_collection: str
        Collection's id that owns the dataset/study. (optional) if a value is provided,
        it will replace the owner collection for the study.
    link_collections: Array of string - Required
        List of collections that will display the dataset/study
    mode:str
        Select flag to update or replace the linked collections (string) Required.
        Default - "update"
        Valid values - "replace", "update"
    """

    if link_collections is None:
        link_collections = []

    data = json.dumps([
        {
            'study_idno': dataset_id,
            'owner_collection': owner_collection,
            'link_collections': link_collections,
            'mode': mode
        }
    ])

    response = make_post_request("datasets/collections/", data)

    if response['status'] == "success" and owner_collection:
        print(f"{dataset_id} successfully attached to {owner_collection} collection and linked to {link_collections}.")
    elif response['status'] == "success" and not owner_collection:
        print(f"{dataset_id} successfully linked to {link_collections} collection")
    else:
        print(response['status'])
    return pd.DataFrame.from_dict(response, orient='index')
