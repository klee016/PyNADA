import requests

def list_all_datasets():
	"""returns a list of all datasets in the FCV catalog
	Parameters:
	Returns:
	"""
	
	collections = requests.get('http://training.ihsn.org/index.php/api/datasets')
	if collections.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(collections.status_code))
    
  for item in collections.json():
  	print(item)