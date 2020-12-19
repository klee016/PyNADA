import pynada as nada
import inspect

nada.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
nada.set_api_key(api_key)

########################################
# create_visualization_dataset template
########################################

dataset_id = "VISUALIZATION_DATASET_SAMPLE_01"
repository_id = "central"  # Collection ID that owns the document
published = 0  # Status: 0=draft, 1=published
overwrite = "yes"  # Overwrite document if already exists? Valid values "yes" "no"
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
visualization_description = {
	"title_statement": {
		"idno": dataset_id,  # Must be same as dataset_id
		"visualization_number": "visualization_no_01",
		"title": "[Template] Visualization Dataset Sample 01",
		"sub_title": "Visualization Dataset Sample 01 (sub_title)",  # A short subtitle for the table
		"alternate_title": "Visualization Dataset Sample 01 (alternate_title)",  # Any form of the title used as a substitute or alternative to the formal title of the resource.
		"abbreviated_title": "Visualization Dataset Sample 01 (abbreviated_title)",  # Title as abbreviated for indexing or identification.
		"legend": "legend"  # Legend for the visualization
	},
	"sub_chart_titles": [  # Titls for each chart included in the visualization
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
	"id_numbers": {  # Numbers e.g. Any unique identifiers such as DOI
		"type": "ID number type",  # ID number type such as DOI
		"value": "type_ID_01"
	},
	"visualization_types": [
		{
			"type": "visualization_type",  # Visualization type e.g. scatter plot, line chart, choropleth
			"note": "visualization_type note"
		}
	],
	"animated": True,  # Visualization uses animation?
	"description": inspect.cleandoc("""\
		
		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
		Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. 
		Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, 
		sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. 
		
	"""),
	"narrative": [
		"visualization narrative"
	],
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
	"acknowledgements": {
		"name": "acknowledgement name",  # Name of the person or organization
		"role": "acknowledgement role"
	},
	"date_created": "2020-10-01",
	"date_published": "2020-11-31",
	"date_modified": "2020-12-31",
	"version": "v_0.0.1",
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
			"from": "2020-01-01",  # Date in ISO format (YYYY-MM-DD). Partial dates are supported
			"to": "2020-12-31"  # Date in ISO format (YYYY-MM-DD). Partial dates are supported
		}
	],
	"universe": [
		{
			"value": "universe"
		}
	],
	"ref_country": [
		{
			"name": "Templand",
			"code": "TMP"
		}
	],
	"geographic_units": [  # List of geographic units (regions, countries, states, provinces, etc.) for which data are available in the database.
		{
			"name": "geographic_units name",  # Name of the geographic unit e.g. 'World', 'Africa', 'Afghanistan'
			"code": "geographic_units code",  # Code of the geographic unit (for countries, preferred = ISO3 code)
			"type": "geographic_units type"  # Type of geographic unit e.g. country, state, region, province etc
		}
	],
	"geographic_granularity": "geographic_granularity",  # Granularity of geographic coverage. examples national, regional, provincial
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
			"access_type": "visualization data access_type",  # Data accessible via `API`, `Bulk download`, `Embedded in script`, etc (string)
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
	"embed_uri": "http://example.org/visualization_description/embed_uri/uri",  # Link for embedding the visualization
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
			"name": "theme name",
			"vocabulary": "theme vocabulary",
			"uri": "http://example.org/visualization_description/themes/uri"
		}
	],
	"topics": [  # Topics covered by the visualization (ideally, the list of topics will be a controlled vocabulary)
		{
			"id": "topic id",
			"name": "topic name",
			"parent_id": "topic parent_id",  # For subtopics, provide the ID of the parent topic
			"vocabulary": "topic vocabulary",  # Name of the controlled vocabulary, if the topic is from a taxonomy.
			"uri": "http://example.org/visualization_description/topics/uri"  # Link to the controlled vocabulary web page, if the topic is from a taxonomy.
		}
	],
	"disciplines": [
		{
			"name": "discipline name",  # Disciplines e.g. Social sciences, economics, Natural sciences, biology
			"vocabulary": "discipline vocabulary",
			"uri": "http://example.org/visualization_description/disciplines/uri"
		}
	],
	"definitions": [  # Definitions or concepts covered by the visualization
		{
			"name": "definition name",
			"definition": "definition text",
			"uri": "http://example.org/visualization_description/definitions/uri"
		}
	],
	"classifications": [  # Classifications used in the visualization
		{
			"name": "classification name",
			"version": "classification version",
			"organization": "classification organization",  # Organization responsible for the classification
			"uri": "http://example.org/visualization_description/classifications/uri"
		}
	],
	"rights": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
	"license": [
		{
			"name": "license name",
			"uri": "http://example.org/visualization_description/license/uri"
		}
	],
	"citation": "reference for the resource",  # A bibliographic reference for the resource.
	"disclaimer": inspect.cleandoc("""\
						
		Proin aliquam eleifend urna, ut rhoncus neque semper in. Integer a viverra tellus, quis tincidunt sem. 
		Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna.
		
	"""),
	"contacts": [
		{
			"name": "contact name",
			"role": "contact role",
			"affiliation": "contact affiliation",
			"email": "contact@example.org",
			"telephone": "contact telephone",
			"uri": "http://example.org/visualization_description/contacts/uri"
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
	"links": [
		{
			"uri": "http://example.org/visualization_description/links/uri",
			"description": "visualization link description"
		}
	],
	"relations": [
		{
			"name": "Related document name",
			"type": "isPartOf"  # Valid values: "isPartOf" "hasPart" "isVersionOf" "isFormatOf" "hasFormat" "references" "isReferencedBy" "isBasedOn" "isBasisFor" "requires" "isRequiredBy"
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
		"file_uri": "http://example.org/files/file.uri",  # Provide file name, path or URL
		"format": "file format",  # The file format, physical medium, or dimensions of the resource.
		"location": "file location",
		"note": "file note"
	}
]
additional = {
	"additional": "additional info"
}

response = nada.create_visualization_dataset(
	dataset_id=dataset_id,
	repository_id=repository_id,
	published=published,
	overwrite=overwrite,
	metadata_information=metadata_information,
	visualization_description=visualization_description,
	files=files,
	additional=additional
)

# upload temporary thumbnail
thumbnail_path = nada.text_to_thumbnail("Visualization\nDataset")
nada.upload_thumbnail(dataset_id, thumbnail_path)