import pynada as nada
import inspect

nada.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
nada.set_api_key(api_key)

#################################
# create_survey_dataset template
#################################

dataset_id = "SURVEY_DATASET_SAMPLE_01"
repository_id = "central"  # Collection ID that owns the survey
access_policy = "data_na"  # Data access policy for attached microdata resources. Valid values: "direct" "open" "public" "licensed" "remote" "data_na"
published = 0  # Status of the survey - 0=draft, 1=published
overwrite = "yes"  # Overwrite survey if already exists? Valid values: "yes" "no"
doc_desc = {
	"title": "metadata title",
	"idno": "metadata idno",
	"producers": [
		{
			"name": "metadata producer name",
			"abbr": "metadata producer abbr",
			"affiliation": "metadata producer affiliation",
			"role": "metadata producer role"
		}
	],
	"prod_date": "2020-12-10",
	"version_statement": {
		"version": "metadata verion",
		"version_date": "2020-01-01",
		"version_resp": "2020-03-01",
		"version_notes": "metadata version_notes"
	}
}
study_desc = {
	"title_statement": {
		"idno": dataset_id,  # Must be same as dataset_id
		"title": "[Template] Survey Dataset Sample 01",
		"sub_title": "sub_title",
		"alternate_title": "Survey Dataset Sample 01 (alternate_title)",
		"translated_title": "Survey Dataset Sample 01 (translated_title)"
	},
	"authoring_entity": [  # The person, corporate body, or agency responsible for the work's substantive and intellectual content. Repeat the element for each author, and use 'affiliation' attribute if available. Invert first and last name and use commas.
		{
			"name": "authoring_entity name",
			"affiliation": "authoring_entity affiliation"
		}
	],
	"oth_id": [  # Acknowledge any other people and institutions that have in some form contributed to the survey
		{
			"name": "oth_id name",  # Person or Agency name
			"role": "oth_id role",
			"affiliation": "oth_id affiliation"
		}
	],
	"production_statement": {
		"producers": [
			{
				"name": "producer name",
				"abbr": "producer abbr",
				"affiliation": "producer affiliation",
				"role": "producer role"
			}
		],
		"copyright": "production_statement copyright",
		"prod_date": "2020-12-31",  # Date when the marked-up document/marked-up document source/data collection/other material(s) were produced (not distributed or archived). The ISO standard for dates (YYYY-MM-DD) is recommended for use with the date attribute. Production date for data collection (2.1.3.3) maps to Dublin Core Date element.
		"prod_place": "production_statement prod_place",  # Address of the archive or organization that produced the work
		"funding_agencies": [  # The source(s) of funds for production of the work. If different funding agencies sponsored different stages of the production process, use the 'role' attribute to distinguish them.
			{
				"name": "production funding_agencies name",
				"abbr": "production funding_agencies abbr",
				"grant": "production funding_agencies grant",
				"role": "production funding_agencies role"
			}
		]
	},
	"distribution_statement": {
		"distributors": [  # The organization designated by the author or producer to generate copies of the particular work including any necessary editions or revisions. Names and addresses may be specified and other archives may be co-distributors. A URI attribute is included to provide an URN or URL to the ordering service or download facility on a Web site.
			{
				"name": "distributor name",  # Organization name
				"abbr": "distributor abbr",
				"affiliation": "distributor affiliation"
			}
		],
		"contact": [
			{
				"name": "distribution contact name",
				"affiliation": "distribution contact affiliation",
				"email": "distribution.contact@example.org"
			}
		],
		"depositor": [
			{
				"name": "distribution depositor name",
				"abbr": "distribution depositor abbr",
				"affiliation": "distribution depositor affiliation"
			}
		],
		"deposit_date": "2020-12-10",
		"distribution_date": "2020-12-10"
	},
	"series_statement": {
		"series_name": "study series_name",  # The name of the series to which the work belongs.
		"series_info": "study series_info"  # A survey may be repeated at regular intervals (such as an annual labour force survey), or be part of an international survey program (such as the MICS, CWIQ, DHS, LSMS and others). The Series information is a description of this collection of surveys. A brief description of the characteristics of the survey, including when it started, how many rounds were already implemented, and who is in charge would be provided here.
	},
	"version_statement": {
		"version": "version",
		"version_date": "version_date",
		"version_resp": "version_resp",  # The organization or person responsible for the version of the work
		"version_notes": "version_notes"
	},
	"bib_citation": "study bib_citation",  # Complete bibliographic reference containing all of the standard elements of a citation that can be used to cite the work. The 'bib_citation_format' field is provided to enable specification of the particular citation style used, e.g., APA, MLA, Chicago, etc.
	"bib_citation_format": "APA",  # Specification of the particular citation style used, e.g., APA, MLA, Chicago, etc.
	"holdings": [  # Information concerning either the physical or electronic holdings of the cited work. Attributes include: location--The physical location where a copy is held; callno--The call number for a work at the location specified; and URI--A URN or URL for accessing the electronic copy of the cited work.
		{
			"name": "study holdings name",
			"location": "study holdings location",
			"callno": "study holdings callno",
			"uri": "http://sample.org/study/holdings/uri"
		}
	],
	"study_notes": "study_notes",
	"study_authorization": {  # Provides structured information on the agency that authorized the study, the date of authorization, and an authorization statement
		"date": "2020-12-31",
		"agency": [  # The source(s) of funds for production of the work. If different funding agencies sponsored different stages of the production process, use the 'role' attribute to distinguish them.
			{
				"name": "study_authorization agency",
				"affiliation": "study_authorization affiliation",
				"abbr": "study_authorization abbr"
			}
		],
		"authorization_statement": "study authorization_statement"  # Authorization Statement
	},
	"study_info": {  # This section contains information about the data collection's scope across several dimensions, including substantive content, geography, and time.
		"study_budget": "study_info study_budget",  # Provide a clear summary of the pDescribe the budget of the project in as much detail as needed. Use XHTML structure elements to identify discrete pieces of information in a way that facilitates direct transfer of information on the study budget between DDI 2 and DDI 3 structures.urposes, objectives and content of the survey
		"keywords": [
			{
				"keyword": "study_info keyword",
				"vocab": "study_info keyword vocab",
				"uri": "http://example.org/study_desc/study_info/keyword/uri"
			}
		],
		"topics": [  # Topic Classification
			{
				"topic": "study_info topic",
				"vocab": "study_info topic vocab",
				"uri": "http://example.org/study_desc/study_info/topic/uri"
			}
		],
		"abstract": inspect.cleandoc("""\
		
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
			Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus.
			Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, sit amet tempus eros tristique eu. 
			Morbi ultrices mauris dignissim lacus dapibus efficitur. 
			
		"""),  # Provide a clear summary of the purposes, objectives and content of the survey
		"time_periods": [  # This field will usually be left empty. Time period differs from the dates of collection as they represent the period for which the data collected are applicable or relevant.
			{
				"start": "2020-01-01",
				"end": "2020-12-31",
				"cycle": "study time_periods cycle"
			}
		],
		"coll_dates": [  # Enter the dates (at least month and year) of the start and end of the data collection. In some cases, data collection for a same survey can be conducted in waves. In such case, you should enter the start and end date of each wave separately, and identify each wave in the 'cycle' field.
			{
				"start": "2020-01-01",
				"end": "2020-12-31",
				"cycle": "study coll_dates cycle"
			}
		],
		"nation": [  # Indicates the country or countries covered in the file. Field abbreviation may be used to list common abbreviations; use of ISO country codes is recommended. Maps to Dublin Core Coverage element. Inclusion of this element is recommended.
			{
				"name": "Templand",
				"abbreviation": "ISO"
			}
		],
		"bbox": [
			{
				"west": "0",
				"east": "20",
				"south": "0",
				"north": "20"
			}
		],
		"bound_poly": [  # This field allows the creation of multiple polygons to describe in a more detailed manner the geographic area covered by the dataset. It should only be used to define the outer boundaries of a covered area. For example, in the United States, such polygons can be created to define boundaries for Hawaii, Alaska, and the continental United States, but not interior boundaries for the contiguous states. This field is used to refine a coordinate-based search, not to actually map an area. If the boundPoly element is used, then geoBndBox MUST be present, and all points enclosed by the boundPoly MUST be contained within the geoBndBox. Elements westBL, eastBL, southBL, and northBL of the geoBndBox should each be represented in at least one point of the boundPoly description.
			{
				"lat": "0.0",  # Latitude (y coordinate) of a point. Valid range expressed in decimal degrees is as follows: -90,0 to 90,0 degrees (latitude)
				"lon": "0.0"  # Longitude (x coordinate) of a point. Valid range expressed in decimal degrees is as follows: -180,0 to 180,0 degrees (longitude)
			},
			{
				"lat": "10.0",
				"lon": "0.0"
			},
			{
				"lat": "10.0",
				"lon": "10.0"
			},
			{
				"lat": "0.0",
				"lon": "10.0"
			}
		],
		"geog_coverage": "geog_coverage",  # Information on the geographic coverage of the data. Includes the total geographic scope of the data, and any additional levels of geographic coding provided in the variables. Maps to Dublin Core Coverage element. Inclusion of this element in the codebook is recommended.
		"geog_coverage_notes": inspect.cleandoc("""\
		
			geog_coverage_notes
			Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus.
			Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, sit amet tempus eros tristique eu. 
			
		"""),  # Geographic coverage notes
		"geog_unit": "geog_unit",  # Lowest level of geographic aggregation covered by the data
		"analysis_unit": "analysis_unit",  # Basic unit(s) of analysis or observation that the study describes: individuals, families/households, groups, facilities, institutions/organizations, administrative units, physical locations, etc.
		"universe": "universe",  # We are interested here in the survey universe (not the universe of particular sections of the questionnaires or variables), i.e. in the identification of the population of interest in the survey. The universe will rarely be the entire population of the country. Sample household surveys, for example, usually do not cover homeless, nomads, diplomats, community households. Some surveys may cover only the population of a particular age group, or only male (or female), etc.
		"data_kind": "data_kind",  # Broad classification of the data
		"notes": inspect.cleandoc("""\
		
			study_info notes
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
			Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus.
			Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, sit amet tempus eros tristique eu. 
			
		"""),  # Study notes
		"quality_statement": {  # This structure consists of two parts, standardsCompliance and otherQualityStatements. In standardsCompliance list all specific standards complied with during the execution of this study. Note the standard name and producer and how the study complied with the standard. Enter any additional quality statements in otherQualityStatements.
			"standard_name": "quality standard_name",
			"standard_producer": "quality standard_producer",
			"standard_compliance_desc": "quality standard_compliance_desc",
			"other_quality_statement": "quality other_quality_statement"
		},
		"ex_post_evaluation": {  # This structure consists of two parts, standardsCompliance and otherQualityStatements. In standardsCompliance list all specific standards complied with during the execution of this study. Note the standard name and producer and how the study complied with the standard. Enter any additional quality statements in otherQualityStatements.
			"completion_date": "ex_post_evaluation completion_date",
			"type": "ex_post_evaluation type",
			"evaluator": [
				{
					"name": "ex_post_evaluation evaluator name",  # Funding Agency/Sponsor
					"abbr": "ex_post_evaluation evaluator abbr",
					"role": "ex_post_evaluation evaluator role"
				}
			],
			"evaluation_process": "ex_post_evaluation evaluation_process",
			"outcomes": "ex_post_evaluation outcomes"
		}
	},
	"study_development": {  # Describe the process of study development as a series of development activities. These activities can be typed using a controlled vocabulary. Describe the activity, listing participants with their role and affiliation, resources used (sources of information), and the outcome of the development activity.
		"activity_type": "study_development activity_type",
		"activity_description": "study_development activity_description",
		"participants": [
			{
				"name": "study_development participant name",
				"affiliation": "study_development participant affiliation",
				"role": "study_development participant role"
			}
		],
		"resource": {  # Development activity resource
			"data_source": [
				{
					"source": "study_development resource data_source"
				}
			],
			"source_origin": "study_development resource source_origin",  # For historical materials, information about the origin(s) of the sources and the rules followed in establishing the sources should be specified. May not be relevant to survey data.
			"source_char": "study_development resource source_char"  # Assessment of characteristics and quality of source material. May not be relevant to survey data.
		},
		"outcome": "study_development outcome"  # Development Activity Outcome
	},
	"method": {  # Methodology and processing
		"data_collection": {  # Information about the methodology employed in a data collection
			"time_method": "panel survey",  # The time method or time dimension of the data collection. Examples: panel survey, cross-section, trend study, time-series
			"data_collectors": [  # The persons and/or agencies that took charge of the data collection. This element includes 3 fields: Name, Abbreviation and the Affiliation. In most cases, we will record here the name of the agency, not the name of interviewers. Only in the case of very small-scale surveys, with a very limited number of interviewers, the name of person will be included as well. The field Affiliation is optional and not relevant in all cases.
				{
					"name": "method data_collection data_collector name",
					"abbr": "method data_collection data_collector abbr",
					"affiliation": "method data_collection data_collector affiliation"
				}
			],
			"collector_training": {  # Describes the training provided to data collectors including interviewer training, process testing, compliance with standards etc. This is repeatable for language and to capture different aspects of the training process. The type attribute allows specification of the type of training being described.
				"type": "method data_collection collector_training type",  # The percentage of sample members who provided information
				"training": "method data_collection collector_training training"  # Training provided to data collectors
			},
			"frequency": "monthly",  # For data collected at more than one point in time, the frequency with which the data were collected. Examples monthly, quarterly, yearly
			"sampling_procedure": "National multistage area probability sample",  # The type of sample and sample design used to select the survey respondents to represent the population. This field only applies to sample surveys. Information on sampling procedure is crucial (although not applicable for censuses and administrative datasets). Examples National multistage area probability sample, Simple random sample, Quota sample
			"sample_frame": {  # Sample frame describes the sampling frame used for identifying the population from which the sample was taken. For example, a telephone book may be a sample frame for a phone survey. In addition to the name, label and text describing the sample frame, this structure lists who maintains the sample frame, the period for which it is valid, a use statement, the universe covered, the type of unit contained in the frame as well as the number of units available, the reference period of the frame and procedures used to update the frame.
				"name": "method data_collection sample_frame name",  # Sample frame name
				"valid_period": [  # Defines a time period for the validity of the sampling frame. Enter dates in YYYY-MM-DD format.
					{
						"event": "start",  # Event e.g. start, end
						"date": "2020-12-31"
					}
				],
				"custodian": "method data_collection sample_frame custodian",  # Custodian identifies the agency or individual who is responsible for creating or maintaining the sample frame.
				"universe": "method data_collection sample_frame universe",  # The group of persons or other elements that are the object of research and to which any analytic results refer.
				"frame_unit": {  # Provides information about the sampling frame unit.
					"is_primary": True,  # Is a primary unit?
					"unit_type": "method data_collection sample_frame frame_unit unit_type",  # Describes the type of sampling frame unit.
					"num_of_units": "10"  # Number of units in the sampling frame
				},
				"reference_period": [  # Indicates the period of time in which the sampling frame was actually used for the study in question. Use ISO 8601 date/time formats to enter the relevant date(s).
					{
						"event": "start",  # Event e.g. start, end
						"date": "2020-12-31"
					}
				],
				"update_procedure": "method data_collection sample_frame update_procedure"  # Description of how and with what frequency the sample frame is updated.
			},
			"sampling_deviation": "method data_collection sampling_deviation",  # This field only applies to sample surveys. Sometimes the reality of the field requires a deviation from the sampling design (for example due to difficulty to access to zones due to weather problems, political instability, etc). If for any reason, the sample design has deviated, this should be reported here.
			"coll_mode": "method data_collection coll_mode",  # The mode of data collection is the manner in which the interview was conducted or information was gathered. In most cases, the response will be 'face to face interview'. But for some specific kinds of datasets, such as for example data on rain fall, the response will be different.
			"research_instrument": "Structured",  # The type of data collection instrument used. Structured indicates an instrument in which all respondents are asked the same questions/tests, possibly with precoded answers. If a small portion of such a questionnaire includes open-ended questions, provide appropriate comments. Semi-structured indicates that the research instrument contains mainly open-ended questions. Unstructured indicates that in-depth interviews were conducted.
			"instru_development": "method data_collection instru_development",  # Describe any development work on the data collection instrument. Type attribute allows for the optional use of a defined development type with or without use of a controlled vocabulary.
			"instru_development_type": "method data_collection instru_development_type",  # Instrument development type
			"sources": {  # Description of sources used for the data collection. The element is nestable so that the sources statement might encompass a series of discrete source statements, each of which could contain the facts about an individual source. This element maps to Dublin Core Source element.
				"data_source": [
					{
						"source": "method data_collection source data_source"
					}
				],
				"source_origin": "method data_collection source source_origin",  # For historical materials, information about the origin(s) of the sources and the rules followed in establishing the sources should be specified. May not be relevant to survey data.
				"source_char": "method data_collection source source_char",  # Assessment of characteristics and quality of source material. May not be relevant to survey data.
				"source_doc": "method data_collection source source_doc"  # Documentation and Access to Sources
			},
			"coll_situation": "method data_collection coll_situation",  # Description of noteworthy aspects of the data collection situation. Includes information on factors such as cooperativeness of respondents, duration of interviews, number of call-backs, etc.
			"act_min": "method data_collection act_min",  # Summary of actions taken to minimize data loss. Includes information on actions such as follow-up visits, supervisory checks, historical matching, estimation, etc.
			"control_operations": "method data_collection control_operations",  # Methods to facilitate data control performed by the primary investigator or by the data archive. Specify any special programs used for such operations.
			"weight": "method data_collection weight",  # The use of sampling procedures may make it necessary to apply weights to produce accurate statistical results. Describe here the criteria for using weights in analysis of a collection. If a weighting formula or coefficient was developed, provide this formula, define its elements, and indicate how the formula is applied to data.
			"cleaning_operations": "consistency checking"  # Methods used to clean the data collection, e.g., consistency checking, wildcode checking, etc.
		},
		"method_notes": "method_notes",  # Methodology notes
		"analysis_info": {  # Information about Data Appraisal
			"response_rate": "50%",  # The percentage of sample members who provided information
			"sampling_error_estimates": "method analysis_info sampling_error_estimates",  # Measure of how precisely one can estimate a population value from a given sample
			"data_appraisal": "method analysis_info data_appraisal"  # Other issues pertaining to data appraisal. Describe here issues such as response variance, nonresponse rate and testing for bias, interviewer and response bias, confidence levels, question bias, etc.
		},
		"study_class": "DDA Class C",  # Generally used to give the data archive's class or study status number, which indicates the processing status of the study. May also be used as a text field to describe processing status. Example: DDA Class C, Study is available from http://example.com
		"data_processing": "method data_processing",  # Describes various data processing procedures not captured elsewhere in the documentation, such as topcoding, recoding, suppression, tabulation, etc. The type attribute supports better classification of this activity, including the optional use of a controlled vocabulary
		"data_processing_type": "method data_processing_type",  # Data procssing type
		"coding_instructions": {  # Describe specific coding instructions used in data processing, cleaning, assession, or tabulation.
			"related_processes": "method coding_instruction related_processes",
			"type": "method coding_instruction type",
			"txt": "method coding_instruction txt",
			"command": "method coding_instruction command",  # Provide command code for the coding instruction. The formalLanguage attribute identifies the language of the command code.
			"command_language": "STATA"  # Identifies the language of the command code. e.g. SPSS, R, STATA
		}
	},
	"data_access": {
		"dataset_availability": {  # Information on availability and storage of the collection
			"access_place": "dataset_availability access_place",  # Location where the data collection is currently stored. Use the URL field access_place_url to provide a URN or URL for the storage site or the actual address from which the data may be downloaded
			"access_place_url": "http://example.org/study_desc/data_access/dataset_availability/access_place_url",  # Location where the data collection is currently stored. Provide a URN or URL for the storage site or the actual address from which the data may be downloaded
			"original_archive": "dataset_availability original_archive",  # Archive from which the data collection was obtained; the originating archive
			"status": "dataset_availability status",  # Statement of collection availability. An archive may need to indicate that a collection is unavailable because it is embargoed for a period of time, because it has been superseded, because a new edition is imminent, etc.
			"coll_size": "dataset_availability coll_size",  # Summarizes the number of physical files that exist in a collection, recording the number of files that contain data and noting whether the collection contains machine-readable documentation and/or other supplementary files and information such as data dictionaries, data definition statements, or data collection instruments.
			"complete": "dataset_availability complete",  # This item indicates the relationship of the data collected to the amount of data coded and stored in the data collection. Information as to why certain items of collected information were not included in the data file stored by the archive should be provided
			"file_quantity": "dataset_availability file_quantity",  # Total number of physical files associated with a collection
			"notes": "dataset_availability notes"  # Notes and comments
		},
		"dataset_use": {  # Information on terms of use for the data collection
			"conf_dec": [  # This element is used to determine if signing of a confidentiality declaration is needed to access a resource.
				{
					"txt": inspect.cleandoc("""\
					
						dataset_use conf_dec txt
						Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, sit amet tempus eros tristique eu. 
						
					"""),  # Confidentiality declaration text
					"required": "dataset_use conf_dec required",  # Is signing of a confidentiality declaration required
					"form_url": "http://example.org/study_desc/data_access/dataset_use/conf_dec/form_url",  # Provide a URN or URL for online access to a confidentiality declaration form.
					"form_id": "dataset_use conf_dec form_id"  # Indicates the number or ID of the form that the user must fill out
				}
			],
			"spec_perm": [  # Determine if any special permissions are required to access a resource
				{
					"txt": "dataset_use spec_perm txt",  # Confidentiality declaration text
					"required": "dataset_use spec_perm required",  # Indicate if special permissions are required to access a resource
					"form_url": "http://example.org/study_desc/data_access/dataset_use/spec_perm/form_url",  # Link to the form URL
					"form_id": "dataset_use spec_perm form_id"  # Indicates the number or ID of the form that the user must fill out
				}
			],
			"restrictions": "dataset_use restrictions",  # Any restrictions on access to or use of the collection such as privacy certification or distribution restrictions should be indicated here. These can be restrictions applied by the author, producer, or disseminator of the data collection. If the data are restricted to only a certain class of user, specify which type.
			"contact": [
				{
					"name": "dataset_use contact name",
					"affiliation": "dataset_use contact affiliation",
					"uri": "http://example.org/study_desc/data_access/dataset_use/contact/uri",
					"email": "dataset_use.contact.email@example.org"
				}
			],
			"cit_req": inspect.cleandoc("""\
			
				dataset_use cit_req
				Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus.
				Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, sit amet tempus eros tristique eu. 
				
			"""),  # Text of requirement that a data collection should be cited properly in articles or other publications that are based on analysis of the data.
			"deposit_req": "dataset_use deposit_req",  # Information regarding user responsibility for informing archives of their use of data through providing citations to the published work or providing copies of the manuscripts.
			"conditions": inspect.cleandoc("""\
			
				dataset_use conditions
				Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus.
				Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, sit amet tempus eros tristique eu. 
				
			"""),  # Indicates any additional information that will assist the user in understanding the access and use conditions of the data collection.
			"disclaimer": inspect.cleandoc("""\
			
				dataset_use disclaimer
				Maecenas sed odio sem. In ut sapien luctus, lacinia est ut, rutrum nunc. Nam dignissim lacus a elit auctor, sed ultricies dui vestibulum.
				
			"""),  # Information regarding responsibility for uses of the data collection
		},
		"notes": "data_access notes"
	}
}
data_files = [
	{
		"file_id": "data_file_id",
		"file_name": "data_file name",
		"description": "data_file description",
		"case_count": 0,
		"var_count": 0,
		"producer": "data_file producer",
		"data_checks": "data_file data_checks",
		"missing_data": "data_file missing_data",
		"version": "data_file version",
		"notes": "data_file notes"
	}
]
# variables = [
# 	{
# 		"file_id": "variable_file_id",  # File to which the variable belongs
# 		"vid": "variable_vid",  # Unique variable ID e.g. V1, V2
# 		"name": "variable_name",
# 		"labl": "variable_labl",
# 		"var_intrvl": "discrete",  # indicates the interval type; options are discrete or continuous. valid values: "discrete" "contin"
# 		"var_dcml": "3",  # Number of decimal points in the variable
# 		"var_wgt": 0,  # indicates whether the variable is a weight
# 		"var_start_pos": 0,  # Variable start position
# 		"var_end_pos": 0,  # Variable end position
# 		"var_width": 0,  # Variable width
# 		"var_imputation": "variable var_imputation",
# 		"var_security": "variable var_security",
# 		"var_respunit": "variable var_respunit",
# 		"var_qstn_preqtxt": "variable var_qstn_preqtxt",  # Text describing a set of conditions under which a question might be asked.
# 		"var_qstn_qstnlit": "variable var_qstn_qstnlit",  # Literal question
# 		"var_qstn_postqtxt": "variable var_qstn_postqtxt",  # Post-question text
# 		"var_qstn_ivulnstr": "variable var_qstn_ivulnstr",  # Interviewer instructions
# 		"var_universe": "variable var_universe",
# 		"var_sumstat": [  # One or more statistical measures that describe the responses to a particular variable and may include one or more standard summaries, e.g., minimum and maximum values, median, mode, etc.
# 			{
# 				"type": "variable var_sumstat type",
# 				"value": "variable var_sumstat value",
# 				"wgtd": "variable var_sumstat wgtd"
# 			}
# 		],
# 		"var_txt": "variable var_txt",
# 		"var_catgry": [
# 			{
# 				"value": "variable var_catgry value",
# 				"label": "variable var_catgry label",
# 				"stats": [
# 					{
# 						"type": "variable var_catgry stats type",
# 						"value": "variable var_catgry stats value",
# 						"wgtd": "variable var_catgry stats wgtd"
# 					}
# 				]
# 			}
# 		],
# 		"var_codinstr": "variable var_codinstr",
# 		"var_concept": [
# 			{
# 				"title": "variable var_concept title",
# 				"vocab": "variable var_concept vocab",
# 				"uri": "http://example.org/variables/var_concept/uri"
# 			}
# 		],
# 		"var_format": {  # The technical format of the variable in question. Attributes for this element include: 'type', which indicates if the variable is character or numeric; 'formatname,' which in some cases may provide the name of the particular, proprietary format actually used; 'schema,' which identifies the vendor or standards body that defined the format (acceptable choices are SAS, SPSS, IBM, ANSI, ISO, XML-data or other); 'category,' which describes what kind of data the format represents, and includes date, time, currency, or 'other' conceptual possibilities.
# 			"type": "variable var_format",
# 			"name": "variable name",
# 			"value": "variable value"
# 		},
# 		"var_notes": "variable var_notes"
# 	}
# ]
# variable_groups = [
# 	{
# 		"vgid": "variable_group_vgid",  # Unique ID for the variable group e.g. VG1
# 		"variables": "variable_group_variables",  # List of variables for the group seperated by space e.g. V1 V2 V3
# 		"variable_groups": "variable_group_variable_groups",  # List of sub-groups e.g. VG2 VG3 VG4
# 		"group_type": "subject",  # valid values: "subject" "section" "multiResp" "grid" "display" "repetition" "version" "iteration" "analysis" "pragmatic" "record" "file" "randomized" "other"
# 		"label": "variable_group label",
# 		"universe": "variable_group universe",
# 		"notes": "variable_group notes",
# 		"txt": "variable_group txt",
# 		"definition": "variable_group definition"
# 	}
# ]
additional = {
	"additional": "Additional metadata not covered by DDI elements"
}

response = nada.create_survey_dataset(
	dataset_id=dataset_id,
	repository_id=repository_id,
	access_policy=access_policy,
	published=published,
	overwrite=overwrite,
	doc_desc=doc_desc,
	study_desc=study_desc,
	data_files=data_files,
	# variables=variables,
	# variable_groups=variable_groups,
	additional=additional
)


# upload temporary thumbnail
thumbnail_path = nada.text_to_thumbnail("Survey\nDataset")
nada.upload_thumbnail(dataset_id, thumbnail_path)