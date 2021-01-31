import pynada as nada
import inspect

nada.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = open("API Key.txt", "r").read()
nada.set_api_key(api_key)

################################
# create_table_dataset template
################################

dataset_id = "TABLE_DATASET_SAMPLE_01"
repository_id = "central"  # Collection ID that owns the document
published = 0  # Status: 0=draft, 1=published
overwrite = "yes"  # Overwrite document if already exists? Valid values: "yes" "no"
metadata_information = {
	"idno": "metadata info id",
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
table_description = {
	"title_statement": {
		"idno": dataset_id,  # Must be same as dataset_id
		"table_number": "table_no_01",  # Table number
		"title": "[Template] Table Dataset Sample 01",  # Table title
		"sub_title": "Table Dataset Sample 01 (sub_title)",  # A short subtitle for the table
		"alternate_title": "Table Dataset Sample 01 (alternate_title)",  # Any form of the title used as a substitute or alternative to the formal title of the resource.
		"abbreviated_title": "Table Dataset Sample 01 (abbreviated_title)"  # Title as abbreviated for indexing or identification.
	},
	"id_numbers": {
		"type": "ISSN",  # table ID number type such as ISSN, ISBN, DOI
		"value": "123456789"  # table ID number
	},
	"authoring_entity": [
		{
			"name": "authoring_entity name",
			"affiliation": "authoring_entity affiliation",
			"abbreviation": "authoring_entity abbreviation",
			"uri": "authoring_entity@example.org"
		}
	],
	"contributors": [
		{
			"name": "contributor name",
			"affiliation": "contributor affiliation",
			"abbreviation": "contributor abbreviation",
			"role": "contributor role",
			"uri": "contributor@example.org"
		}
	],
	"publisher": [
		{
			"name": "publisher name",
			"affiliation": "publisher affiliation",
			"abbreviation": "publisher abbreviation",
			"role": "publisher role",
			"uri": "publisher@example.org"
		}
	],
	"date_created": "2020-01-01",
	"date_published": "2020-10-01",
	"date_modified": "2020-11-01",
	"version": "v_0.0.1",
	"description": inspect.cleandoc("""\
		
		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
		Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. 
		Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, 
		sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. 
		
	"""),
	"table_columns": [  # List of table column names
		{
			"var_name": "table_column_var_name",
			"label": "table_column_label"
		}
	],
	"table_rows": [  # Table row level data
		{
			"var_name": "table_row_var_name",
			"label": "table_row_label"
		}
	],
	"table_footnotes": [
		{
			"number": "footnote_01",
			"text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
		}
	],
	"table_series": [
		{
			"name": "table_series name",
			"maintainer": "table_series maintainer",
			"uri": "http://example.org/table_description/table_series/uri",
			"description": inspect.cleandoc("""\
				
				Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, 
				sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. 
				
			"""),
		}
	],
	"statistics": [
		{
			"value": "table statistics"
		}
	],
	"unit_observation": [
		{
			"value": "table unit_observation"
		}
	],
	"data_sources": [
		{
			"source": "table data_source"
		}
	],
	"time_periods": [
		{
			"from": "2020-01-01",  # Date in ISO format (YYYY-MM-DD). Partial dates are supported
			"to": "2020-12-31"  # Date in ISO format (YYYY-MM-DD). Partial dates are supported
		}
	],
	"universe": [
		{
			"value": "table universe"
		}
	],
	"ref_country": [
		{
			"name": "templand",
			"code": "TMP"
		}
	],
	"geographic_units": [  # List of geographic units (regions, countries, states, provinces, etc.) for which data are available in the database.
		{
			"name": "Africa",  # Name of the geographic unit e.g. 'World', 'Africa', 'Afghanistan'
			"code": "geographic_units code",  # Code of the geographic unit (for countries, preferred = ISO3 code)
			"type": "geographic_units type"  # Type of geographic unit e.g. country, state, region, province etc
		}
	],
	"geographic_granularity": "national",  # Granularity of geographic coverage. examples national, regional, provincial
	"languages": [
		{
			"name": "table language name",
			"code": "table language code"
		}
	],
	"links": [
		{
			"uri": "http://example.org/table_description/link/uri",
			"description": "table link description"
		}
	],
	"publications": [
		{
			"title": "publication title",
			"uri": "http://example.org/table_description/publication/uri"
		}
	],
	"keywords": [
		{
			"name": "keyword name",
			"vocabulary": "keyword vocabulary",
			"uri": "http://example.org/table_description/keyword/uri"
		}
	],
	"themes": [
		{
			"name": "theme name",
			"vocabulary": "theme vocabulary",
			"uri": "http://example.org/table_description/theme/uri"
		}
	],
	"topics": [  # Topics covered by the table (ideally, the list of topics will be a controlled vocabulary)
		{
			"id": "table topic id",
			"name": "table topic name",
			"parent_id": "table topic parent_id",  # For subtopics, provide the ID of the parent topic
			"vocabulary": "table topic vocabulary",  # Name of the controlled vocabulary, if the topic is from a taxonomy.
			"uri": "http://example.org/table_description/topic/uri"  # Link to the controlled vocabulary web page, if the topic is from a taxonomy.
		}
	],
	"disciplines": [
		{
			"name": "discipline name",  # Disciplines e.g. Social sciences, economics, Natural sciences, biology
			"vocabulary": "discipline vocabulary",
			"uri": "http://example.org/table_description/discipline/uri"
		}
	],
	"definitions": [  # Definitions or concepts covered by the table
		{
			"name": "definition name",
			"definition": "definition text",
			"uri": "http://example.org/table_description/definition/uri"
		}
	],
	"classifications": [  # Classifications used in the table
		{
			"name": "classification name",
			"version": "classification version",
			"organization": "classification organization",  # Organization responsible for the classification
			"uri": "http://example.org/table_description/classification/uri"
		}
	],
	"rights": "table rights",
	"license": [
		{
			"name": "license name",
			"uri": "http://example.org/table_description/license/uri"
		}
	],
	"citation": "reference for the resource",  # A bibliographic reference for the resource.
	"confidentiality": "confidentiality text",
	"contacts": [
		{
			"name": "contact name",
			"role": "contact role",
			"affiliation": "contact affiliation",
			"email": "contact email",
			"telephone": "contact telephone",
			"uri": "contact@example.org"
		}
	],
	"notes": [
		{
			"note": inspect.cleandoc("""\
				
				Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, 
				sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. 
				Maecenas sed odio sem. In ut sapien luctus, lacinia est ut, rutrum nunc. Nam dignissim lacus a elit auctor, sed ultricies dui vestibulum. Interdum et malesuada fames ac ante ipsum primis in faucibus. 
				In nunc orci, congue eget justo id, rutrum hendrerit dui.
			"""),
		}
	],
	"relations": [
		{
			"name": "Related document name",
			"type": "isPartOf"  # "isPartOf""hasPart""isVersionOf""isFormatOf""hasFormat""references""isReferencedBy""isBasedOn""isBasisFor""requires""isRequiredBy"
		}
	]
}
files = [
	{
		"file_uri": "http://example.org/files/file.uri",  # File name or URL
		"format": "file format",  # The file format, physical medium, or dimensions of the resource.
		"location": "file location",
		"note": "file note"
	}
]
tags = [
	{
		"tag": "tag"
	}
]
additional = {
	"additional": "additional info"
}

response = nada.create_table_dataset(
	dataset_id=dataset_id,
	repository_id=repository_id,
	published=published,
	overwrite=overwrite,
	metadata_information=metadata_information,
	table_description=table_description,
	files=files,
	tags=tags,
	additional=additional
)


# upload temporary thumbnail
thumbnail_path = nada.text_to_thumbnail("Table\nDataset")
nada.upload_thumbnail(dataset_id, thumbnail_path)