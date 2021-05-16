import pynada as nada
import inspect

nada.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = open("API Key.txt", "r").read()
nada.set_api_key(api_key)

#####################################
# create_geospatial_dataset template
#####################################

dataset_id = "GEOSPATIAL_DATASET_SAMPLE_02"
repository_id = "central"  # Collection ID that owns the dataset
published = 1  # Status of the dataset: 0=draft, 1=published
overwrite = "yes"  # Overwrite if already exists? Valid values: "yes""no"
type = "dataset"  # Geospatial metadata type - dataset, service
dataset_metadata = {
    "fileIdentifier": dataset_id,
    "language": [
        {
            "codeListValue": "language codeListValue",
            "codeList": "language codeList",
            "codeSpace": "language codeSpace"
        }
    ],
    "characterSet": {
        "codeListValue": "characterSet codeListValue",
        "codeList": "characterSet codeList"
    },
    "parentIdentifier": "parentIdentifier",
    "hierarchyLevel": [
        {
            "hierarchyLevel": "hierarchyLevel"
        }
    ],
    "hierarchyLevelName": [
        {
            "hierarchyLevelName": "hierarchyLevelName"
        }
    ],
    "contact": [
        {
            "individualName": "individualName",
            "organisationName": "organisationName",
            "positionName": "positionName",
            "contactInfo": {
                "phone": {
                    "voice": "voice",
                    "facsimile": "facsimile"
                },
                "address": {
                    "deliveryPoint": "deliveryPoint",
                    "city": "city",
                    "postalCode": "postalCode",
                    "country": "country",
                    "elctronicMailAddress": "elctronicMailAddress"
                },
                "onlineResource": {
                    "linkage": "linkage",
                    "name": "name",
                    "description": "description",
                    "protocol": "protocol",
                    "function": "function"
                }
            },
            "role": "role"
        }
    ],
    "dateStamp": "dateStamp",
    "metadataStandardName": "metadataStandardName",
    "metadataStandardVersion": "metadataStandardVersion",
    "dataSetURI": "dataSetURI",
    "locale": [
        {
            "id": "id",
            "languageCode": {
                "codeListValue": "codeListValue",
                "codeList": "codeList",
                "codeSpace": "codeSpace"
            },
            "characterEncoding": {
                "characterSet": {
                    "codeListValue": "codeListValue",
                    "codeList": "codeList"
                }
            }
        }
    ],
    "spatialRepresentationInfo": [
        {
            "vectorSpatialRepresentation": {
                "topologyLevel": "topologyLevel",
                "geometricObjects": [
                    {
                        "geometricObjectType": "geometricObjectType",
                        "geometricObjectCount": 0
                    }
                ]
            },
            "gridSpatialRepresentation": {
                "numberOfDimensions": 0,
                "axisDimensionProperties": [
                    {
                        "dimension": {
                            "dimensionName": "dimensionName",
                            "dimensionSize": 0,
                            "resolution": 0
                        }
                    }
                ],
                "cellGeometry": "cellGeometry",
                "transformationParameterAvailability": True
            }
        }
    ],
    "referenceSystemInfo": [
        {
            "code": "code",
            "codeSpace": "codeSpace"
        }
    ],
    "identificationInfo": [
        {
            "citation": {
                "title": "[Template] Geospatial Dataset Sample 02",
                "alternateTitle": "alternateTitle",
                "date": [
                    {
                        "date": "date",
                        "type": "type"
                    }
                ],
                "edition": "edition",
                "editionDate": "editionDate",
                "identifier": {
                    "authority": "authority",
                    "code": None
                },
                "citedResponsibleParty": [
                    {
                        "individualName": "individualName",
                        "organisationName": "organisationName",
                        "positionName": "positionName",
                        "contactInfo": {
                            "phone": {
                                "voice": "voice",
                                "facsimile": "facsimile"
                            },
                            "address": {
                                "deliveryPoint": "deliveryPoint",
                                "city": "city",
                                "postalCode": "postalCode",
                                "country": "country",
                                "elctronicMailAddress": "elctronicMailAddress"
                            },
                            "onlineResource": {
                                "linkage": "linkage",
                                "name": "name",
                                "description": "description",
                                "protocol": "protocol",
                                "function": "function"
                            }
                        },
                        "role": "role"
                    }
                ],
                "presentationForm": [
                    None
                ],
                "series": {
                    "name": "name",
                    "issueIdentification": "issueIdentification",
                    "page": "page"
                },
                "otherCitationDetails": "otherCitationDetails",
                "collectiveTitle": "collectiveTitle",
                "ISBN": "ISBN",
                "ISSN": "ISSN"
            },
            "abstract": "abstract",
            "purpose": "purpose",
            "credit": "credit",
            "status": "status",
            "pointOfContact": [
                {
                    "individualName": "individualName",
                    "organisationName": "organisationName",
                    "positionName": "positionName",
                    "contactInfo": {
                        "phone": {
                            "voice": "voice",
                            "facsimile": "facsimile"
                        },
                        "address": {
                            "deliveryPoint": "deliveryPoint",
                            "city": "city",
                            "postalCode": "postalCode",
                            "country": "country",
                            "elctronicMailAddress": "elctronicMailAddress"
                        },
                        "onlineResource": {
                            "linkage": "linkage",
                            "name": "name",
                            "description": "description",
                            "protocol": "protocol",
                            "function": "function"
                        }
                    },
                    "role": "role"
                }
            ],
            "resourceMaintenance": [
                {
                    "maintenanceAndUpdateFrequency": "maintenanceAndUpdateFrequency"
                }
            ],
            "graphicOverview": [
                {
                    "fileName": "fileName",
                    "fileDescription": "fileDescription",
                    "fileType": "fileType"
                }
            ],
            "resourceFormat": [
                {
                    "name": "name",
                    "version": "version",
                    "amendmentNumber": "amendmentNumber",
                    "specification": "specification",
                    "fileDecompressionTechnique": "fileDecompressionTechnique",
                    "FormatDistributor": {
                        "individualName": "individualName",
                        "organisationName": "organisationName",
                        "positionName": "positionName",
                        "contactInfo": {
                            "phone": {
                                "voice": "voice",
                                "facsimile": "facsimile"
                            },
                            "address": {
                                "deliveryPoint": "deliveryPoint",
                                "city": "city",
                                "postalCode": "postalCode",
                                "country": "country",
                                "elctronicMailAddress": "elctronicMailAddress"
                            },
                            "onlineResource": {
                                "linkage": "linkage",
                                "name": "name",
                                "description": "description",
                                "protocol": "protocol",
                                "function": "function"
                            }
                        },
                        "role": "role"
                    }
                }
            ],
            "descriptiveKeywords": [
                {
                    "type": [
                        {
                            "code": "code",
                            "code_uri": "code_uri"
                        }
                    ],
                    "keyword": [
                        "keyword"
                    ],
                    "thesaurusName": {
                        "title": "title",
                        "alternateTitle": "alternateTitle",
                        "date": [
                            {
                                "date": "date",
                                "type": "type"
                            }
                        ],
                        "edition": "edition",
                        "editionDate": "editionDate",
                        "identifier": {
                            "authority": "authority",
                            "code": None
                        },
                        "citedResponsibleParty": [
                            {
                                "individualName": "individualName",
                                "organisationName": "organisationName",
                                "positionName": "positionName",
                                "contactInfo": {
                                    "phone": {
                                        "voice": "voice",
                                        "facsimile": "facsimile"
                                    },
                                    "address": {
                                        "deliveryPoint": "deliveryPoint",
                                        "city": "city",
                                        "postalCode": "postalCode",
                                        "country": "country",
                                        "elctronicMailAddress": "elctronicMailAddress"
                                    },
                                    "onlineResource": {
                                        "linkage": "linkage",
                                        "name": "name",
                                        "description": "description",
                                        "protocol": "protocol",
                                        "function": "function"
                                    }
                                },
                                "role": "role"
                            }
                        ],
                        "presentationForm": [
                            None
                        ],
                        "series": {
                            "name": "name",
                            "issueIdentification": "issueIdentification",
                            "page": "page"
                        },
                        "otherCitationDetails": "otherCitationDetails",
                        "collectiveTitle": "collectiveTitle",
                        "ISBN": "ISBN",
                        "ISSN": "ISSN"
                    }
                }
            ],
            "resourceConstraints": [
                {
                    "legalConstraints": {
                        "useLimitation": [
                            "useLimitation"
                        ],
                        "accessConstraints": [
                            "accessConstraints"
                        ],
                        "useConstraints": [
                            "useConstraints"
                        ],
                        "otherConstraints": [
                            "otherConstraints"
                        ]
                    },
                    "securityConstraints": {
                        "useLimitation": [
                            "useLimitation"
                        ],
                        "classification": "classification",
                        "userNote": "userNote",
                        "classificationSystem": "classificationSystem",
                        "handlingDescription": "handlingDescription"
                    }
                }
            ],
            "resourceSpecificUsage": [
                {
                    "specificUsage": "specificUsage",
                    "usageDateTime": "usageDateTime",
                    "userDeterminedLimitations": "userDeterminedLimitations",
                    "userContactInfo": [
                        {
                            "individualName": "individualName",
                            "organisationName": "organisationName",
                            "positionName": "positionName",
                            "contactInfo": {
                                "phone": {
                                    "voice": "voice",
                                    "facsimile": "facsimile"
                                },
                                "address": {
                                    "deliveryPoint": "deliveryPoint",
                                    "city": "city",
                                    "postalCode": "postalCode",
                                    "country": "country",
                                    "elctronicMailAddress": "elctronicMailAddress"
                                },
                                "onlineResource": {
                                    "linkage": "linkage",
                                    "name": "name",
                                    "description": "description",
                                    "protocol": "protocol",
                                    "function": "function"
                                }
                            },
                            "role": "role"
                        }
                    ]
                }
            ],
            "aggregationInfo": {
                "aggregateDataSetName": "aggregateDataSetName",
                "aggregateDataSetIdentifier": "aggregateDataSetIdentifier",
                "associationType": "associationType",
                "initiativeType": "initiativeType"
            },
            "spatialRepresentationType": "spatialRepresentationType",
            "spatialResolution": 0,
            "language": [
                {
                    "codeListValue": "codeListValue",
                    "codeList": "codeList",
                    "codeSpace": "codeSpace"
                }
            ],
            "characterSet": [
                {
                    "codeListValue": "codeListValue",
                    "codeList": "codeList"
                }
            ],
            "topicCategory": [
                "topicCategory"
            ],
            "extent": {
                "geographicElement": [
                    {
                        "geographicBoundingBox": {
                            "southBoundLongitude": -180,
                            "westBoundLongitude": -180,
                            "northBoundLongitude": -180,
                            "eastBoundLongitude": -180
                        },
                        "geographicDescription": "geographicDescription"
                    }
                ],
                "temporalElement": [
                    {
                        "extent": None
                    }
                ],
                "verticalElement": [
                    {
                        "minimumValue": 0,
                        "maximumValue": 0,
                        "verticalCRS": None
                    }
                ]
            },
            "supplementalInformation": "supplementalInformation"
        }
    ],
    "contentInfo": [
        {
            "featureCatalogueDescription": {
                "complianceCode": True,
                "language": "language",
                "includedWithDataset": True,
                "featureCatalogueCitation": {
                    "title": "title",
                    "alternateTitle": "alternateTitle",
                    "date": [
                        {
                            "date": "date",
                            "type": "type"
                        }
                    ],
                    "edition": "edition",
                    "editionDate": "editionDate",
                    "identifier": {
                        "authority": "authority",
                        "code": None
                    },
                    "citedResponsibleParty": [
                        {
                            "individualName": "individualName",
                            "organisationName": "organisationName",
                            "positionName": "positionName",
                            "contactInfo": {
                                "phone": {
                                    "voice": "voice",
                                    "facsimile": "facsimile"
                                },
                                "address": {
                                    "deliveryPoint": "deliveryPoint",
                                    "city": "city",
                                    "postalCode": "postalCode",
                                    "country": "country",
                                    "elctronicMailAddress": "elctronicMailAddress"
                                },
                                "onlineResource": {
                                    "linkage": "linkage",
                                    "name": "name",
                                    "description": "description",
                                    "protocol": "protocol",
                                    "function": "function"
                                }
                            },
                            "role": "role"
                        }
                    ],
                    "presentationForm": [
                        None
                    ],
                    "series": {
                        "name": "name",
                        "issueIdentification": "issueIdentification",
                        "page": "page"
                    },
                    "otherCitationDetails": "otherCitationDetails",
                    "collectiveTitle": "collectiveTitle",
                    "ISBN": "ISBN",
                    "ISSN": "ISSN"
                }
            },
            "coverageDescription": {
                "contentType": "contentType",
                "dimension": [
                    {
                        "name": "name",
                        "type": "type"
                    }
                ]
            }
        }
    ],
    "distributionInfo": {
        "distributionFormat": [
            {
                "name": "name",
                "version": "version",
                "amendmentNumber": "amendmentNumber",
                "specification": "specification",
                "fileDecompressionTechnique": "fileDecompressionTechnique",
                "FormatDistributor": {
                    "individualName": "individualName",
                    "organisationName": "organisationName",
                    "positionName": "positionName",
                    "contactInfo": {
                        "phone": {
                            "voice": "voice",
                            "facsimile": "facsimile"
                        },
                        "address": {
                            "deliveryPoint": "deliveryPoint",
                            "city": "city",
                            "postalCode": "postalCode",
                            "country": "country",
                            "elctronicMailAddress": "elctronicMailAddress"
                        },
                        "onlineResource": {
                            "linkage": "linkage",
                            "name": "name",
                            "description": "description",
                            "protocol": "protocol",
                            "function": "function"
                        }
                    },
                    "role": "role"
                }
            }
        ],
        "distributor": [
            {
                "individualName": "individualName",
                "organisationName": "organisationName",
                "positionName": "positionName",
                "contactInfo": {
                    "phone": {
                        "voice": "voice",
                        "facsimile": "facsimile"
                    },
                    "address": {
                        "deliveryPoint": "deliveryPoint",
                        "city": "city",
                        "postalCode": "postalCode",
                        "country": "country",
                        "elctronicMailAddress": "elctronicMailAddress"
                    },
                    "onlineResource": {
                        "linkage": "linkage",
                        "name": "name",
                        "description": "description",
                        "protocol": "protocol",
                        "function": "function"
                    }
                },
                "role": "role"
            }
        ],
        "transferOptions": [
            {
                "onLine": [
                    {
                        "linkage": "linkage",
                        "name": "name",
                        "description": "description",
                        "protocol": "protocol",
                        "function": "function"
                    }
                ]
            }
        ]
    },
    "dataQualityInfo": [
        {
            "scope": "scope",
            "report": [
                {
                    "DQ_DomainConsistency": {
                        "result": {
                            "nameOfMeasure": [
                                "nameOfMeasure"
                            ],
                            "measureIdentification": "measureIdentification",
                            "measureDescription": "measureDescription",
                            "evaluationMethodType": "evaluationMethodType",
                            "evaluationMethodDescription": "evaluationMethodDescription",
                            "evaluationProcedure": {
                                "title": "title",
                                "alternateTitle": "alternateTitle",
                                "date": [
                                    {
                                        "date": "date",
                                        "type": "type"
                                    }
                                ],
                                "edition": "edition",
                                "editionDate": "editionDate",
                                "identifier": {
                                    "authority": "authority",
                                    "code": None
                                },
                                "citedResponsibleParty": [
                                    {
                                        "individualName": "individualName",
                                        "organisationName": "organisationName",
                                        "positionName": "positionName",
                                        "contactInfo": {
                                            "phone": {
                                                "voice": "voice",
                                                "facsimile": "facsimile"
                                            },
                                            "address": {
                                                "deliveryPoint": "deliveryPoint",
                                                "city": "city",
                                                "postalCode": "postalCode",
                                                "country": "country",
                                                "elctronicMailAddress": "elctronicMailAddress"
                                            },
                                            "onlineResource": {
                                                "linkage": "linkage",
                                                "name": "name",
                                                "description": "description",
                                                "protocol": "protocol",
                                                "function": "function"
                                            }
                                        },
                                        "role": "role"
                                    }
                                ],
                                "presentationForm": [
                                    None
                                ],
                                "series": {
                                    "name": "name",
                                    "issueIdentification": "issueIdentification",
                                    "page": "page"
                                },
                                "otherCitationDetails": "otherCitationDetails",
                                "collectiveTitle": "collectiveTitle",
                                "ISBN": "ISBN",
                                "ISSN": "ISSN"
                            },
                            "dateTime": "dateTime",
                            "result": [
                                {
                                    "specification": {
                                        "title": "title",
                                        "alternateTitle": "alternateTitle",
                                        "date": [
                                            {
                                                "date": "date",
                                                "type": "type"
                                            }
                                        ],
                                        "edition": "edition",
                                        "editionDate": "editionDate",
                                        "identifier": {
                                            "authority": "authority",
                                            "code": None
                                        },
                                        "citedResponsibleParty": [
                                            {
                                                "individualName": "individualName",
                                                "organisationName": "organisationName",
                                                "positionName": "positionName",
                                                "contactInfo": {
                                                    "phone": {
                                                        "voice": "voice",
                                                        "facsimile": "facsimile"
                                                    },
                                                    "address": {
                                                        "deliveryPoint": "deliveryPoint",
                                                        "city": "city",
                                                        "postalCode": "postalCode",
                                                        "country": "country",
                                                        "elctronicMailAddress": "elctronicMailAddress"
                                                    },
                                                    "onlineResource": {
                                                        "linkage": "linkage",
                                                        "name": "name",
                                                        "description": "description",
                                                        "protocol": "protocol",
                                                        "function": "function"
                                                    }
                                                },
                                                "role": "role"
                                            }
                                        ],
                                        "presentationForm": [
                                            None
                                        ],
                                        "series": {
                                            "name": "name",
                                            "issueIdentification": "issueIdentification",
                                            "page": "page"
                                        },
                                        "otherCitationDetails": "otherCitationDetails",
                                        "collectiveTitle": "collectiveTitle",
                                        "ISBN": "ISBN",
                                        "ISSN": "ISSN"
                                    },
                                    "explanation": "explanation",
                                    "pass": True
                                }
                            ]
                        }
                    }
                }
            ],
            "lineage": {
                "statement": "statement",
                "processStep": [
                    {
                        "description": "description",
                        "rationale": "rationale",
                        "dateTime": "dateTime",
                        "processor": [
                            {
                                "individualName": "individualName",
                                "organisationName": "organisationName",
                                "positionName": "positionName",
                                "contactInfo": {
                                    "phone": {
                                        "voice": "voice",
                                        "facsimile": "facsimile"
                                    },
                                    "address": {
                                        "deliveryPoint": "deliveryPoint",
                                        "city": "city",
                                        "postalCode": "postalCode",
                                        "country": "country",
                                        "elctronicMailAddress": "elctronicMailAddress"
                                    },
                                    "onlineResource": {
                                        "linkage": "linkage",
                                        "name": "name",
                                        "description": "description",
                                        "protocol": "protocol",
                                        "function": "function"
                                    }
                                },
                                "role": "role"
                            }
                        ],
                        "source": [
                            {
                                "description": "description",
                                "sourceCitation": {
                                    "title": "title",
                                    "alternateTitle": "alternateTitle",
                                    "date": [
                                        {
                                            "date": "date",
                                            "type": "type"
                                        }
                                    ],
                                    "edition": "edition",
                                    "editionDate": "editionDate",
                                    "identifier": {
                                        "authority": "authority",
                                        "code": None
                                    },
                                    "citedResponsibleParty": [
                                        {
                                            "individualName": "individualName",
                                            "organisationName": "organisationName",
                                            "positionName": "positionName",
                                            "contactInfo": {
                                                "phone": {
                                                    "voice": "voice",
                                                    "facsimile": "facsimile"
                                                },
                                                "address": {
                                                    "deliveryPoint": "deliveryPoint",
                                                    "city": "city",
                                                    "postalCode": "postalCode",
                                                    "country": "country",
                                                    "elctronicMailAddress": "elctronicMailAddress"
                                                },
                                                "onlineResource": {
                                                    "linkage": "linkage",
                                                    "name": "name",
                                                    "description": "description",
                                                    "protocol": "protocol",
                                                    "function": "function"
                                                }
                                            },
                                            "role": "role"
                                        }
                                    ],
                                    "presentationForm": [
                                        None
                                    ],
                                    "series": {
                                        "name": "name",
                                        "issueIdentification": "issueIdentification",
                                        "page": "page"
                                    },
                                    "otherCitationDetails": "otherCitationDetails",
                                    "collectiveTitle": "collectiveTitle",
                                    "ISBN": "ISBN",
                                    "ISSN": "ISSN"
                                }
                            }
                        ]
                    }
                ]
            }
        }
    ],
    "metadataMaintenance": {
        "maintenanceAndUpdateFrequency": "maintenanceAndUpdateFrequency"
    },
    "portrayalCatalogueInfo": {
        "portrayalCatalogueCitation": [
            {
                "title": "title",
                "alternateTitle": "alternateTitle",
                "date": [
                    {
                        "date": "date",
                        "type": "type"
                    }
                ],
                "edition": "edition",
                "editionDate": "editionDate",
                "identifier": {
                    "authority": "authority",
                    "code": None
                },
                "citedResponsibleParty": [
                    {
                        "individualName": "individualName",
                        "organisationName": "organisationName",
                        "positionName": "positionName",
                        "contactInfo": {
                            "phone": {
                                "voice": "voice",
                                "facsimile": "facsimile"
                            },
                            "address": {
                                "deliveryPoint": "deliveryPoint",
                                "city": "city",
                                "postalCode": "postalCode",
                                "country": "country",
                                "elctronicMailAddress": "elctronicMailAddress"
                            },
                            "onlineResource": {
                                "linkage": "linkage",
                                "name": "name",
                                "description": "description",
                                "protocol": "protocol",
                                "function": "function"
                            }
                        },
                        "role": "role"
                    }
                ],
                "presentationForm": [
                    None
                ],
                "series": {
                    "name": "name",
                    "issueIdentification": "issueIdentification",
                    "page": "page"
                },
                "otherCitationDetails": "otherCitationDetails",
                "collectiveTitle": "collectiveTitle",
                "ISBN": "ISBN",
                "ISSN": "ISSN"
            }
        ]
    },
    "metadataExtensionInfo": None,
    "applicationSchemaInformation": None
}

