from pynada import search_and_browse

search_and_browse.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = open("API Key.txt", "r").read()
search_and_browse.set_api_key(api_key)


#print(search_and_browse.list_collections())

print(search_and_browse.list_datasets())

#print(search_and_browse.get_dataset_info('IMAGE-DATASET-SAMPLE-01'))

#print(search_and_browse.list_tags('IMAGE-DATASET-SAMPLE-01'))

#print(search_and_browse.list_aliases('TIMESERIES-DATASET-SAMPLE-01'))

#print(search_and_browse.list_variables('ALB_2005_LSMS_V01_M'))

#print(search_and_browse.get_variable_info('ALB_2005_LSMS_V01_M', 'V1'))

#print(search_and_browse.list_resources('BGD_RRRC-UNHCR-IOM_20190108'))

#print(search_and_browse.list_datafiles('BGD_RRRC-UNHCR-IOM_20190108'))

#print(search_and_browse.list_files('survey-doc-01'))