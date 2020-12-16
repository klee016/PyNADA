import requests
import json

api_key = ''
api_base_url = ''


def set_api_key(key):
    """Set an API key for authorization.

    Parameters
    ----------
    key : str
        API key
    """
    
    global api_key
    api_key = key

    
    
def get_api_key():
    """Get API key

    Returns
    -------
    api_key : str
        API key
    """
    
    return api_key

    
    
def set_api_url(url):
    """Set API Base URL

    Parameters
    ----------
    url : str
        URL string
    """
    
    global api_base_url
    api_base_url = url



def get_api_url():
    """Get API Base URL

    Returns
    -------
    base_url : str
        API Base URL
    """
    
    return api_base_url


def make_get_request(endpoint, params):
    """Make a general GET HTTP request

    Parameters
    ----------
    endpoint : str
        API endpoint
    params : dict
        GET parameters

    Returns
    -------
    response : dict
        HTTP response
    """
    
    headers = {
        'X-API-KEY': api_key
    }

    response = requests.get(api_base_url + endpoint, headers=headers, params=params)
    
    if response.status_code != 200:
        raise Exception('GET /'+endpoint+'/ {}'.format(response.status_code) + ' ' + f'{response.text}')

    print(response.text)
    return response.json()


   
def make_post_request(endpoint, data, files=None):
    """Make a general POST HTTP request

    Parameters
    ----------
    endpoint : str
        API endpoint
    data : dict
        POST data
    file : file object
        File

    Returns
    -------
    response : dict
        HTTP response
    """

    headers = {
        'X-API-KEY': api_key
    }

    if len(data) == 0:
        data = ""
    else:
        data = json.dumps(data)

    response = requests.post(api_base_url + endpoint, headers=headers, data=data, files=files)

    print(response.status_code)
    if response.status_code != 200:
        print(response.request.body)
        raise Exception('POST /'+endpoint+'/ {}'.format(response.status_code) + ' ' + f'{response.text}')

    print(response.text)
    return response.json()


def make_delete_request(endpoint):
    """Make a general DELETE HTTP request

    Parameters
    ----------
    endpoint : str
        API endpoint

    Returns
    -------
    response : dict
        HTTP response
    """

    headers = {
        'X-API-KEY': api_key
    }

    response = requests.delete(api_base_url + endpoint, headers=headers)

    if response.status_code != 200:
        print(response.request.body)
        raise Exception('DELETE /' + endpoint + '/ {}'.format(response.status_code) + ' ' + f'{response.text}')

    print(response.text)
    return response.json()