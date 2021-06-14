import requests
import json
import sys
import pandas as pd


api_base_url = ''
http_headers = {}


def set_api_key(key):
    """Set an API key for authorization.

    Parameters
    ----------
    key : str
        API key
    """

    # global api_key
    # api_key = key
    global http_headers
    http_headers['X-API-KEY'] = key


def get_api_key():
    """Get API key

    Returns
    -------
    api_key : str
        API key
    """
    
    # return api_key
    return http_headers['X-API-KEY']


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


def set_api_auth(auth):
    """Set authorization string

    Parameters
    ----------
    auth : str
        Authorization string
    """

    global http_headers
    http_headers['Authorization'] = auth


def get_api_auth():
    """Get authorization string

    Returns
    -------
    auth : str
        Authorization string
    """

    return http_headers['Authorization']


def set_api_env(url=None, headers=None):
    """Set base URL and http headers

    Parameters
    ----------
    url : str
        Base URL string
    headers : dict
        Http headers
    """

    global api_base_url
    global http_headers
    api_base_url = url
    http_headers = headers


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

    response = requests.get(api_base_url + endpoint, headers=http_headers, params=params)
    
    if response.status_code != 200:
        raise Exception('GET /'+endpoint+'/ {}'.format(response.status_code) + ' ' + f'{response.text}')

    try:
        json_response = response.json()
    except ValueError:
        raise Exception('GET /' + endpoint + '/ {}'.format(response.status_code) + ' ' + f'{response.text}')

    return json_response

   
def make_post_request(endpoint, data, files=None):
    """Make a general POST HTTP request

    Parameters
    ----------
    endpoint : str
        API endpoint
    data : dict
        POST data
    files : file object
        File

    Returns
    -------
    response : dict
        HTTP response
    """

    if len(data) == 0:
        data = ""
    elif depth(data) > 0 and files is None:
        data = json.dumps(data)

    response = requests.post(api_base_url + endpoint, headers=http_headers, data=data, files=files)

    if response.status_code != 200:
        raise Exception('POST /'+endpoint+'/ {}'.format(response.status_code) + ' ' + f'{response.text}')

    try:
        json_response = response.json()
    except ValueError:
        raise Exception('GET /' + endpoint + '/ {}'.format(response.status_code) + ' ' + f'{response.text}')

    return json_response


def make_put_request(endpoint, data):
    """Make a general PUT HTTP request

    Parameters
    ----------
    endpoint : str
        API endpoint
    data : dict
        PUT data

    Returns
    -------
    response : dict
        HTTP response
    """

    if len(data) == 0:
        data = ""
    elif depth(data) > 1:
        data = json.dumps(data)

    response = requests.put(api_base_url + endpoint, headers=http_headers, data=data)

    if response.status_code != 200:
        raise Exception('PUT /'+endpoint+'/ {}'.format(response.status_code) + ' ' + f'{response.text}')

    try:
        json_response = response.json()
    except ValueError:
        raise Exception('GET /' + endpoint + '/ {}'.format(response.status_code) + ' ' + f'{response.text}')

    return json_response


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

    response = requests.delete(api_base_url + endpoint, headers=http_headers)

    if response.status_code != 200:
        raise Exception('DELETE /' + endpoint + '/ {}'.format(response.status_code) + ' ' + f'{response.text}')

    try:
        json_response = response.json()
    except ValueError:
        raise Exception('GET /' + endpoint + '/ {}'.format(response.status_code) + ' ' + f'{response.text}')

    return json_response


def depth(d):
    """Returns the depth of a dictionary
    """
    if isinstance(d, dict):
        return 1 + (max(map(depth, d.values())) if d else 0)
    return 0
