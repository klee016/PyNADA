from pynada import create_and_import
from pynada import utils

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

#################################
# add_visualization_dataset test
#################################
dataset_id = "VISUALIZATION_DATASET_SAMPLE_01"

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
		"type": "ID number type",
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
			"name": "authoring_entity name",
			"affiliation": "authoring_entity affiliation",
			"abbreviation": "authoring_entity abbreviation",
			"uri": "http://example.org/visualization_description/authoring_entity/uri"
		}
	],
	"contributors": [
		{
			"name": "contributor name",
			"affiliation": "contributor affiliation",
			"abbreviation": "contributor abbreviation",
			"role": "contributor role",
			"uri": "http://example.org/visualization_description/contributors/uri"
		}
	],
	"publisher": [
		{
			"name": "publisher name",
			"affiliation": "publisher affiliation",
			"abbreviation": "publisher abbreviation",
			"role": "publisher role",
			"uri": "http://example.org/visualization_description/publisher/uri"
		}
	],
	"acknowledgements": {
		"name": "acknowledgement name",
		"role": "acknowledgement role"
	},
	"date_created": "date_created",
	"date_published": "date_published",
	"date_modified": "date_modified",
	"version": "version",
	"visualization_series": [
		{
			"name": "visualization_series name",
			"maintainer": "visualization_series maintainer",
			"uri": "http://example.org/visualization_description/visualization_series/uri",
			"description": "visualization_series description"
		}
	],
	"data_sources": [
		{
			"source": "data source"
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
			"value": "universe"
		}
	],
	"ref_country": [
		{
			"name": "ref_country name",
			"code": "ref_country code"
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
			"uri": "http://example.org/visualization_description/data/uri",
			"note": "visualization data note"
		}
	],
	"scripts": [
		{
			"software_name": "visualization script software_name",
			"software_version": "visualization script software_version",
			"software_library": "visualization script software_library",
			"script_access": "visualization script script_access",
			"script_uri": "http://example.org/visualization_description/scripts/uri"
		}
	],
	"embed_uri": "http://example.org/visualization_description/embed_uri/uri",
	"publications": [
		{
			"title": "publication title",
			"uri": "http://example.org/visualization_description/publications/uri"
		}
	],
	"keywords": [
		{
			"name": "keyword name",
			"vocabulary": "keyword vocabulary",
			"uri": "http://example.org/visualization_description/keywords/uri"
		}
	],
	"themes": [
		{
			"name": "visualization theme name",
			"vocabulary": "visualization theme vocabulary",
			"uri": "http://example.org/visualization_description/themes/uri"
		}
	],
	"topics": [
		{
			"id": "visualization topic id",
			"name": "visualization topic name",
			"parent_id": "visualization topic parent_id",
			"vocabulary": "visualization topic vocabulary",
			"uri": "http://example.org/visualization_description/topics/uri"
		}
	],
	"disciplines": [
		{
			"name": "discipline name",
			"vocabulary": "discipline vocabulary",
			"uri": "http://example.org/visualization_description/disciplines/uri"
		}
	],
	"definitions": [
		{
			"name": "definition name",
			"definition": "definition text",
			"uri": "http://example.org/visualization_description/definitions/uri"
		}
	],
	"classifications": [
		{
			"name": "classification name",
			"version": "classification version",
			"organization": "classification organization",
			"uri": "http://example.org/visualization_description/classifications/uri"
		}
	],
	"rights": "visualization rights",
	"license": [
		{
			"name": "license name",
			"uri": "http://example.org/visualization_description/license/uri"
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
			"uri": "http://example.org/visualization_description/contacts/uri"
		}
	],
	"notes": [
		{
			"note": "note text"
		}
	],
	"links": [
		{
			"uri": "http://example.org/visualization_description/links/uri",
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
	dataset_id=dataset_id,
	repository_id=repository_id,
	published=published,
	overwrite=overwrite,
	metadata_information=metadata_information,
	visualization_description=visualization_description,
	files=files,
	additional=additional
)

print(response)

utils.text_to_thumbnail("Visualization\nDataset")
create_and_import.add_thumbnail(idno, "temp_thumbnail.jpg")