from .search_and_browse import *


def delete_dataset(idno):
    """Delete dataset

    Parameters
    ----------
    idno : str
        Dataset IDNo
    """

    response = make_delete_request('datasets/' + idno)

    if response['status'] == 'success':
        print('Successfully deleted.')



def upload_file(idno, file_path):
    """upload a single file and attach it to a dataset.

    Parameters
    ----------
    idno : str
        Dataset IDNo
    file_path : str
        path and file name
    """

    data = {}
    file = {'file': open(file_path, 'rb')}

    response = make_post_request('datasets/' + idno + '/files', data, file)

    #print(response)
    if response['status'] == 'success':
        print('Successfully deleted.')



def delete_file(idno, file_name):
    """delete a single file from a dataset.

    Parameters
    ----------
    idno : str
        Dataset IDNo
    file_name : str
        file name
    """
    df_files = list_files(idno)
    base64 = df_files[df_files['name'] == file_name]['base64'].values[0]

    #print('datasets/' + idno + '/files/' + base64)
    response = make_delete_request('datasets/' + idno + '/files/' + base64)

    #print(response)
    if response['status'] == 'success':
        print('Successfully deleted.')



def update_survey(idno=None):

    data = {
        "published": 1
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/update/survey/' + idno, data)

    return response
