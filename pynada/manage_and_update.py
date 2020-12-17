from .search_and_browse import *
from pathlib import Path
import validators


def delete_dataset(dataset_id):
    """Delete dataset

    Parameters
    ----------
    dataset_id : str
        Dataset IDNo
    """

    response = make_delete_request('datasets/' + dataset_id)

    if response['status'] == 'success':
        print('Successfully deleted.')


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

    response = make_post_request('datasets/' + dataset_id + '/files', data, file)

    #print(response)
    if response['status'] == 'success':
        print('Successfully uploaded.')


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
    response = make_delete_request('datasets/' + dataset_id + '/files/' + base64)

    #print(response)
    if response['status'] == 'success':
        print('Successfully deleted.')


def add_thumbnail(dataset_id, file_path):
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

    response = make_post_request('datasets/thumbnail/' + dataset_id, data, file)

    #print(response)
    if response['status'] == 'success':
        print('Thumbnail successfully uploaded.')


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
        changed=None
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

    data = {
        "dctype": dctype,
        "dcformat": dcformat,
        "title": title,
        "author": author,
        "dcdate": dcdate,
        "country": country,
        "language": language,
        "contributor": contributor,
        "publisher": publisher,
        "rights": rights,
        "description": description,
        "abstract": abstract,
        "toc": toc,
        "filename": filename,
        "created": created,
        "changed": changed
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/'+dataset_id+'/resources', data)

    return response
    #return pd.DataFrame.from_dict(response['datasets']).set_index('id')









def update_survey(dataset_id=None):

    data = {
        "published": 1
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/update/survey/' + dataset_id, data)

    return response
