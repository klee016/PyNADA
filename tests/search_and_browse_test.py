from pynada import search_and_browse

search_and_browse.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
search_and_browse.set_api_key(api_key)

# result = search_and_browse.list_all_datasets()
# print("okay")

#print(search_and_browse.list_all_collections())

#print(search_and_browse.list_all_datasets())

print(search_and_browse.get_dataset_info('IMAGE-DATASET-SAMPLE-01'))

#print(search_and_browse.list_resources('BGD_RRRC-UNHCR-IOM_20190108'))

#print(search_and_browse.list_datafiles('BGD_RRRC-UNHCR-IOM_20190108'))

#print(search_and_browse.list_files('survey-doc-01'))