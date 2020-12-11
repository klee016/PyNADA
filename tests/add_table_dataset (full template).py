from pynada import create_and_import

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

##########################
# add_table_dataset test
##########################
idno = "TABLE_DATASET_SAMPLE_01"

repositoryid = "string"
published = 0
overwrite = "no"
metadata_information = {
	"idno": "metadata info id",
	"producers": [
		{
			"name": "metadata_information producer name",
			"abbr": "metadata_information producer abbr",
			"affiliation": "metadata_information producer affiliation",
			"role": "metadata_information producer role"
		}
	],
	"production_date": "2020-12-31",
	"version": "metadata_information version"
}
table_description = {
	"title_statement": {
		"idno": "TABLE_DATASET_SAMPLE_01",
		"table_number": "table_number",
		"title": "TABLE DATASET SAMPLE 01 (full title)",
		"sub_title": "TABLE DATASET SAMPLE 01 (sub_title)",
		"alternate_title": "TABLE DATASET SAMPLE 01 (alternate_title)",
		"abbreviated_title": "TABLE DATASET SAMPLE 01 (abbreviated_title)"
	},
	"id_numbers": {
		"type": "table ID number type such as ISSN, ISBN, DOI",
		"value": "table ID number"
	},
	"authoring_entity": [
		{
			"name": "table authoring_entity name",
			"affiliation": "table authoring_entity affiliation",
			"abbreviation": "table authoring_entity abbreviation",
			"uri": "table authoring_entity uri"
		}
	],
	"contributors": [
		{
			"name": "table contributor name",
			"affiliation": "table contributor affiliation",
			"abbreviation": "table contributor abbreviation",
			"role": "table contributor role",
			"uri": "table contributor uri"
		}
	],
	"publisher": [
		{
			"name": "table publisher name",
			"affiliation": "table publisher affiliation",
			"abbreviation": "table publisher abbreviation",
			"role": "table publisher role",
			"uri": "table publisher uri"
		}
	],
	"date_created": "table date_created",
	"date_published": "table date_published",
	"date_modified": "table date_modified",
	"version": "table version",
	"description": "table description",
	"table_columns": [
		{
			"var_name": "table_column var_name",
			"label": "table_column label"
		}
	],
	"table_rows": [
		{
			"var_name": "table_row var_name",
			"label": "table_row label"
		}
	],
	"table_footnotes": [
		{
			"number": "table_footnote number",
			"text": "table_footnote text"
		}
	],
	"table_series": [
		{
			"name": "table_series name",
			"maintainer": "table_series maintainer",
			"uri": "table_series uri",
			"description": "table_series description"
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
			"name": "table ref_country name",
			"code": "table ref_country code"
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
			"uri": "table link uri",
			"description": "table link description"
		}
	],
	"publications": [
		{
			"title": "publication title",
			"uri": "publication uri"
		}
	],
	"keywords": [
		{
			"name": "keyword name",
			"vocabulary": "keyword vocabulary",
			"uri": "keyword uri"
		}
	],
	"themes": [
		{
			"name": "table theme name",
			"vocabulary": "table theme vocabulary",
			"uri": "table theme uri"
		}
	],
	"topics": [
		{
			"id": "table topic id",
			"name": "table topic name",
			"parent_id": "table topic parent_id",
			"vocabulary": "table topic vocabulary",
			"uri": "table topic uri"
		}
	],
	"disciplines": [
		{
			"name": "discipline name",
			"vocabulary": "discipline vocabulary",
			"uri": "discipline uri"
		}
	],
	"definitions": [
		{
			"name": "definition name",
			"definition": "definition text",
			"uri": "definition uri"
		}
	],
	"classifications": [
		{
			"name": "classification name",
			"version": "classification version",
			"organization": "classification organization",
			"uri": "classification uri"
		}
	],
	"rights": "table rights",
	"license": [
		{
			"name": "license name",
			"uri": "license uri"
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
			"uri": "contact uri"
		}
	],
	"notes": [
		{
			"note": "note text"
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

response = create_and_import.add_table_dataset(
	idno=idno,
	repositoryid=repositoryid,
	published=published,
	overwrite=overwrite,
	metadata_information=metadata_information,
	table_description=table_description,
	files=files,
	tags=tags,
	additional=additional
)

print(response)