feature_catalogue = {
    "name": "name",
    "scope": [
        "scope"
    ],
    "fieldOfApplication": [
        "fieldOfApplication"
    ],
    "versionNumber": "versionNumber",
    "versionDate": {
        "date": "date",
        "type": "type"
    },
    "producer": {
        "individualName": "individualName",
        "organisationName": "organisationName",
        "positionName": "positionName",
        "contactInfo": {
            "phone": {
                "voice": "voice",
                "facsimile": "facsimile"
            },
            "address": {
                "deliveryPoint": "deliveryPoint",
                "city": "city",
                "postalCode": "postalCode",
                "country": "country",
                "elctronicMailAddress": "elctronicMailAddress"
            },
            "onlineResource": {
                "linkage": "linkage",
                "name": "name",
                "description": "description",
                "protocol": "protocol",
                "function": "function"
            }
        },
        "role": "role"
    },
    "functionalLanguage": "functionalLanguage",
    "featureType": [
        {
            "typeName": "typeName",
            "definition": "definition",
            "code": "code",
            "isAbstract": True,
            "aliases": [
                "aliases"
            ],
            "carrierOfCharacteristics": [
                {
                    "memberName": "memberName",
                    "definition": "definition",
                    "cardinality": {
                        "lower": 0,
                        "upper": 0
                    },
                    "code": "code",
                    "valueMeasurementUnit": "valueMeasurementUnit",
                    "valueType": "valueType",
                    "listedValue": [
                        {
                            "label": "label",
                            "code": "code",
                            "definition": "definition"
                        }
                    ]
                }
            ]
        }
    ]
}

additional = {
    "additional": "additional info"
}

response = nada.create_geospatial_dataset(
    dataset_id=dataset_id,
    repository_id=repository_id,
    published=published,
    overwrite=overwrite,
    type=type,
    dataset_metadata=dataset_metadata,
    feature_catalogue=feature_catalogue,
    additional=additional
)

print(response)

# upload temporary thumbnail
thumbnail_path = nada.text_to_thumbnail("Geospatial\nDataset")
nada.upload_thumbnail(dataset_id, thumbnail_path)