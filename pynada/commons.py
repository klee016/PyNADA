import requests

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
    Returns: HTTP response in JSON
    """
    
    headers = {
        'X-API-KEY': api_key
    }
    
    response = requests.get(api_base_url+endpoint, headers=headers, params=params)
    
    if response.status_code != 200:
        # This means something went wrong.
        raise Exception('GET /tasks/ {}'.format(response.status_code))
    
    return response.json()
   
    