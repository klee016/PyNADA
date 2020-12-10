from pynada import create_and_import

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

#########################
# add_image_dataset test
#########################
idno = "IMAGE-DATASET-SAMPLE-01"

repositoryid = "central"
published = 0
overwrite = "yes"
metadata_information = {
	"title": "metadata title",
	"idno": "metadata idno",
	"producers": [
		{
			"name": "producer name",
			"abbr": "producer abbr",
			"affiliation": "producer affiliation",
			"role": "producer role"
		}
	],
	"production_date": "2020-12-10",
	"version": "version"
}

image_description = {
	"iptc": {
		"mediafragment": {
			"uri": "http://example.org/iptc/mediafragment/url",
			"delimitertype": "spatial",
			"description": "iptc mediafragment description"
		},
		"photoVideoMetadataIPTC": {
			"aboutCvTerms": [
				{
					"cvId": "http://example.org/iptc/photoVideoMetadataIPTC/aboutCvTerms/cvId",
					"cvTermName": "IPTC Cv Term Name",
					"cvTermId": "http://example.org/iptc/photoVideoMetadataIPTC/aboutCvTerms/cvTermId",
					"cvTermRefinedAbout": "http://example.org/iptc/photoVideoMetadataIPTC/aboutCvTerms/cvTermRefinedAbout"
				}
			],
			"additionalModelInfo": "IPTC additional Module Info",
			"artworkOrObjects": [
				{
					"circaDateCreated": "IPTC artworkOrObjects circaDateCreated",
					"contentDescription": "IPTC artworkOrObjects contentDescription",
					"contributionDescription": "IPTC artworkOrObjects contributionDescription",
					"copyrightNotice": "IPTC artworkOrObjects copyrightNotice",
					"creatorIdentifiers": [
						"IPTC artworkOrObjects creatorIdentifier"
					],
					"creatorNames": [
						"IPTC artworkOrObjects creatorName"
					],
					"currentCopyrightOwnerIdentifier": "http://example.org/iptc/photoVideoMetadataIPTC/artworkOrObjects/currentCopyrightOwnerIdentifier",
					"currentCopyrightOwnerName": "IPTC artworkOrObjects currentCopyrightOwnerName",
					"currentLicensorIdentifier": "http://example.org/iptc/photoVideoMetadataIPTC/artworkOrObjects/currentLicensorIdentifier",
					"currentLicensorName": "IPTC artworkOrObjects currentLicensorName",
					"dateCreated": "2020-12-06T18:29:44Z",
					"physicalDescription": "IPTC artworkOrObjects physicalDescription",
					"source": "IPTC artworkOrObjects source",
					"sourceInventoryNr": "IPTC artworkOrObjects sourceInventoryNr",
					"sourceInventoryUrl": "http://example.org/iptc/photoVideoMetadataIPTC/artworkOrObjects/sourceInventoryUrl",
					"stylePeriod": [
						"IPTC  artworkOrObjects stylePeriod"
					],
					"title": "IPTC artworkOrObjects title"
				}
			],
			"captionWriter": "IPTC captionWriter",
			"cityName": "IPTC cityName",
			"copyrightNotice": "IPTC copyrightNotice",
			"copyrightOwners": [
				{
					"name": "IPTC copyrightOwner name",
					"role": [
						"http://example.org/iptc/photoVideoMetadataIPTC/copyrightOwners/role"
					],
					"identifiers": [
						"http://example.org/iptc/photoVideoMetadataIPTC/copyrightOwners/identifier"
					]
				}
			],
			"countryCode": "IPTC countryCode",
			"countryName": "IPTC countryName",
			"creatorContactInfo": {
				"country": "IPTC creatorContactInfo country",
				"emailwork": "IPTC creatorContactInfo emailwork",
				"region": "IPTC creatorContactInfo region",
				"phonework": "IPTC creatorContactInfo phonework",
				"weburlwork": "IPTC creatorContactInfo weburlwork",
				"address": "IPTC creatorContactInfo address",
				"city": "IPTC creatorContactInfo city",
				"postalCode": "IPTC creatorContactInfo postalCode"
			},
			"creatorNames": [
				"IPTC creatorNames"
			],
			"creditLine": "IPTC creditLine",
			"dateCreated": "2020-12-06T18:29:44Z",
			"description": "IPTC description",
			"digitalImageGuid": "IMAGE-DATASET-SAMPLE-01",
			"digitalSourceType": "http://example.org/iptc/photoVideoMetadataIPTC/digitalSourceType",
			"embdEncRightsExpr": [
				{
					"encRightsExpr": "IPTC embdEncRightsExpr encRightsExpr",
					"rightsExprEncType": "IPTC embdEncRightsExpr rightsExprEncType",
					"rightsExprLangId": "http://example.org/iptc/photoVideoMetadataIPTC/embdEncRightsExpr/rightsExprLangId"
				}
			],
			"eventName": "IPTC eventName",
			"genres": [
				{
					"cvId": "http://example.org/iptc/photoVideoMetadataIPTC/genres/cvId",
					"cvTermName": "IPTC genres cvTermName",
					"cvTermId": "http://example.org/iptc/photoVideoMetadataIPTC/genres/cvTermId",
					"cvTermRefinedAbout": "http://example.org/iptc/photoVideoMetadataIPTC/genres/cvTermRefinedAbout"
				}
			],
			"headline": "IMAGE DATASET SAMPLE 01",
			"imageRating": 0,
			"imageSupplierImageId": "IPTC imageSupplierImageId",
			"instructions": "IPTC instructions",
			"intellectualGenre": "IPTC intellectualGenre",
			"jobid": "IPTC jobid",
			"jobtitle": "IPTC jobtitle",
			"keywords": [
				"IPTC keyword"
			],
			"linkedEncRightsExpr": [
				{
					"linkedRightsExpr": "http://example.org/iptc/photoVideoMetadataIPTC/linkedEncRightsExpr/linkedRightsExpr",
					"rightsExprEncType": "IPTC linkedEncRightsExpr rightsExprEncType",
					"rightsExprLangId": "http://example.org/iptc/photoVideoMetadataIPTC/linkedEncRightsExpr/rightsExprLangId"
				}
			],
			"locationsShown": [
				{
					"city": "IPTC locationsShown city",
					"countryCode": "IPTC locationsShown countryCode",
					"countryName": "IPTC locationsShown countryName",
					"gpsAltitude": 0,
					"gpsLatitude": 0,
					"gpsLongitude": 0,
					"identifiers": [
						"http://example.org/iptc/photoVideoMetadataIPTC/locationsShown/identifier"
					],
					"name": "IPTC locationsShown name",
					"provinceState": "IPTC locationsShown provinceState",
					"sublocation": "IPTC locationsShown sublocation",
					"worldRegion": "IPTC locationsShown worldRegion"
				}
			],
			"maxAvailHeight": 0,
			"maxAvailWidth": 0,
			"minorModelAgeDisclosure": "http://example.org/iptc/photoVideoMetadataIPTC/minorModelAgeDisclosure",
			"modelAges": [
				0
			],
			"modelReleaseDocuments": [
				"IPTC modelReleaseDocument"
			],
			"modelReleaseStatus": {
				"cvId": "http://example.org/iptc/photoVideoMetadataIPTC/modelReleaseStatus/cvId",
				"cvTermName": "IPTC modelReleaseStatus cvTermName",
				"cvTermId": "http://example.org/iptc/photoVideoMetadataIPTC/modelReleaseStatus/cvTermId",
				"cvTermRefinedAbout": "http://example.org/iptc/photoVideoMetadataIPTC/modelReleaseStatus/cvTermRefinedAbout"
			},
			"organisationInImageCodes": [
				"IPTC organisationInImageCode"
			],
			"organisationInImageNames": [
				"IPTC organisationInImageName"
			],
			"personInImageNames": [
				"IPTC personInImageNames"
			],
			"personsShown": [
				{
					"name": "IPTC personsShown name",
					"description": "IPTC personsShown description",
					"identifiers": [
						"http://example.org/iptc/photoVideoMetadataIPTC/personsShown/identifier"
					],
					"characteristics": [
						{
							"cvId": "http://example.org/iptc/photoVideoMetadataIPTC/personsShown/characteristics/cvId",
							"cvTermName": "IPTC personsShown cvTermName",
							"cvTermId": "http://example.org/iptc/photoVideoMetadataIPTC/personsShown/characteristics/cvTermId",
							"cvTermRefinedAbout": "http://example.org/iptc/photoVideoMetadataIPTC/personsShown/characteristics/cvTermRefinedAbout"
						}
					]
				}
			],
			"productsShown": [
				{
					"description": "IPTC productsShown description",
					"gtin": "IPTC productsShown gtin",
					"name": "IPTC productsShown name"
				}
			],
			"propertyReleaseDocuments": [
				"IPTC propertyReleaseDocument"
			],
			"propertyReleaseStatus": {
				"cvId": "http://example.org/iptc/photoVideoMetadataIPTC/propertyReleaseStatus/cvId",
				"cvTermName": "IPTC propertyReleaseStatus cvTermName",
				"cvTermId": "http://example.org/iptc/photoVideoMetadataIPTC/propertyReleaseStatus/cvTermId",
				"cvTermRefinedAbout": "http://example.org/iptc/photoVideoMetadataIPTC/propertyReleaseStatus/cvTermRefinedAbout"
			},
			"provinceStatePhoto": "IPTC provinceStatePhoto",
			"registryEntries": [
				{
					"role": "http://example.org/iptc/photoVideoMetadataIPTC/registryEntries/role",
					"assetIdentifier": "IPTC registryEntries assetIdentifier",
					"registryIdentifier": "http://example.org/iptc/photoVideoMetadataIPTC/registryEntries/registryIdentifier"
				}
			],
			"sceneCodes": [
				"IPTC sceneCode"
			],
			"source": "IPTC source",
			"subjectCodes": [
				"IPTC subjectCodes"
			],
			"sublocationName": "IPTC sublocationName",
			"supplier": [
				{
					"name": "IPTC supplier name",
					"identifiers": [
						"http://example.org/iptc/photoVideoMetadataIPTC/supplier/identifiers"
					]
				}
			],
			"title": "IPTC title",
			"usageTerms": "IPTC usageTerms",
			"webstatementRights": "http://example.org/iptc/photoVideoMetadataIPTC/webstatementRights"
		}
	},
	"license": [
		{
			"name": "image license name",
			"uri": "image license uri"
		}
	],
	"album": [
		{
			"name": "image album name",
			"description": "image album description",
			"owner": "image album owner",
			"uri": "image album uri"
		}
	],
	"tags": [
		{
			"tag": "image tag"
		}
	],
	"files": [
		{
			"file_uri": "image file uri",
			"format": "image file format",
			"note": "image file note",
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
