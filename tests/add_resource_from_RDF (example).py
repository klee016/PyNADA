from pynada import create_and_import
from pynada import utils
import inspect

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

################################
# add_resource_from_RDF example
################################

# add a very simple survey dataset

dataset_id = "SURVEY_DATASET_SAMPLE_03"
repository_id = "central"
access_policy = "open"
published = 0
overwrite = "yes"
doc_desc = {
    "title": "metadata title",
    "idno": "metadata id",
    "producers": [
        {
            "name": "metadata producer name",
            "abbr": "metadata producer abbr",
            "affiliation": "metadata producer affiliation",
            "role": "metadata producer role"
        },
    ],
    "prod_date": "2020-12-08",
    "version_statement": {
        "version": "v_0.0.1",
        "version_date": "2020-12-08",
    },
}
study_desc = {
    "title_statement": {
        "idno": "SURVEY_DATASET_SAMPLE_03",
        "title": "[Example] Survey Dataset Sample 03 (RDF import)"
    },
    "study_info": {
        "nation": [
            {
                "name": "Bangladesh",
                "abbreviation": "BGD"
            }
        ]
    }
}

response = create_and_import.add_survey_dataset(
    dataset_id=dataset_id,
    repository_id=repository_id,
    access_policy=access_policy,
    published=published,
    overwrite=overwrite,
    doc_desc=doc_desc,
    study_desc=study_desc
)

print(response)


# add a resource by importing RDF

dataset_id = "SURVEY_DATASET_SAMPLE_03"
file = "resource_sample.rdf"

response = create_and_import.add_resource_from_RDF(
	dataset_id=dataset_id,
	file=file
)

print(response)