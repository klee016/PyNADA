import pynada as nada

nada.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
nada.set_api_key(api_key)

result = nada.list_datasets()

#print(nada.list_collections())

#print(nada.list_datasets())

#print(nada.get_dataset_info('IMAGE-DATASET-SAMPLE-01'))

#print(nada.list_tags('IMAGE-DATASET-SAMPLE-01'))

#print(nada.list_aliases('TIMESERIES-DATASET-SAMPLE-01'))

#print(nada.list_variables('ALB_2005_LSMS_V01_M'))

#print(nada.get_variable_info('ALB_2005_LSMS_V01_M', 'V1'))

#print(nada.list_resources('BGD_RRRC-UNHCR-IOM_20190108'))

#print(nada.list_datafiles('BGD_RRRC-UNHCR-IOM_20190108'))

#print(nada.list_files('survey-doc-01'))