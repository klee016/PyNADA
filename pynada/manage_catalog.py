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