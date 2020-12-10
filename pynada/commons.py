import requests
import json

api_key = ''
api_base_url = ''


def set_api_key(key):
    """
    Set an API key for authorization. The key is sent in subsequent requests.
    Parameters: API key string
    """
    
    global api_key
    api_key = key

    
    
def get_api_key():
    """
    Get API key
    """
    
    return api_key

    
    
def set_api_url(url):
    """
    Set API Base URL
    Parameters: URL string
    """
    
    global api_base_url
    api_base_url = url



def get_api_url():
    """
    Get API Base URL
    """
    
    return api_base_url


def make_get_request(endpoint, params):
    """
    Make a general GET HTTP request
    Parameters: API endpoint, params
    Returns: HTTP response in dict
    """
    
    headers = {
        'X-API-KEY': api_key
    }
    print(api_base_url + endpoint)
    response = requests.get(api_base_url + endpoint, headers=headers, params=params)
    
    if response.status_code != 200:
        raise Exception('GET /'+endpoint+'/ {}'.format(response.status_code) + ' ' + f'{response.text}')

    print(response.text)
    return response.json()


   
def make_post_request(endpoint, data, files=None):
    """
    Make a general POST HTTP request
    Parameters: API endpoint, data
    Returns: HTTP response in dict
    """

    headers = {
        'X-API-KEY': api_key
    }

    if len(data) == 0:
        data = ""
    else:
        data = json.dumps(data)

    response = requests.post(api_base_url + endpoint, headers=headers, data=data, files=files)
    #response = requests.post(api_base_url + urllib.parse.quote(endpoint), headers=headers, json=data)

    print(response.status_code)
    if response.status_code != 200:
        print(response.request.body)
        raise Exception('POST /'+endpoint+'/ {}'.format(response.status_code) + ' ' + f'{response.text}')

    print(response.text)
    return response.json()


def make_delete_request(endpoint):
    """
    Make a general DELETE HTTP request
    Parameters: API endpoint
    Returns: success result in dict
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