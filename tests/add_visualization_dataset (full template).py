from pynada import create_and_import

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

#################################
# add_visualization_dataset test
#################################
idno = "VISUALIZATION_DATASET_SAMPLE_01"

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
visualization_description = {
	"title_statement": {
		"idno": "VISUALIZATION_DATASET_SAMPLE_01",
		"visualization_number": "visualization_number",
		"title": "VISUALIZATION DATASET SAMPLE 01 (full title)",
		"sub_title": "VISUALIZATION DATASET SAMPLE 01 (sub_title)",
		"alternate_title": "VISUALIZATION DATASET SAMPLE 01 (alternate_title)",
		"abbreviated_title": "VISUALIZATION DATASET SAMPLE 01 (abbreviated_title)",
		"legend": "visualization legend"
	},
	"sub_chart_titles": [
		{
			"title": "title for each chart"
		}
	],
	"chart_footnotes": [
		{
			"number": "chart_footnote number",
			"text": "chart_footnote text"
		}
	],
	"id_numbers": {
		"type": "ID number type such as DOI",
		"value": "ID number"
	},
	"visualization_types": [
		{
			"type": "visualization_type",
			"note": "visualization_type note"
		}
	],
	"animated": True,
	"description": "visualization description",
	"narrative": [
		"visualization narrative"
	],
	"authoring_entity": [
		{
			"name": "visualization authoring_entity name",
			"affiliation": "visualization authoring_entity affiliation",
			"abbreviation": "visualization authoring_entity abbreviation",
			"uri": "visualization authoring_entity uri"
		}
	],
	"contributors": [
		{
			"name": "visualization contributor name",
			"affiliation": "visualization contributor affiliation",
			"abbreviation": "visualization contributor abbreviation",
			"role": "visualization contributor role",
			"uri": "visualization contributor uri"
		}
	],
	"publisher": [
		{
			"name": "visualization publisher name",
			"affiliation": "visualization publisher affiliation",
			"abbreviation": "visualization publisher abbreviation",
			"role": "visualization publisher role",
			"uri": "visualization publisher uri"
		}
	],
	"acknowledgements": {
		"name": "visualization acknowledgement name",
		"role": "visualization acknowledgement role"
	},
	"date_created": "visualization date_created",
	"date_published": "visualization date_published",
	"date_modified": "visualization date_modified",
	"version": "visualization version",
	"visualization_series": [
		{
			"name": "visualization_series name",
			"maintainer": "visualization_series maintainer",
			"uri": "visualization_series uri",
			"description": "visualization_series description"
		}
	],
	"data_sources": [
		{
			"source": "visualization data source"
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
			"value": "visualization universe"
		}
	],
	"ref_country": [
		{
			"name": "visualization ref_country name",
			"code": "visualization ref_country code"
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
			"name": "visualization language name",
			"code": "visualization language code"
		}
	],
	"data_accessibility": "visualization data_accessibility",
	"data": [
		{
			"dataset": "visualization data dataset",
			"access_type": "visualization data access_type",
			"uri": "visualization data uri",
			"note": "visualization data note"
		}
	],
	"scripts": [
		{
			"software_name": "visualization script software_name",
			"software_version": "visualization script software_version",
			"software_library": "visualization script software_library",
			"script_access": "visualization script script_access",
			"script_uri": "visualization script script_uri"
		}
	],
	"embed_uri": "visualization embed_uri",
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
			"name": "visualization theme name",
			"vocabulary": "visualization theme vocabulary",
			"uri": "visualization theme uri"
		}
	],
	"topics": [
		{
			"id": "visualization topic id",
			"name": "visualization topic name",
			"parent_id": "visualization topic parent_id",
			"vocabulary": "visualization topic vocabulary",
			"uri": "visualization topic uri"
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
	"rights": "visualization rights",
	"license": [
		{
			"name": "license name",
			"uri": "license uri"
		}
	],
	"citation": "reference for the resource",
	"disclaimer": "disclaimer text",
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
	"links": [
		{
			"uri": "visualization link uri",
			"description": "visualization link description"
		}
	],
	"relations": [
		{
			"name": "Related document name",
			"type": "isPartOf"
		}
	],
	"tags": [
		{
			"tag": "tag"
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
additional = {
	"additional": "additional info"
}

response = create_and_import.add_visualization_dataset(
	idno=idno,
	repositoryid=repositoryid,
	published=published,
	overwrite=overwrite,
	metadata_information=metadata_information,
	visualization_description=visualization_description,
	files=files,
	additional=additional
)

print(response)
