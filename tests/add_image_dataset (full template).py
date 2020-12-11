from pynada import create_and_import

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

#########################
# add_image_dataset test
#########################
idno = "IMAGE_DATASET_SAMPLE_01"

repositoryid = "central"
published = 0
overwrite = "yes"
metadata_information = {
	"title": "string",
	"idno": "string",
	"producers": [
		{
			"name": "string",
			"abbr": "string",
			"affiliation": "string",
			"role": "string"
		}
	],
	"production_date": "string",
	"version": "string"
}
image_description = {
	"iptc": {
		"mediafragment": {
			"uri": "http://example.com",
			"delimitertype": "spatial",
			"description": "string"
		},
		"photoVideoMetadataIPTC": {
			"aboutCvTerms": [
				{
					"cvId": "http://example.com",
					"cvTermName": "string",
					"cvTermId": "http://example.com",
					"cvTermRefinedAbout": "http://example.com"
				}
			],
			"additionalModelInfo": "string",
			"artworkOrObjects": [
				{
					"circaDateCreated": "string",
					"contentDescription": "string",
					"contributionDescription": "string",
					"copyrightNotice": "string",
					"creatorIdentifiers": [
						"string"
					],
					"creatorNames": [
						"string"
					],
					"currentCopyrightOwnerIdentifier": "http://example.com",
					"currentCopyrightOwnerName": "string",
					"currentLicensorIdentifier": "http://example.com",
					"currentLicensorName": "string",
					"dateCreated": "2020-12-06T18:29:44Z",
					"physicalDescription": "string",
					"source": "string",
					"sourceInventoryNr": "string",
					"sourceInventoryUrl": "http://example.com",
					"stylePeriod": [
						"string"
					],
					"title": "string"
				}
			],
			"captionWriter": "string",
			"cityName": "string",
			"copyrightNotice": "string",
			"copyrightOwners": [
				{
					"name": "string",
					"role": [
						"http://example.com"
					],
					"identifiers": [
						"http://example.com"
					]
				}
			],
			"countryCode": "string",
			"countryName": "string",
			"creatorContactInfo": {
				"country": "string",
				"emailwork": "string",
				"region": "string",
				"phonework": "string",
				"weburlwork": "string",
				"address": "string",
				"city": "string",
				"postalCode": "string"
			},
			"creatorNames": [
				"string"
			],
			"creditLine": "string",
			"dateCreated": "2020-12-06T18:29:44Z",
			"description": "string",
			"digitalImageGuid": "IMAGE_DATASET_SAMPLE_01",
			"digitalSourceType": "http://example.com",
			"embdEncRightsExpr": [
				{
					"encRightsExpr": "string",
					"rightsExprEncType": "string",
					"rightsExprLangId": "http://example.com"
				}
			],
			"eventName": "string",
			"genres": [
				{
					"cvId": "http://example.com",
					"cvTermName": "string",
					"cvTermId": "http://example.com",
					"cvTermRefinedAbout": "http://example.com"
				}
			],
			"headline": "IMAGE DATASET SAMPLE 01",
			"imageRating": 0,
			"imageSupplierImageId": "string",
			"instructions": "string",
			"intellectualGenre": "string",
			"jobid": "string",
			"jobtitle": "string",
			"keywords": [
				"string"
			],
			"linkedEncRightsExpr": [
				{
					"linkedRightsExpr": "http://example.com",
					"rightsExprEncType": "string",
					"rightsExprLangId": "http://example.com"
				}
			],
			"locationsShown": [
				{
					"city": "string",
					"countryCode": "string",
					"countryName": "string",
					"gpsAltitude": 0,
					"gpsLatitude": 0,
					"gpsLongitude": 0,
					"identifiers": [
						"http://example.com"
					],
					"name": "string",
					"provinceState": "string",
					"sublocation": "string",
					"worldRegion": "string"
				}
			],
			"maxAvailHeight": 0,
			"maxAvailWidth": 0,
			"minorModelAgeDisclosure": "http://example.com",
			"modelAges": [
				0
			],
			"modelReleaseDocuments": [
				"string"
			],
			"modelReleaseStatus": {
				"cvId": "http://example.com",
				"cvTermName": "string",
				"cvTermId": "http://example.com",
				"cvTermRefinedAbout": "http://example.com"
			},
			"organisationInImageCodes": [
				"string"
			],
			"organisationInImageNames": [
				"string"
			],
			"personInImageNames": [
				"string"
			],
			"personsShown": [
				{
					"name": "string",
					"description": "string",
					"identifiers": [
						"http://example.com"
					],
					"characteristics": [
						{
							"cvId": "http://example.com",
							"cvTermName": "string",
							"cvTermId": "http://example.com",
							"cvTermRefinedAbout": "http://example.com"
						}
					]
				}
			],
			"productsShown": [
				{
					"description": "string",
					"gtin": "string",
					"name": "string"
				}
			],
			"propertyReleaseDocuments": [
				"string"
			],
			"propertyReleaseStatus": {
				"cvId": "http://example.com",
				"cvTermName": "string",
				"cvTermId": "http://example.com",
				"cvTermRefinedAbout": "http://example.com"
			},
			"provinceStatePhoto": "string",
			"registryEntries": [
				{
					"role": "http://example.com",
					"assetIdentifier": "string",
					"registryIdentifier": "http://example.com"
				}
			],
			"sceneCodes": [
				"string"
			],
			"source": "string",
			"subjectCodes": [
				"string"
			],
			"sublocationName": "string",
			"supplier": [
				{
					"name": "string",
					"identifiers": [
						"http://example.com"
					]
				}
			],
			"title": "string",
			"usageTerms": "string",
			"webstatementRights": "http://example.com"
		}
	},
	"license": [
		{
			"name": "string",
			"uri": "string"
		}
	],
	"album": [
		{
			"name": "string",
			"description": "string",
			"owner": "string",
			"uri": "string"
		}
	],
	"tags": [
		{
			"tag": "string"
		}
	],
	"files": [
		{
			"file_uri": "string",
			"format": "string",
			"note": "string",
			"show": True
		}
	]
}


response = create_and_import.add_image_dataset(
	idno=idno,
	repositoryid=repositoryid,
	published=published,
	overwrite=overwrite,
	metadata_information=metadata_information,
	image_description=image_description
)

print(response)
