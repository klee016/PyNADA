from pynada import create_and_import
from pynada import utils

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

##############################
# add_timeseries_dataset test
##############################
idno = "TIMESERIES_DATASET_SAMPLE_01"

repositoryid = "central"  # Collection that owns the series
access_policy = "na"  # Valid values - "direct" "open" "public" "licensed" "remote" "na"
data_remote_url = "http://example.org/data_remote_url"  # Link to the website where the data is available, this is only needed if access_policy is set to "remote".
published = 0  # 0=draft, 1=published
overwrite = "yes"  # Valid values - "yes" "no"
metadata_creation = {  # Information on who generated the documentation
	"producers": [
		{
			"name": "timeseries producer name",
			"abbr": "timeseries producer abbr",
			"affiliation": "timeseries producer affiliation",
			"role": "timeseries producer name"
		}
	],
	"prod_date": "2020-12-31",  # Document production date using format(YYYY-MM-DD)
	"version": "1.0.0"  # Identify and describe the current version of the document
}
series_description = {
	"idno": "TIMESERIES_DATASET_SAMPLE_01",  # Unique series ID
	"name": "TIMESERIES DATASET SAMPLE 01",
	"database_id": "TimeseriesDB ID",
	"aliases": [
		{
			"alias": "timeseries alias"
		}
	],
	"measurement_unit": "unit",  # Series unit of measure
	"periodicity": "timeseries periodicity",
	"base_period": "timeseries base_period",
	"definition_short": "timeseries definition_short",
	"definition_long": "timeseries definition_long ",
	"definition_references": [  # URL to standard definition of the indicator (international or national standard)
		{
			"source": "definition_reference source",
			"uri": "http://example.org/series_description/definition_references/uri",
			"note": "definition_reference note"
		}
	],
	"statistical_concept": "timeseries statistical_concept",
	"concepts": [  # Related concepts
		{
			"name": "concept name",
			"definition": "concept definition",
			"uri": "http://example.org/series_description/concepts/uri"
		}
	],
	"methodology": "methodology used",
	"imputation": "imputation used",
	"quality_checks": "Quality control methods",
	"quality_note": "Note on data quality",
	"series_break": "Breaks in series",
	"limitation": "Limitations and exceptions",
	"themes": [
		{
			"name": "timeseries theme name",
			"vocabulary": "timeseries theme vocabulary",
			"uri": "http://example.org/series_description/themes/uri"
		}
	],
	"topics": [  # Topics covered by the timeseries (ideally, the list of topics will be a controlled vocabulary)
		{
			"id": "timeseries topic id",
			"name": "timeseries topic name",
			"parent_id": "timeseries topic parent_id",  # For subtopics, provide the ID of the parent topic
			"vocabulary": "timeseries topic vocabulary",  # Name of the controlled vocabulary, if the topic is from a taxonomy.
			"uri": "http://example.org/series_description/topics/uri"  # Link to the controlled vocabulary web page, if the topic is from a taxonomy.
		}
	],
	"disciplines": [  # Disciplines e.g. Social sciences, economics, Natural sciences, biology
		{
			"name": "discipline name",
			"vocabulary": "discipline vocabulary",
			"uri": "http://example.org/series_description/disciplines/uri"
		}
	],
	"relevance": "relevance",
	"time_periods": [
		{
			"start": "time_period start",
			"end": "time_period end"
		}
	],
	"geographic_units": [  # List of geographic units (regions, countries, states, provinces, etc.) for which data are available in the database.
		{
			"name": "geographic_units name",  # Name of the geographic unit e.g. 'World', 'Africa', 'Afghanistan'
			"code": "geographic_units code",  # Code of the geographic unit (for countries, preferred = ISO3 code)
			"type": "geographic_units type"  # Type of geographic unit e.g. country, state, region, province etc
		}
	],
	"aggregation_method": "aggregation_method",
	"license": {
		"name": "access licence name",
		"uri": "http://example.org/series_description/license/uri"
	},
	"confidentiality": "confidentiality statement",
	"confidentiality_status": "confidentiality status",
	"confidentiality_note": "confidentiality note",
	"links": [  # Links to API calls, websites, etc.
		{
			"type": "API",  # e.g. API, website
			"description": "link description",
			"uri": "http://example.org/series_description/links/uri"
		}
	],
	"api_documentation": {
		"description": "api_documentation description",
		"uri": "http://example.org/series_description/api_documentation/uri"
	},
	"source": "Original source",
	"source_note": "Notes form original source",
	"keywords": [
		{
			"name": "keyword name",
			"vocabulary": "keyword name",
			"uri": "http://example.org/series_description/keywords/uri"
		}
	],
	"acronyms": [
		{
			"acronym": "AOA",  # Acronym or abbreviation
			"expansion": "Expansion of the acronym or abbreviation",
			"occurrence": 0
		}
	],
	"notes": [
		{
			"note": "note text"
		}
	],
	"related_indicators": [
		{
			"code": "Related indicator code",
			"label": "Related indicator label",
			"uri": "http://example.org/series_description/related_indicators/uri"
		}
	],
	"compliance": [  # Compliance with international resolution
		{
			"standard": "compliance standard",
			"organization": "compliance organization",
			"uri": "http://example.org/series_description/compliance/uri"
		}
	],
	"lda_topics": [
		{
			"model_info": [
				{
					"source": "LDA topic model source",
					"author": "LDA topic model author",
					"version": "LDA topic model version",
					"model_id": "LDA topic model model_id",
					"nb_topics": 0,  # Number of topics
					"description": "LDA topic model description",
					"corpus": "LDA topic model corpus",
					"uri": "http://example.org/series_description/lda_topics/model_info/uri"
				}
			],
			"topic_description": [
				{
					"topic_id": "LDA topic_id",  # int or str
					"topic_score": "LDA topic_score",  # int or str
					"topic_label": "LDA topic_label",
					"topic_words": [
						{
							"word": "LDA topic word",
							"word_weight": 0
						}
					]
				}
			]
		}
	],
	"word_vectors": [
		{
			"id": "Vector Model ID",
			"description": "Vector Model Description",
			"date": "2020-12-31",
			"vector": {}
		}
	],
	"series_groups": [  # Series included in groups
		{
			"name": "series_group name",
			"version": "series_group version",
			"uri": "http://example.org/series_groups/uri"
		}
	]
}
additional = {}

response = create_and_import.add_timeseries_dataset(
	idno=idno,
	repositoryid=repositoryid,
	access_policy=access_policy,
	published=published,
	overwrite=overwrite,
	metadata_creation=metadata_creation,
	series_description=series_description,
	additional=additional
)

print(response)

utils.text_to_thumbnail("Timeseries\nDataset")
create_and_import.add_thumbnail(idno, "temp_thumbnail.jpg")