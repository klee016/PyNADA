import pynada as nada
import inspect

nada.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
nada.set_api_key(api_key)

#####################################
# create_geospatial_dataset template
#####################################

dataset_id = "GEOSPATIAL_DATASET_SAMPLE_01"
repository_id = "central"  # Collection ID that owns the dataset
published = 0  # Status of the dataset: 0=draft, 1=published
overwrite = "yes"  # Overwrite if already exists? Valid values: "yes""no"
metadata_maintenance = {
	"update_frequency": "maintenance update_frequency",  # Maintenance Frequency e.g., continual, daily, weekly, fortnightly, monthly, quarterly, biannually, annually, asNeeded, irregular, not-Planned, unknown
	"note": "maintenance note",  # Maintenance Note
	"contact": [
		{
			"person_name": "maintenance contact person_name",
			"role": "maintenance contact role",
			"organisation": "maintenance contact organisation",
			"position": "maintenance contact position",
			"instructions": "maintenance contact instruction",
			"phone": "maintenance contact phone",
			"fax": "maintenance contact fax",
			"email": "maintenance contact email",
			"website": "maintenance contact website",
			"address": "maintenance contact address",
			"city": "maintenance contact city",
			"administrative_area": "maintenance contact administrative_area",
			"postal_code": "maintenance contact postal_code",
			"country": "maintenance contact country"
		}
	],
	"prod_date": "2020-12-31",  # Document production date using format(YYYY-MM-DD)
	"version": "the current version of the dataset"  # Identify and describe the current version of the document
}
dataset_description = {
	"file_identifier": dataset_id,  # Must be same as dataset_id
	"language": "language code",  # Language code
	"charset_code": "UTF-8",  # character encoding used
	"hierarchy_level": "geospatial dataset hierarchy_level",  # Hierarchy level e.g. dataset, series
	"date_stamp": "2009-11-17T10:00:00",  # Date and time when the metadata record was created or updated. Requires an extended ISO 8601 formatted combined UTC date and time string (2009-11-17T10:00:00)
	"contact": [
		{
			"person_name": "contact person_name",
			"role": "contact role",
			"organisation": "contact organisation",
			"position": "contact position",
			"instructions": "contact instruction",
			"phone": "contact phone",
			"fax": "contact fax",
			"email": "contact email",
			"website": "contact website",
			"address": "contact address",
			"city": "contact city",
			"administrative_area": "contact administrative_area",
			"postal_code": "contact postal_code",
			"country": "contact country"
		}
	],
	"identification_info": {  # Resource Dataset or Dataset Series Identification
		"title": "[Template] Geospatial Dataset Sample 01",
		"alternate_title": "Geospatial Dataset Sample 01 (alternate_title)",
		"date": [
			{
				"date": "2020-12-31",
				"type": "type of event e.g. publication"
			}
		],
		"edition": "first",  # Edition e.g. first
		"identifiers": [
			{
				"identifier": "geospatial data identifier"
			}
		],
		"presentation_form": "e.g. documentDigital",  # documentDigital, documentHardcopy, imageDigital, image-Hardcopy, mapDigital, mapHardcopy, modelDigital, model-Hardcopy, profileDigital, profileHardcopy, tableDigital, tableHardcopy, videoDigital, videoHardcopy, audioDigital
		"abstract": inspect.cleandoc("""\
		
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
			Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. 
			Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, 
			non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, 
			sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. 
			
		"""),  # A free text summary of the content, significance, purpose, scope, etc. of the resource.
		"purpose": inspect.cleandoc("""\
		
			Pellentesque elementum massa mauris, ac tincidunt orci scelerisque nec. Sed mattis mauris sed dolor elementum, eget facilisis purus aliquet. Praesent eget iaculis augue, vel elementum purus. 
			Proin aliquam eleifend urna, ut rhoncus neque semper in. Integer a viverra tellus, quis tincidunt sem. Fusce nulla dui, commodo sit amet sem id, mattis eleifend lectus. Suspendisse eget tempus tortor. In quis cursus nulla.
			
		"""),  # Summary of the intentions for which the dataset was developed. Purpose includes objectives for creating the dataset and what the dataset is to support.
		"credit": inspect.cleandoc("""\
		
			In posuere tempus mi, in vehicula mi tristique nec. Phasellus neque ipsum, ultrices in interdum eget, vehicula id quam. Aliquam cursus euismod maximus.
						
		"""),
		"status": "completed",  # Status code - completed, historicalArchive, obsolete, onGoing, planned, required, underDevelopment
		"point_of_contact": [
			{
				"person_name": "point_of_contact person_name",
				"role": "point_of_contact role",
				"organisation": "point_of_contact organisation",
				"position": "point_of_contact position",
				"instructions": "point_of_contact instruction",
				"phone": "point_of_contact phone",
				"fax": "point_of_contact fax",
				"email": "point_of_contact@example.org",
				"website": "http://example.org/dataset_description/point_of_contact/website",
				"address": "point_of_contact address",
				"city": "point_of_contact city",
				"administrative_area": "point_of_contact administrative_area",
				"postal_code": "point_of_contact postal_code",
				"country": "point_of_contact country"
			}
		],
		"resource_maintenance": {
			"maintenance_frequency": "continual"  # Maintenance frequency code - continual, daily, weekly, fortnightly, monthly, quarterly, biannually, annually, asNeeded, irregular, not-Planned, unknown
		},
		"graphic_overview": [  # Graphic overview of resource
			{
				"name": "graphic_overview name",
				"type": "graphic_overview type",
				"description": "graphic_overview description"
			}
		],
		"keywords": [
			{
				"keyword": "keyword",
				"code": "discipline",  # allowed {discipline, place, stratum, temporal, theme}
				"code_uri": "http://example.org/dataset_description/keyword/lcode_uri"
			}
		],
		"resource_constraints": {
			"legal_constraints": [
				{
					"code_list_uri": "http://example.org/dataset_description/resource_constraints/legal_constraints/code_list_uri",
					"code": "legal_constraints code",
					"value": "legal_constraints value"
				}
			],
			"use_limitations": "use_limitations",
			"other_constraints": "other_constraints"
		},
		"spatial_representation_type": "vector",  # Spatial Representation type - vector, grid, textTable, tin, stereoModel, video
		"representative_fraction_denominator": "100000",  # Spatial Resolution Fraction
		"language": "identification_info language",  # Language code
		"charset_code": "identification_info charset_code",
		"topics": [
			{
				"topic": "geospatial dataset topic",  # Topic code e.g. farming, biota, boundaries, climatologyMeterologyAtmosphere, economy
				"vocab": "geospatial dataset topic vocab",
				"vocab_uri": "http://example.org/dataset_description/topics/vocab_uri"
			}
		],
		"extent": {
			"geographic_bounding_box": [
				{
					"south": 0,  # South (number) [ -180 .. 180 ]
					"west": 30,  # West (number) [ -180 .. 180 ]
					"north": 20,  # North (number) [ -180 .. 180 ]
					"east": 0  # East (number) [ -180 .. 180 ]
				}
			]
		},
		"supplemental_information": "supplemental_information"
	},
	"distribution_info": {
		"distributors": [
			{
				"person_name": "distributor person_name",
				"role": "distributor role",
				"organisation": "distributor organisation",
				"position": "distributor position",
				"instructions": "distributor instructions",
				"phone": "distributor phone",
				"fax": "distributor fax",
				"email": "distributor.email@example.org",
				"website": "distributor website",
				"address": "distributor address",
				"city": "distributor city",
				"administrative_area": "distributor administrative_area",
				"postal_code": "distributor postal_code",
				"country": "distributor country"
			}
		],
		"online_resource": [
			{
				"url": "http://example.org/dataset_description/distribution_info/online_resource",
				"name": "distribution_info online_resource name",
				"description": "distribution_info online_resource description",
				"format": "CSV"  # distribution_info online_resource file format e.g. CSV, ZIP
			}
		]
	},
	"data_quality_info": {
		"Scope": "dataset",  # Scope code - dataset, series, collectionSession, etc.
		"lineage": "data_quality_info lineage statement"  # Data quality lineage statement
	},
	"spatial_representation_info": {  # Resource spatial representation - Spatial representation information for the dataset (resource). Best practice is to include metadata for spatial representation if the described resource is a georeferenced dataset.
		"topology_level": "geometryOnly",  # Topology Level Code: {geometryOnly, topology1D, planarGraph, fullPlanarGraph, surfaceGraph, fullSurfaceGraph, topology3D, fullTopology3D, abstract}
		"Geometric_object_code": "complex"  # Geometric Object Type Code codes ={complex, composite, curve, point, solid, surface}
	},
	"reference_system_info": {  # Resource’s spatial reference system - Description of the spatial and/or temporal reference systems used in the dataset.
		"code": "EPSG:5701",  # reference_system Identifier Code
		"code_space": "urn:ogc:def:crs"  # spatial reference system code_space
	}
}
additional = {
	"additional": "additional info"
}

response = nada.create_geospatial_dataset(
	dataset_id=dataset_id,
	repository_id=repository_id,
	published=published,
	overwrite=overwrite,
	metadata_maintenance=metadata_maintenance,
	dataset_description=dataset_description,
	additional=additional
)


# upload temporary thumbnail
thumbnail_path = nada.text_to_thumbnail("Geospatial\nDataset")
nada.upload_thumbnail(dataset_id, thumbnail_path)