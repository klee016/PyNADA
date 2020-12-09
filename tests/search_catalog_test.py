from pynada import search_catalog

search_catalog.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
search_catalog.set_api_key(api_key)

print(search_catalog.list_all())

#print(search_catalog.dataset_info('WPS8038'))