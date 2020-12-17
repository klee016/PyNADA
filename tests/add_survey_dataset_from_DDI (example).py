from pynada import create_and_import
from pynada import utils
import inspect

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

######################################
# add_survey_dataset_from_DDI example
######################################

file = "SURVEY_DATASET_SAMPLE_02.xml"
overwrite = "yes"
repository_id = "central"
access_policy = "open"
published = 1

response = create_and_import.add_survey_dataset_from_DDI(
    file=file,
    overwrite=overwrite,
    repository_id=repository_id,
    access_policy=access_policy,
    # data_remote_url=data_remote_url,
    # rdf=rdf,
    # published=published
)

print(response)

dataset_id = response['survey']['idno']
thumbnail_path = utils.text_to_thumbnail("Survey\nDataset")
create_and_import.add_thumbnail(dataset_id, thumbnail_path)
