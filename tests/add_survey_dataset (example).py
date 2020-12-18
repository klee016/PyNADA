from pynada import create_and_import

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

##################
# add_survey test
##################
dataset_id = "survey-add-test-01"
repository_id = "central"
access_policy = "data_na"
published = 0
overwrite = "yes"
doc_desc = {
    "title": "test survey 01",
    "idno": "survey-doc-01",
    "producers": [
        {
            "name": "Kamwoo Lee",
            "abbr": "KL",
            "affiliation": "DECAT",
            "role": "test"
        },
    ],
    "prod_date": "2020-12-08",
    "version_statement": {
        "version": "0.1",
        "version_date": "2020-12-08",
        "version_resp": "test",
        "version_notes": "test"
    },
}
study_desc = {
    "title_statement": {
        "idno": "survey-add-test-01",
        "title": "test title",
        "sub_title": "test sub title",
        "alternate_title": "test alternate title",
        "translated_title": "test translated title"
    },
    "authoring_entity": [
        {
            "name": "WB",
            "affiliation": "test"
        }
    ],
    "oth_id": [
        {
            "name": "KL",
            "role": "test",
            "affiliation": "test"
        }
    ],
    "study_info": {
        "nation": [
            {
                "name": "Bangladesh",
                "abbreviation": "BGD"
            }
        ]
    }
}

response = create_and_import.create_survey_dataset(
    dataset_id=dataset_id,
    repository_id=repository_id,
    access_policy=access_policy,
    published=published,
    overwrite=overwrite,
    doc_desc=doc_desc,
    study_desc=study_desc
)

print(response)
