from pynada import create_and_import
from pynada import utils
import inspect

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

#####################################
# create_timeseries_dataset template
#####################################

dataset_id = "TIMESERIES_DATASET_SAMPLE_01"
repository_id = "central"  # Collection ID that owns the series
access_policy = "na"  # Data access policy for attached microdata resources. Valid values - "direct" "open" "public" "licensed" "remote" "na"
data_remote_url = "http://example.org/data_remote_url"  # Link to the website where the data is available, this is only needed if access_policy is set to "remote".
published = 0  # Status of the study: 0=draft, 1=published
overwrite = "yes"  # Overwrite database if already exists? Valid values - "yes" "no"
metadata_creation = {  # Information on who generated the documentation
	"producers": [
		{
			"name": "producer name",
			"abbr": "producer abbr",
			"affiliation": "producer affiliation",
			"role": "producer name"
		}
	],
	"prod_date": "2020-12-31",  # Document production date using format(YYYY-MM-DD)
	"version": "v_0.0.1"  # Identify and describe the current version of the document
}
series_description = {
	"idno": dataset_id,  # Must be same as dataset_id
	"name": "[Template] Timeseries Dataset Sample 01",
	"database_id": "TimeseriesDB_01",
	"aliases": [
		{
			"alias": "timeseries_alias"
		}
	],
	"measurement_unit": "unit",  # Series unit of measure
	"periodicity": "timeseries periodicity",
	"base_period": "timeseries base_period",
	"definition_short": "timeseries definition_short",
	"definition_long": inspect.cleandoc("""\
				
		Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, 
		sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. 
		
	"""),
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
	"methodology": inspect.cleandoc("""\
				
		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. Nulla eget lacinia leo, at rutrum nibh. 
		Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue.
		
	"""),
	"imputation": inspect.cleandoc("""\
				
		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. Nulla eget lacinia leo, at rutrum nibh. 
		Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue.
		
	"""),
	"quality_checks": "Quality control methods",
	"quality_note": "Note on data quality",
	"series_break": "Breaks in series",
	"limitation": inspect.cleandoc("""\
				
		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. Nulla eget lacinia leo, at rutrum nibh. 
		Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue.
		
	"""),
	"themes": [
		{
			"name": "timeseries theme name",
			"vocabulary": "timeseries theme vocabulary",
			"uri": "http://example.org/series_description/themes/uri"
		}
	],
	"topics": [  # Topics covered by the timeseries (ideally, the list of topics will be a controlled vocabulary)
		{
			"id": "topic_id",
			"name": "topic name",
			"parent_id": "topic parent_id",  # For subtopics, provide the ID of the parent topic
			"vocabulary": "topic vocabulary",  # Name of the controlled vocabulary, if the topic is from a taxonomy.
			"uri": "http://example.org/series_description/topics/uri"  # Link to the controlled vocabulary web page, if the topic is from a taxonomy.
		}
	],
	"disciplines": [
		{
			"name": "discipline name",  # Disciplines e.g. Social sciences, economics, Natural sciences, biology
			"vocabulary": "discipline vocabulary",
			"uri": "http://example.org/series_description/disciplines/uri"
		}
	],
	"relevance": "relevance",
	"time_periods": [
		{
			"start": "2020-01-01",
			"end": "2020-12-31"
		}
	],
	"geographic_units": [  # List of geographic units (regions, countries, states, provinces, etc.) for which data are available in the database.
		{
			"name": "Templand",  # Name of the geographic unit e.g. 'World', 'Africa', 'Afghanistan'
			"code": "TMP",  # Code of the geographic unit (for countries, preferred = ISO3 code)
			"type": "geographic_units type"  # Type of geographic unit e.g. country, state, region, province etc
		}
	],
	"aggregation_method": "aggregation_method",
	"license": {
		"name": "access licence name",
		"uri": "http://example.org/series_description/license/uri"
	},
	"confidentiality": inspect.cleandoc("""\
				
		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus.
		Maecenas sed odio sem. In ut sapien luctus, lacinia est ut, rutrum nunc. 
		
	"""),
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
			"note": inspect.cleandoc("""\
		
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
			Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus.
			Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, sit amet tempus eros tristique eu. 
			Morbi ultrices mauris dignissim lacus dapibus efficitur. 
			
		"""),
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
additional = {}  # Any other custom metadata not covered by the schema

response = create_and_import.create_timeseries_dataset(
	dataset_id=dataset_id,
	repository_id=repository_id,
	access_policy=access_policy,
	published=published,
	overwrite=overwrite,
	metadata_creation=metadata_creation,
	series_description=series_description,
	additional=additional
)

print(response)

# upload temporary thumbnail
thumbnail_path = utils.text_to_thumbnail("Timeseries\nDataset")
create_and_import.upload_thumbnail(dataset_id, thumbnail_path)