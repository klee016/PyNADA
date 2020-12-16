from pynada import create_and_import
from pynada import utils

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

#################################d
# add_geospatial_dataset test
#################################
idno = "GEOSPATIAL_DATASET_SAMPLE_01"

repositoryid = "central"
published = 0
overwrite = "yes"
metadata_maintenance = {
	"update_frequency": "maintenance update_frequency",
	"note": "maintenance note",
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
	"prod_date": "2020-12-31",
	"version": "the current version of the dataset"
}
dataset_description = {
	"file_identifier": "GEOSPATIAL_DATASET_SAMPLE_01",
	"language": "language code",
	"charset_code": "character encoding used",
	"hierarchy_level": "geospatial dataset hierarchy_level",
	"date_stamp": "2009-11-17T10:00:00",
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
	"identification_info": {
		"title": "GEOSPATIAL DATASET SAMPLE 01 (full title)",
		"alternate_title": "GEOSPATIAL DATASET SAMPLE 01 (alternate_title)",
		"date": [
			{
				"date": "2020-12-31",
				"type": "type of event e.g. publication"
			}
		],
		"edition": "Edition e.g. first",
		"identifiers": [
			{
				"identifier": "geospatial data identifier"
			}
		],
		"presentation_form": "e.g. documentDigital",
		"abstract": "geospatial dataset abstract",
		"purpose": "geospatial dataset purpose",
		"credit": "geospatial dataset credit",
		"status": "status code e.g. historicalArchive",
		"point_of_contact": [
			{
				"person_name": "point_of_contact person_name",
				"role": "point_of_contact role",
				"organisation": "point_of_contact organisation",
				"position": "point_of_contact position",
				"instructions": "point_of_contact instruction",
				"phone": "point_of_contact phone",
				"fax": "point_of_contact fax",
				"email": "point_of_contact email",
				"website": "point_of_contact website",
				"address": "point_of_contact address",
				"city": "point_of_contact city",
				"administrative_area": "point_of_contact administrative_area",
				"postal_code": "point_of_contact postal_code",
				"country": "point_of_contact country"
			}
		],
		"resource_maintenance": {
			"maintenance_frequency": "maintenance frequency code e.g. weekly"
		},
		"graphic_overview": [
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
				"code_uri": "keyword code_list used"
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
		"language": "identification_info language",
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
					"south": -180,
					"west": -180,
					"north": -180,
					"east": -180
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
		"Scope": "data_quality_info scope",
		"lineage": "data_quality_info lineage statement"
	},
	"spatial_representation_info": {
		"topology_level": "geometryOnly",  # Topology Level Code: {geometryOnly, topology1D, planarGraph, fullPlanarGraph, surfaceGraph, fullSurfaceGraph, topology3D, fullTopology3D, abstract}
		"Geometric_object_code": "complex"  # Geometric Object Type Code codes ={complex, composite, curve, point, solid, surface}
	},
	"reference_system_info": {
		"code": "EPSG:5701",  # reference_system Identifier Code
		"code_space": "urn:ogc:def:crs"  # spatial reference system code_space
	}
}
additional = {
	"additional": "additional info"
}

response = create_and_import.add_geospatial_dataset(
	idno=idno,
	repositoryid=repositoryid,
	published=published,
	overwrite=overwrite,
	metadata_maintenance=metadata_maintenance,
	dataset_description=dataset_description,
	additional=additional
)

print(response)

utils.text_to_thumbnail("Geospatial\nDataset")
create_and_import.add_thumbnail(idno, "temp_thumbnail.jpg")