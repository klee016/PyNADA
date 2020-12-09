from pynada import create_dataset

create_dataset.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_dataset.set_api_key(api_key)

##################
# add_survey test
##################
# idno = "survey-add-test-01"
# repositoryid = "central"
# access_policy = "data_na"
# published = 0
# overwrite = "no"
# doc_desc = {
#     "title": "test survey 01",
#     "idno": "survey-doc-01",
#     "producers": [
#         {
#             "name": "Kamwoo Lee",
#             "abbr": "KL",
#             "affiliation": "DECAT",
#             "role": "test"
#         },
#     ],
#     "prod_date": "2020-12-08",
#     "version_statement": {
#         "version": "0.1",
#         "version_date": "2020-12-08",
#         "version_resp": "test",
#         "version_notes": "test"
#     },
# }
# study_desc = {
#     "title_statement": {
#         "idno": "survey-add-test-01",
#         "title": "test title",
#         "sub_title": "test sub title",
#         "alternate_title": "test alternate title",
#         "translated_title": "test translated title"
#     },
#     "authoring_entity": [
#         {
#             "name": "WB",
#             "affiliation": "test"
#         }
#     ],
#     "oth_id": [
#         {
#             "name": "KL",
#             "role": "test",
#             "affiliation": "test"
#         }
#     ],
#     "study_info": {
#         "nation": [
#             {
#                 "name": "Bangladesh",
#                 "abbreviation": "BGD"
#             }
#         ]
#     }
# }
#
# response = create_dataset.add_survey(
#     idno=idno,
#     repositoryid=repositoryid,
#     access_policy=access_policy,
#     published=published,
#     overwrite=overwrite,
#     doc_desc=doc_desc,
#     study_desc=study_desc
# )
#
# print(response)


####################
# add_document test
####################
idno = "WPS8038"
repositoryid = "central"
published = 1
overwrite = "yes"
document_description = {
    "title_statement": {
        "title": "The economics of forced displacement: An introduction",
        "idno": "WPS8038"
    },
    "date_published": "2017-04-25",
    "authors": [
        {
            "last_name": "Verme",
            "first_name": "Paolo",
            "affiliation": "World Bank"
        }
    ],
    "journal": "World Bank Policy Research Working Paper No. 8038",
    "abstract": "Forced displacement -- defined as the displacement of refugees and internally displaced persons due to violence -- has reached an unprecedented scale and global attention during the past few years, particularly in the aftermath of the Syrian refugee crisis in 2011 and the European Union's migration crisis in 2015. As this plight gained momentum, economics found itself unprepared to answer the basic questions surrounding refugees and internally displaced persons. Few economists or institutions were working on forced displacement. Economic theory or empirics had little to offer in articles published in journals. Data were scarce, unreliable, or inaccessible. Can economics rise to the challenge? Is the economics of forced displacement different from neoclassical economics? Can off-the-shelves models be used to study forced displaced populations? What is missing to do the economics of forced displacement? What are the data constraints that limit economists in this work? This paper provides a first nontechnical introduction to these topics. The paper argues that the modeling of utility, choice, risk, and information in a short-term setting is the key to address the problem. Neoclassical economics lacks some of the theoretical ingredients that are needed, but recent developments in game theory, neuroeconomics, and behavioral economics have opened new horizons that make the task of modeling forced displacement within reach. Empirics is clearly limited by the scarcity of quality data, but an example shows how welfare economists can start working with existing data. Economists have no excuse to maintain the status quo and should get on with the work on forced displacement.",
    "languages": [
        {
            "name": "English",
            "code": "EN"
        }
    ]
}
files = [
    {
        "file_uri": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2958540"
    }
]


response = create_dataset.add_document(
    idno=idno,
    repositoryid=repositoryid,
    published=published,
    overwrite=overwrite,
    document_description=document_description,
    files=files
)

print(response)
