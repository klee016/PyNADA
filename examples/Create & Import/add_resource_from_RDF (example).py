import pynada as nada
import inspect

nada.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
nada.set_api_key(api_key)

################################
# add_resource_from_RDF example
################################

file = "SURVEY_DATASET_SAMPLE_03.xml"
overwrite = "yes"
repository_id = 'central'
access_policy = 'open'
published = 1

response = nada.add_survey_dataset_from_DDI(
	file=file,
	overwrite=overwrite,
	repository_id=repository_id,
	access_policy=access_policy,
	# data_remote_url=data_remote_url,
	# rdf=rdf,
	published=published
)

print(response)

thumbnail_path = nada.text_to_thumbnail("Survey\nDataset")
nada.add_thumbnail(dataset_id, thumbnail_path)