import pynada as nada
import inspect

nada.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
nada.set_api_key(api_key)

#############################
# add_table_dataset template
#############################

dataset_id = "TABLE_DATASET_SAMPLE_01"
repository_id = "central"
published = 0
overwrite = "yes"
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
	"production_date": "2020-12-31",
	"version": "metadata version"
}
table_description = {
	"title_statement": {
		"idno": "TABLE_DATASET_SAMPLE_01",
		"table_number": "table_no_01",
		"title": "[Template] Table Dataset Sample 01",
		"sub_title": "Table Dataset Sample 01 (sub_title)",
		"alternate_title": "Table Dataset Sample 01 (alternate_title)",
		"abbreviated_title": "Table Dataset Sample 01 (abbreviated_title)"
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
	"table_columns": [
		{
			"var_name": "table_column_var_name",
			"label": "table_column_label"
		}
	],
	"table_rows": [
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
			"from": "2020-01-01",
			"to": "2020-12-31"
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
	"geographic_units": [
		{
			"name": "geographic_units name",
			"code": "geographic_units code",
			"type": "geographic_units type"
		}
	],
	"geographic_granularity": "geographic_granularity",
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
	"topics": [
		{
			"id": "table topic id",
			"name": "table topic name",
			"parent_id": "table topic parent_id",
			"vocabulary": "table topic vocabulary",
			"uri": "http://example.org/table_description/topic/uri"
		}
	],
	"disciplines": [
		{
			"name": "discipline name",
			"vocabulary": "discipline vocabulary",
			"uri": "http://example.org/table_description/discipline/uri"
		}
	],
	"definitions": [
		{
			"name": "definition name",
			"definition": "definition text",
			"uri": "http://example.org/table_description/definition/uri"
		}
	],
	"classifications": [
		{
			"name": "classification name",
			"version": "classification version",
			"organization": "classification organization",
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
	"citation": "reference for the resource",
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
			"type": "isPartOf"
		}
	]
}
files = [
	{
		"file_uri": "file_uri",
		"format": "file format",
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

response = nada.add_table_dataset(
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

print(response)

thumbnail_path = nada.text_to_thumbnail("Table\nDataset")
nada.add_thumbnail(dataset_id, thumbnail_path)