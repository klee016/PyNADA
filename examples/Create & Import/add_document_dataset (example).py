import pynada as nada

nada.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
nada.set_api_key(api_key)


##################################
# create_document_dataset example
##################################

dataset_id = "DOCUMENT-DATASET-SAMPLE-02"
repository_id = "central"
published = 1
overwrite = "yes"
document_description = {
    "title_statement": {
        "title": "[Example] Document Dataset Sample 02",
        "idno": "DOCUMENT-DATASET-SAMPLE-02"
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


response = nada.create_document_dataset(
    dataset_id=dataset_id,
    repository_id=repository_id,
    published=published,
    overwrite=overwrite,
    document_description=document_description,
    files=files
)

print(response)


# If you have pdf file, generate thumbnail from it.
pdf_file_path = 'WPS8038.pdf'
thumbnail_path = nada.pdf_to_thumbnail(pdf_file_path, page_no = 1)
nada.upload_thumbnail(dataset_id, thumbnail_path)