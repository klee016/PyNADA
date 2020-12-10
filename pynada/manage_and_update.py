from .commons import *


def delete_dataset(idno):
    """Delete dataset

    Parameters
    ----------
    idno : str
        Dataset IDNo

    Returns
    -------
    dict
        response
    """

    response = make_delete_request('datasets/' + idno)

    if response['result'] == 'success':
        print('Successfully deleted.')



def update_survey(idno=None):

    data = {
        "published": 1
    }

    data = {key: value for key, value in data.items() if value is not None}
    response = make_post_request('datasets/update/survey/' + idno, data)

    return response
