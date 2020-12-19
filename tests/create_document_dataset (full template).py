from pynada import create_and_import
from pynada import utils
import inspect

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

###################################
# create_document_dataset template
###################################

dataset_id = "DOCUMENT-DATASET-SAMPLE-01"
repository_id = "string"  # Collection ID that owns the document
published = 0  # Status: 0=draft, 1=published
overwrite = "yes"  # Valid values: "yes" "no"
metadata_information = {
	"title": "metadata title",
	"idno": "metadata id",
	"producers": [
		{
			"name": "metadata producer name",
			"abbr": "metadata producer abbr",
			"affiliation": "metadata producer affiliation",
			"role": "metadata producer role"
		}
	],
	"production_date": "2020-12-31",  # Document production date using format(YYYY-MM-DD)
	"version": "metadata version"  # Identify and describe the current version of the document
}
document_description = {
	"title_statement": {
		"idno": dataset_id,  # Must be same as dataset_id
		"title": "[Template] Document Dataset Sample 01",
		"sub_title": "Document Dataset Sample 01 (sub_title)",
		"alternate_title": "Document Dataset Sample 01 (alternate_title)",
		"abbreviated_title": "Document Dataset Sample 01 (abbreviated_title)"
	},
	"type": "article",  # Valid values: "article" "book" "booklet" "collection" "conference" "inbook" "incollection" "inproceeding" "manual" "masterthesis" "patent" "phdthesis" "proceedings" "techreport" "working-paper" "website" "other"
	"description": "description",  # An account of the content of the resource.
	"toc": "Table of contents",  # Table of contents
	"toc_structured": [
		{
			"id": "TOC id",
			"parent_id": "parent TOC ID",  # For sub levels, provide the ID of the parent TOC ID
			"name": "TOC name"  # Title
		}
	],
	"abstract": inspect.cleandoc("""\
	
		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
		Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. 
		Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, 
		non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, 
		sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. 
		
	"""),  # A summary of the content
	"notes": [
		{
			"note": inspect.cleandoc("""\
	
				Maecenas sed odio sem. In ut sapien luctus, lacinia est ut, rutrum nunc. Nam dignissim lacus a elit auctor, sed ultricies dui vestibulum. Interdum et malesuada fames ac ante ipsum primis in faucibus.
				In nunc orci, congue eget justo id, rutrum hendrerit dui.
		
			""")
		}
	],
	"scope": "The extent or scope of the content of the resource.",  # This fields maps to Dublin Core's coverage field.
	"ref_country": [
		{
			"name": "ref_country",
			"code": "ISO"
		}
	],
	"spatial_coverage": inspect.cleandoc("""\
	
		Pellentesque vehicula nisl sed leo consequat, interdum congue diam maximus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec nec ex egestas, congue libero sit amet, tincidunt risus.
		Cras sed ligula pellentesque, efficitur ex nec, gravida sapien. Nulla mollis, tortor vitae ullamcorper iaculis, felis metus molestie massa, nec fringilla eros arcu quis tortor.

	"""),  # The spatial extent or scope of the content of the resource.
	"temporal_coverage": inspect.cleandoc("""\
	
		Pellentesque vehicula nisl sed leo consequat, interdum congue diam maximus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec nec ex egestas, congue libero sit amet, tincidunt risus.
		Cras sed ligula pellentesque, efficitur ex nec, gravida sapien. Nulla mollis, tortor vitae ullamcorper iaculis, felis metus molestie massa, nec fringilla eros arcu quis tortor.

	"""),  # The temporal extent or scope of the content of the resource.
	"date_created": "2020-12-31",  # Date of creation
	"date_available": "From 2020-01-01 To 2020-12-31",  # Date (often a range) that the resource will become or did become available.
	"date_modified": "2020-08-01",  # Date on which the resource was changed.
	"date_published": "2020-10-01",  # Date on which document was published.
	"id_numbers": [
		{
			"type": "ISSN",  # ID number type such as ISSN, ISBN, DOI
			"value": "123456789"
		}
	],
	"publication_frequency": "publication_frequency",  # Current stated publication frequency of either an item or an update to an item. Dates are included when the beginning date of the current frequency is not the same as the beginning date of publication.
	"languages": [
		{
			"name": "English",  # Documentation language
			"code": "ENG"
		}
	],
	"license": [
		{
			"name": "license name",
			"uri": "http://example.org/document_description/license/uri"
		}
	],
	"bibliographic_citation": "bibliographic_citation",  # A bibliographic reference for the resource.
	"chapter": "chapter",  # A chapter or section number
	"edition": "edition",  # The edition of a book
	"institution": "institution",  # The sponsoring institution of a document.
	"journal": "journal",  # Name of the Journal
	"volume": "volume",  # Volume number
	"issue": "issue",  # Issue number
	"pages": "7,53,82--94",  # One or more page numbers or ranges of number
	"series": "series",  # The name given to a series or set of books. When citing an entire book, the title field gives its title and the optional series field gives the name of a series in which the book was published.
	"creator": "creator",  # Entity primarily responsible for making the content of the resource.
	"authors": [
		{
			"first_name": "author first_name",
			"initial": "author initial",
			"last_name": "author last_name",
			"affiliation": "author affiliation"
		}
	],
	"editors": [
		{
			"first_name": "editor first_name",
			"initial": "editor initial",
			"last_name": "editor last_name",
			"affiliation": "editor affiliation"
		}
	],
	"translators": [
		{
			"first_name": "translator first_name",
			"initial": "translator initial",
			"last_name": "translator last_name",
			"affiliation": "translator affiliation"
		}
	],
	"contributors": [
		{
			"first_name": "contributor first_name",
			"initial": "contributor initial",
			"last_name": "contributor last_name",
			"affiliation": "contributor affiliation"
		}
	],
	"publisher": "publisher",  # Entity responsible for making the resource available
	"publisher_address": "publisher_address",  # For major publishing houses, just the city is given. For small publishers, you can help the reader by giving the complete address.
	"rights": "rights text",  # Information about rights held in and over the resource.
	"copyright": "copyright text",  # Statement and identifier indicating the legal ownership and rights regarding use and re-use of all or part of the resource.
	"usage_terms": "usage_terms",  # Terms Governing Use and Reproduction
	"security_classification": "security_classification",  # Specifics pertaining to the security classification associated with the document, title, abstract, contents note, and/or the author. In addition, it can contain handling instructions and external dissemination information pertaining to the dissemination of the document, title, abstract, contents note, and author.
	"access_restrictions": "access_restrictions",  # Information about restrictions imposed on access to the described materials.
	"sources": {
		"data_source": ['data source 1', 'data source 2'],
		"source_origin": "source_origin",
		"source_char": "source_char",  # Assessment of characteristics and quality of source material. May not be relevant to survey data.
		"source_doc": "source_doc"  # Documentation and Access to Sources
	},
	"keywords": [
		{
			"name": "keyword name",
			"vocabulary": "keyword name",
			"uri": "http://example.org/document_description/keyword/uri"
		}
	],
	"themes": [
		{
			"name": "theme name",
			"vocabulary": "theme vocabulary",
			"uri": "http://example.org/document_description/theme/uri"
		}
	],
	"topics": [  # Topics covered by the table (ideally, the list of topics will be a controlled vocabulary)
		{
			"id": "topic id",
			"name": "topic name",
			"parent_id": "topic parent_id",  # For subtopics, provide the ID of the parent topic
			"vocabulary": "topic vocabulary",  # Name of the controlled vocabulary, if the topic is from a taxonomy.
			"uri": "http://example.org/document_description/topics/uri"  # Link to the controlled vocabulary web page, if the topic is from a taxonomy.
		}
	],
	"disciplines": [
		{
			"name": "discipline name",  # e.g. Social sciences, economics, Natural sciences, biology
			"vocabulary": "discipline vocabulary",
			"uri": "http://example.org/document_description/discipline/uri"
		}
	],
	"audience": "audience",  # A category of user for whom the resource is intended.
	"mandate": "mandate",
	"pricing": "pricing",  # Current price of an item or the special export price of an item in any currency.
	"relations": [  # Related documents
		{
			"name": "related document name",
			"type": "isPartOf"  # Valid values: "isPartOf" "hasPart" "isVersionOf" "isFormatOf" "hasFormat" "references" "isReferencedBy" "isBasedOn" "isBasisFor" "requires" "isRequiredBy"
		}
	],
	"lda_topics": [
		{
			"model_info": [
				{
					"source": "LDA topics model source",
					"author": "LDA topics model author",
					"version": "LDA topics model version",
					"model_id": "LDA topics model_id",
					"nb_topics": 0,
					"description": "LDA topics model description",
					"corpus": "LDA topics model corpus",
					"uri": "http://example.org/document_description/lda_topics/model_info/uri"
				}
			],
			"topic_description": [
				{
					"topic_id": "LDA topics id",
					"topic_score": "LDA topics score",
					"topic_label": "LDA topics label",
					"topic_words": [
						{
							"word": "LDA topics word",
							"word_weight": 0
						}
					]
				}
			],
			"word_vectors": [
				{
					"id": "word_vectors id",
					"description": "word_vectors description",
					"date": "2020-12-31",
					"vector": {}
				}
			]
		}
	]
}
tags = [
	{
		"tag": "tag"
	}
]
files = [
	{
		"file_uri": "http://example.org/files/file.uri",  # File name or URL
		"format": "application/excel",  # The file format, physical medium, or dimensions of the resource.
		"location": "100",  # Page number or sheet name for the table
		"note": "file note text"  # file note
	}
]

response = create_and_import.create_document_dataset(
	dataset_id=dataset_id,
	repository_id=repository_id,
	published=published,
	overwrite=overwrite,
	metadata_information=metadata_information,
	document_description=document_description,
	tags=tags,
	files=files
)

print(response)

# upload temporary thumbnail
thumbnail_path = utils.text_to_thumbnail("Document\nDataset")
create_and_import.upload_thumbnail(dataset_id, thumbnail_path)