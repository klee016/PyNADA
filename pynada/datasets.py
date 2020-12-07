def list_all_datasets():
    """returns a list of all datasets in the FCV catalog
    Parameters:
    Returns:
    """

    collections = requests.get('http://training.ihsn.org/index.php/api/datasets')
    if collections.status_code != 200:
        # This means something went wrong.
        raise Exception('GET /tasks/ {}'.format(collections.json()))
    
    for item in collections.json():
        print(item)