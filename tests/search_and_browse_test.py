from pynada import search_and_browse

search_and_browse.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
search_and_browse.set_api_key(api_key)

#print(search_and_browse.list_all())

#print(search_and_browse.dataset_info('WPS8038'))

print(search_and_browse.list_resources('BGD_RRRC-UNHCR-IOM_20190108'))

#print(search_and_browse.list_datafiles('BGD_RRRC-UNHCR-IOM_20190108'))

#print(search_and_browse.list_files('BGD_RRRC-UNHCR-IOM_20190108'))