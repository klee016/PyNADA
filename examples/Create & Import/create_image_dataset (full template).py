import pynada as nada
import inspect

nada.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
nada.set_api_key(api_key)

################################
# create_image_dataset template
################################

dataset_id = "IMAGE-DATASET-SAMPLE-01"
repository_id = "central"  # Collection ID that owns the document
published = 0  # Status 0=draft, 1=published
overwrite = "yes"  # Overwrite document if already exists? Valid values: "yes" "no"
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
	"production_date": "2020-12-10",  # Document production date using format(YYYY-MM-DD)
	"version": "version"  # Identify and describe the current version of the document
}

image_description = {
	"iptc": {  # Overall structure of photo metadata of a single media asset - sets of metadata for the whole asset and parts of the asset -- the properties comply with the IPTC Photo Metadata Standard 2017.1(IPTC/MS/2017-07-06)
		"mediafragment": {  # Object defining this fragement of a media asset - if ommitted = the whole asset
			"uri": "http://example.org/iptc/mediafragment/url",
			"delimitertype": "spatial",  # Valid values: "spatial" "temporal"
			"description": "IPTC mediafragment description"
		},
		"photoVideoMetadataIPTC": {  # Container for IPTC photo/video metadata
			"aboutCvTerms": [  # One or more topics, themes or entities the content is about, each one expressed by a term from a Controlled Vocabulary.
				{
					"cvId": "http://example.org/iptc/photoVideoMetadataIPTC/aboutCvTerms/cvId",  # The globally unique identifier of the Controlled Vocabulary the term is from.
					"cvTermName": "IPTC Cv Term Name",  # The natural language name of the term from a Controlled Vocabulary.
					"cvTermId": "http://example.org/iptc/photoVideoMetadataIPTC/aboutCvTerms/cvTermId",  # The globally unique identifier of the term from a Controlled Vocabulary.
					"cvTermRefinedAbout": "http://example.org/iptc/photoVideoMetadataIPTC/aboutCvTerms/cvTermRefinedAbout"  # The refined 'about' relationship of the term with the content.
				}
			],
			"additionalModelInfo": "IPTC additional Module Info",  # Information about the ethnicity and other facets of the model(s) in a model-released image.
			"artworkOrObjects": [  # A set of metadata about artwork or an object in the image
				{
					"circaDateCreated": "IPTC artworkOrObjects circaDateCreated",  # Approximate date or range of dates associated with the creation and production of an artwork or object or its components.
					"contentDescription": "IPTC artworkOrObjects contentDescription",  # A textual description of the content depicted in the artwork or object.
					"contributionDescription": "IPTC artworkOrObjects contributionDescription",  # A textual description about a contribution made to an artwork or an object.
					"copyrightNotice": "IPTC artworkOrObjects copyrightNotice",  # Contains any necessary copyright notice for claiming the intellectual property for artwork or an object in the image and should identify the current owner of the copyright of this work with associated intellectual property rights.
					"creatorIdentifiers": [  # Globally unique identifier for the creator of artwork or object.
						"IPTC artworkOrObjects creatorIdentifier"
					],
					"creatorNames": [  # Contains the name of the artist who has created artwork or an object in the image. In cases where the artist could or should not be identified the name of a company or organisation may be appropriate
						"IPTC artworkOrObjects creatorName"
					],
					"currentCopyrightOwnerIdentifier": "http://example.org/iptc/photoVideoMetadataIPTC/artworkOrObjects/currentCopyrightOwnerIdentifier",  # Globally unique identifier for the current owner of the copyright of the artwork or object.
					"currentCopyrightOwnerName": "IPTC artworkOrObjects currentCopyrightOwnerName",  # Name of the current owner of the copyright of the artwork or object.
					"currentLicensorIdentifier": "http://example.org/iptc/photoVideoMetadataIPTC/artworkOrObjects/currentLicensorIdentifier",  # Globally unique identifier for the current licensor of the artwork or object.
					"currentLicensorName": "IPTC artworkOrObjects currentLicensorName",  # Name of the current licensor of the artwork or object.
					"dateCreated": "2020-12-06T18:29:44Z",  # Designates the date and optionally the time the artwork or object in the image was created. This relates to artwork or objects with associated intellectual property rights.
					"physicalDescription": "IPTC artworkOrObjects physicalDescription",  # A textual description of the physical characteristics of the artwork or object, without reference to the content depicted.
					"source": "IPTC artworkOrObjects source",  # The organisation or body holding and registering the artwork or object in the image for inventory purposes.
					"sourceInventoryNr": "IPTC artworkOrObjects sourceInventoryNr",  # The inventory number issued by the organisation or body holding and registering the artwork or object in the image.
					"sourceInventoryUrl": "http://example.org/iptc/photoVideoMetadataIPTC/artworkOrObjects/sourceInventoryUrl",  # URL reference to the metadata record of the inventory maintained by the Source.
					"stylePeriod": [  # The style, historical or artistic period, movement, group, or school whose characteristics are represented in the artwork or object.
						"IPTC  artworkOrObjects stylePeriod"
					],
					"title": "IPTC artworkOrObjects title"  # A reference for the artwork or object in the image.
				}
			],
			"captionWriter": "IPTC captionWriter",  # Identifier or the name of the person involved in writing, editing or correcting the description of the image.
			"cityName": "IPTC cityName",  # Name of the city of the location shown in the image. This element is at the third level of a top-down geographical hierarchy.
			"copyrightNotice": "IPTC copyrightNotice",  # Contains any necessary copyright notice for claiming the intellectual property for this photograph and should identify the current owner of the copyright for the photograph. Other entities like the creator of the photograph may be added in the corresponding field. Notes on usage rights should be provided in "Rights usage terms".
			"copyrightOwners": [  # Owner or owners of the copyright in the licensed image.
				{
					"name": "IPTC copyrightOwner name",  # Full name of the entity/concept
					"role": [  # Identifier of the role the entity has in the context of the metadata property
						"http://example.org/iptc/photoVideoMetadataIPTC/copyrightOwners/role"
					],
					"identifiers": [  # Globally unique identifier of the entity/concept
						"http://example.org/iptc/photoVideoMetadataIPTC/copyrightOwners/identifier"
					]
				}
			],
			"countryCode": "TMP",  # Code of the country of the location shown in the image. This element is at the top/first level of a top-down geographical hierarchy. The code should be taken from ISO 3166 two or three letter code. The full name of a country should go to the "Country" element.
			"countryName": "Templand",  # Full name of the country of the location shown in the image. This element is at the top/first level of a top-down geographical hierarchy. The full name should be expressed as a verbal name and not as a code, a code should go to the element "CountryCode"
			"creatorContactInfo": {  # The creator's contact information provides all necessary information to get in contact with the creator of this image and comprises a set of sub-properties for proper addressing.
				"country": "IPTC creatorContactInfo country",  # The contact information country part.
				"emailwork": "IPTC creatorContactInfo emailwork",  # The contact information email address part.
				"region": "IPTC creatorContactInfo region",  # The contact information part denoting regional information such as state or province.
				"phonework": "IPTC creatorContactInfo phonework",  # The contact information phone number part.
				"weburlwork": "IPTC creatorContactInfo weburlwork",  # The contact information web address part. Multiple addresses can be given. May have to be separated by a comma in the user interface.
				"address": "IPTC creatorContactInfo address",  # The contact information address part. Comprises an optional company name and all required information to locate the building or postbox to which mail should be sent. To that end, the address is a multiline field.
				"city": "IPTC creatorContactInfo city",  # The contact information city part.
				"postalCode": "IPTC creatorContactInfo postalCode"  # The contact information part denoting the local postal code.
			},
			"creatorNames": [  # Contains the name of the photographer, but in cases where the photographer should not be identified the name of a company or organisation may be appropriate.
				"IPTC creatorNames"
			],
			"creditLine": "IPTC creditLine",  # The credit to person(s) and/or organisation(s) required by the supplier of the image to be used when published. This is a free-text field.
			"dateCreated": "2020-12-06T18:29:44Z",  # Designates the date and optionally the time the content of the image was created rather than the date of the creation of the digital representation.
			"description": inspect.cleandoc("""\
			
				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
				Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. 
				Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, 
				non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, 
				sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. 
				
			"""),  # A textual description, including captions, of the image.
			"digitalImageGuid": dataset_id,  # Must be same as dataset_id. Globally unique identifier for this digital image. It is created and applied by the creator of the digital image at the time of its creation . This value shall not be changed after that time.
			"digitalSourceType": "http://example.org/iptc/photoVideoMetadataIPTC/digitalSourceType",  # The type of the source of this digital image
			"embdEncRightsExpr": [  # An embedded rights expression using any rights expression language
				{
					"encRightsExpr": "IPTC embdEncRightsExpr encRightsExpr",  # Embedded serialized rights expression using a rights expression language which is encoded as a string.
					"rightsExprEncType": "IPTC embdEncRightsExpr rightsExprEncType",  # Encoding type of the rights expression, identified by an IANA Media Type.
					"rightsExprLangId": "http://example.org/iptc/photoVideoMetadataIPTC/embdEncRightsExpr/rightsExprLangId"  # Identifier of the rights expression language used by the rights expression.
				}
			],
			"eventName": "IPTC eventName",  # Names or describes the specific event at which the photo was taken.
			"genres": [  # Artistic, style, journalistic, product or other genre(s) of the image (expressed by a term from any Controlled Vocabulary)
				{
					"cvId": "http://example.org/iptc/photoVideoMetadataIPTC/genres/cvId",  # The globally unique identifier of the Controlled Vocabulary the term is from.
					"cvTermName": "IPTC genres cvTermName",  # The natural language name of the term from a Controlled Vocabulary.
					"cvTermId": "http://example.org/iptc/photoVideoMetadataIPTC/genres/cvTermId",  # The globally unique identifier of the term from a Controlled Vocabulary.
					"cvTermRefinedAbout": "http://example.org/iptc/photoVideoMetadataIPTC/genres/cvTermRefinedAbout"  # The refined 'about' relationship of the term with the content.
				}
			],
			"headline": "[Template] Image Dataset Sample 01",
			"imageRating": 0,  # Rating of the image by its user or supplier
			"imageSupplierImageId": "IPTC imageSupplierImageId",  # Optional identifier assigned by the Image Supplier to the image.
			"instructions": inspect.cleandoc("""\
			
				Vestibulum interdum mi at turpis tristique viverra. Phasellus molestie ante id efficitur interdum. Vivamus metus dolor, volutpat non justo non, lobortis varius sem. Suspendisse scelerisque molestie urna, vel dapibus massa rutrum quis. 
				Nam porta posuere enim, ac interdum ex pellentesque ac. Praesent auctor neque vel neque tristique facilisis vel non purus. Mauris semper nibh eu erat elementum congue nec quis ligula. In in imperdiet lorem, et consectetur erat. 
				Nam elit odio, ultrices eu tempus at, fringilla at tortor. Integer id rutrum est, sed ornare metus. 
				Praesent sollicitudin vitae est vel tristique. Vestibulum nec magna vitae nunc feugiat pulvinar. 
				Etiam consectetur eget quam sed rhoncus. Phasellus eu lacus ac magna interdum consequat nec id ipsum.
				
			"""),  # Any of a number of instructions from the provider or creator to the receiver of the image which might include any of the following: embargoes (NewsMagazines OUT) and other restrictions not covered by the "Rights Usage Terms" field; information regarding the original means of capture (scanning notes, colourspace info) or other specific text information that the user may need for accurate reproduction; additional permissions required when publishing; credits for publishing if they exceed the IIM length of the credit field
			"intellectualGenre": "IPTC intellectualGenre",  # Describes the nature, intellectual, artistic or journalistic characteristic of an image.
			"jobid": "IPTC jobid",  # Number or identifier for the purpose of improved workflow handling. This is a user created identifier related to the job for which the image is supplied.
			"jobtitle": "IPTC jobtitle",  # Contains the job title of the photographer. As this is sort of a qualifier the Creator element has to be filled in as mandatory prerequisite for using Creator's Jobtitle.
			"keywords": [  # Keywords to express the subject of the image. Keywords may be free text and don't have to be taken from a controlled vocabulary. Codes from the controlled vocabulary IPTC Subject NewsCodes must go to the "Subject Code" field.
				"IPTC keyword"
			],
			"linkedEncRightsExpr": [  # A linked rights expression using any rights expression language.
				{
					"linkedRightsExpr": "http://example.org/iptc/photoVideoMetadataIPTC/linkedEncRightsExpr/linkedRightsExpr",  # Link to a rights expression using a rights expression language.
					"rightsExprEncType": "IPTC linkedEncRightsExpr rightsExprEncType",  # Encoding type of the rights expression, identified by an IANA Media Type.
					"rightsExprLangId": "http://example.org/iptc/photoVideoMetadataIPTC/linkedEncRightsExpr/rightsExprLangId"  # Identifier of the rights expression language used by the rights expression.
				}
			],
			"locationsShown": [  # The location the photo was taken.
				{
					"city": "IPTC locationsShown city", # Name of the city the Location is located in
					"countryCode": "ISO",  # ISO code of the country the Location is located in
					"countryName": "IPTC locationsShown countryName",  # Name of the country the Location is located in
					"gpsAltitude": 0,  # Altitude in meters of a WGS84 based position of this Location
					"gpsLatitude": 0,  # Lattitude of a WGS84 based position of this Location
					"gpsLongitude": 0,  # Longitude of a WGS84 based position of this Location
					"identifiers": [  # Globally unique identifier of the location
						"http://example.org/iptc/photoVideoMetadataIPTC/locationsShown/identifier"
					],
					"name": "IPTC locationsShown name",  # Full name of the location
					"provinceState": "IPTC locationsShown provinceState",  # Name of the state or province the Location is located in
					"sublocation": "IPTC locationsShown sublocation",  # Name of a sub location the Location is located in
					"worldRegion": "IPTC locationsShown worldRegion"  # Name of the world region the Location is located in
				}
			],
			"maxAvailHeight": 0,  # The maximum available height in pixels of the original photo from which this photo has been derived by downsizing.
			"maxAvailWidth": 0,  # The maximum available width in pixels of the original photo from which this photo has been derived by downsizing.
			"minorModelAgeDisclosure": "http://example.org/iptc/photoVideoMetadataIPTC/minorModelAgeDisclosure",  # Age of the youngest model pictured in the image, at the time that the image was made.
			"modelAges": [  # Age of the human model(s) at the time this image was taken in a model released image.
				0
			],
			"modelReleaseDocuments": [  # Optional identifier associated with each Model Release.
				"IPTC modelReleaseDocument"
			],
			"modelReleaseStatus": {  # Summarises the availability and scope of model releases authorising usage of the likenesses of persons appearing in the photograph.
				"cvId": "http://example.org/iptc/photoVideoMetadataIPTC/modelReleaseStatus/cvId",  # The globally unique identifier of the Controlled Vocabulary the term is from.
				"cvTermName": "IPTC modelReleaseStatus cvTermName",  # The natural language name of the term from a Controlled Vocabulary.
				"cvTermId": "http://example.org/iptc/photoVideoMetadataIPTC/modelReleaseStatus/cvTermId",  # The globally unique identifier of the term from a Controlled Vocabulary.
				"cvTermRefinedAbout": "http://example.org/iptc/photoVideoMetadataIPTC/modelReleaseStatus/cvTermRefinedAbout"  # The refined 'about' relationship of the term with the content.
			},
			"organisationInImageCodes": [  # Code from a controlled vocabulary for identifying the organisation or company which is featured in the image.
				"IPTC organisationInImageCode"
			],
			"organisationInImageNames": [  # Name of the organisation or company which is featured in the image.
				"IPTC organisationInImageName"
			],
			"personInImageNames": [  # Name of a person shown in the image.
				"IPTC personInImageNames"
			],
			"personsShown": [  # Details about a person the content is about.
				{
					"name": "IPTC personsShown name",  # Name of the person
					"description": "IPTC personsShown description",  # A textual description of the person
					"identifiers": [  # Globally unique identifier of the person
						"http://example.org/iptc/photoVideoMetadataIPTC/personsShown/identifier"
					],
					"characteristics": [  # A property or trait of the person
						{
							"cvId": "http://example.org/iptc/photoVideoMetadataIPTC/personsShown/characteristics/cvId",  # The globally unique identifier of the Controlled Vocabulary the term is from.
							"cvTermName": "IPTC personsShown cvTermName",  # The natural language name of the term from a Controlled Vocabulary.
							"cvTermId": "http://example.org/iptc/photoVideoMetadataIPTC/personsShown/characteristics/cvTermId",  # The globally unique identifier of the term from a Controlled Vocabulary.
							"cvTermRefinedAbout": "http://example.org/iptc/photoVideoMetadataIPTC/personsShown/characteristics/cvTermRefinedAbout"  # The refined 'about' relationship of the term with the content.
						}
					]
				}
			],
			"productsShown": [  # A product the content is about.
				{
					"description": "IPTC productsShown description",  # A textual description of the product.
					"gtin": "00000123456789",  # A 14 digit GTIN (Global Trade Item Number) of the product (GTIN-8 to GTIN-14 codes are used).
					"name": "IPTC productsShown name"  # Name of the product.
				}
			],
			"propertyReleaseDocuments": [  # Optional identifier associated with each Property Release.
				"IPTC propertyReleaseDocument"
			],
			"propertyReleaseStatus": {  # Summarises the availability and scope of property releases authorising usage of the properties appearing in the photograph.
				"cvId": "http://example.org/iptc/photoVideoMetadataIPTC/propertyReleaseStatus/cvId",  # The globally unique identifier of the Controlled Vocabulary the term is from.
				"cvTermName": "IPTC propertyReleaseStatus cvTermName",  # The natural language name of the term from a Controlled Vocabulary.
				"cvTermId": "http://example.org/iptc/photoVideoMetadataIPTC/propertyReleaseStatus/cvTermId",  # The globally unique identifier of the term from a Controlled Vocabulary.
				"cvTermRefinedAbout": "http://example.org/iptc/photoVideoMetadataIPTC/propertyReleaseStatus/cvTermRefinedAbout"  # The refined 'about' relationship of the term with the content.


			},
			"provinceStatePhoto": "IPTC provinceStatePhoto",  # Name of the subregion of a country of the location shown in the image. This element is at the second level of a top-down geographical hierarchy.
			"registryEntries": [  # Both a Registry Item Id and a Registry Organisation Id to record any registration of this digital image with a registry.
				{
					"role": "http://example.org/iptc/photoVideoMetadataIPTC/registryEntries/role",  # An identifier of the reason and/or purpose for this Registry Entry.
					"assetIdentifier": "IPTC registryEntries assetIdentifier",  # Unique identifier of the video as issued by a registry
					"registryIdentifier": "http://example.org/iptc/photoVideoMetadataIPTC/registryEntries/registryIdentifier"  # An identifier for the registry which issued the identifier of the video.
				}
			],
			"sceneCodes": [  # Describes the scene of a photo content. Specifies one ore more terms from the IPTC "Scene-NewsCodes". Each Scene is represented as a string of 6 digits in an unordered list.
				"IPTC sceneCode"
			],
			"source": "IPTC source",  # The name of a person or party who has a role in the content supply chain. This could be an agency, a member of an agency, an individual or a combination. Source could be different from Creator and from the entities in the Copyright Notice.
			"subjectCodes": [  # Specifies one or more Subjects from the IPTC Subject-NewsCodes taxonomy to categorise the image. Each Subject is represented as a string of 8 digits in an unordered list.
				"IPTC subjectCodes"
			],
			"sublocationName": "IPTC sublocationName",  # Exact name of the sublocation shown in the image. This sublocation name could either be the name of a sublocation to a city or the name of a well known location or (natural) monument outside a city. In the sense of a sublocation to a city this element is at the fourth level of a top-down geographical hierarchy.
			"supplier": [  # Identifies the most recent supplier of the image, who is not necessarily its owner or creator.
				{
					"name": "IPTC supplier name",
					"identifiers": [
						"http://example.org/iptc/photoVideoMetadataIPTC/supplier/identifiers"
					]
				}
			],
			"title": "IPTC title",  # A shorthand reference for the digital image. Title provides a short human readable name which can be a text and/or numeric reference. It is not the same as Headline.
			"usageTerms": "IPTC usageTerms",  # The licensing parameters of the image expressed in free-text.
			"webstatementRights": "http://example.org/iptc/photoVideoMetadataIPTC/webstatementRights"  # URL referencing a web resouce providing a statement of the copyright ownership and usage rights of the image.
		}
	},
	"license": [
		{
			"name": "license name",
			"uri": "license uri"
		}
	],
	"album": [
		{
			"name": "album name",
			"description": "album description",
			"owner": "album owner",
			"uri": "album uri"
		}
	],
	"tags": [
		{
			"tag": "tag"
		}
	],
	"files": [
		{
			"file_uri": "http://example.org/image_description/files/file.uri",  # File name or URL
			"format": "file format",  # The file format, physical medium, or dimensions of the resource.
			"note": "file note",
			"show": True  # Show the image file on the page
		}
	]
}

response = nada.create_image_dataset(
	dataset_id=dataset_id,
	repository_id=repository_id,
	published=published,
	overwrite=overwrite,
	metadata_information=metadata_information,
	image_description=image_description
)


# upload temporary thumbnail
thumbnail_path = nada.text_to_thumbnail("Image\nDataset")
nada.upload_thumbnail(dataset_id, thumbnail_path)