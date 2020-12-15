from pynada import create_and_import
from pynada import utils

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

##########################
# add_survey_dataset test
##########################
idno = "SURVEY_DATASET_SAMPLE_01"

repositoryid = "central"
access_policy = "data_na"
published = 0
overwrite = "yes"
doc_desc = {
	"title": "doc title",
	"idno": "doc idno",
	"producers": [
		{
			"name": "doc producer name",
			"abbr": "doc producer abbr",
			"affiliation": "doc producer affiliation",
			"role": "doc producer role"
		}
	],
	"prod_date": "2020-12-10",
	"version_statement": {
		"version": "doc verion",
		"version_date": "doc version_date",
		"version_resp": "doc version_resp",
		"version_notes": "doc version_notes"
	}
}
study_desc = {
	"title_statement": {
		"idno": "SURVEY_DATASET_SAMPLE_01",
		"title": "SURVEY DATASET SAMPLE 01 (Full Title)",
		"sub_title": "SURVEY DATASET SAMPLE 01",
		"alternate_title": "SURVEY DATASET SAMPLE 01 (alternate_title)",
		"translated_title": "SURVEY DATASET SAMPLE 01 (translated_title)"
	},
	"authoring_entity": [
		{
			"name": "study authoring_entity name",
			"affiliation": "study authoring_entity affiliation"
		}
	],
	"oth_id": [
		{
			"name": "study oth_id name",
			"role": "study oth_id role",
			"affiliation": "study oth_id affiliation"
		}
	],
	"production_statement": {
		"producers": [
			{
				"name": "study production_statement producer name",
				"abbr": "study production_statement producer abbr",
				"affiliation": "study production_statement producer affiliation",
				"role": "study production_statement producer role"
			}
		],
		"copyright": "study production_statement copyright",
		"prod_date": "2020-12-31",
		"prod_place": "study production_statement prod_place",
		"funding_agencies": [
			{
				"name": "study production funding_agencies name",
				"abbr": "study production funding_agencies abbr",
				"grant": "study production funding_agencies grant",
				"role": "study production funding_agencies role"
			}
		]
	},
	"distribution_statement": {
		"distributors": [
			{
				"name": "distribution distributors name",
				"abbr": "distribution distributors abbr",
				"affiliation": "distribution distributors affiliation"
			}
		],
		"contact": [
			{
				"name": "distribution contact name",
				"affiliation": "distribution contact affiliation",
				"email": "distribution contact email"
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
		"series_name": "study series_name",
		"series_info": "study series_info"
	},
	"version_statement": {
		"version": "version",
		"version_date": "version_date",
		"version_resp": "version_resp",
		"version_notes": "version_notes"
	},
	"bib_citation": "study bib_citation",
	"bib_citation_format": "APA",  # Specification of the particular citation style used
	"holdings": [
		{
			"name": "study holdings name",
			"location": "study holdings location",
			"callno": "study holdings callno",
			"uri": "http://sample.org/study/holdings/uri"
		}
	],
	"study_notes": "study_notes",
	"study_authorization": {
		"date": "2020-12-31",
		"agency": [
			{
				"name": "study_authorization agency",
				"affiliation": "study_authorization affiliation",
				"abbr": "study_authorization abbr"
			}
		],
		"authorization_statement": "study authorization_statement"
	},
	"study_info": {
		"study_budget": "study_info study_budget",
		"keywords": [
			{
				"keyword": "study_info keyword",
				"vocab": "study_info keyword vocab",
				"uri": "http://example.org/study_desc/study_info/keyword/uri"
			}
		],
		"topics": [
			{
				"topic": "study_info topic",
				"vocab": "study_info topic vocab",
				"uri": "http://example.org/study_desc/study_info/topic/uri"
			}
		],
		"abstract": "study_info abstract",
		"time_periods": [
			{
				"start": "2020-01-01",
				"end": "2020-12-31",
				"cycle": "study time_periods cycle"
			}
		],
		"coll_dates": [
			{
				"start": "2020-01-01",
				"end": "2020-12-31",
				"cycle": "study coll_dates cycle"
			}
		],
		"nation": [
			{
				"name": "study nation name",
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
		"bound_poly": [
			{
				"lat": "0.0",
				"lon": "0.0"
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
		"geog_coverage": "geog_coverage",
		"geog_coverage_notes": "geog_coverage_notes",
		"geog_unit": "geog_unit",
		"analysis_unit": "analysis_unit",
		"universe": "universe",
		"data_kind": "data_kind",
		"notes": "study_info notes",
		"quality_statement": {
			"standard_name": "quality standard_name",
			"standard_producer": "quality standard_producer",
			"standard_compliance_desc": "quality standard_compliance_desc",
			"other_quality_statement": "quality other_quality_statement"
		},
		"ex_post_evaluation": {
			"completion_date": "ex_post_evaluation completion_date",
			"type": "ex_post_evaluation type",
			"evaluator": [
				{
					"name": "ex_post_evaluation evaluator name",
					"abbr": "ex_post_evaluation evaluator abbr",
					"role": "ex_post_evaluation evaluator role"
				}
			],
			"evaluation_process": "ex_post_evaluation evaluation_process",
			"outcomes": "ex_post_evaluation outcomes"
		}
	},
	"study_development": {
		"activity_type": "study_development activity_type",
		"activity_description": "study_development activity_description",
		"participants": [
			{
				"name": "study_development participant name",
				"affiliation": "study_development participant affiliation",
				"role": "study_development participant role"
			}
		],
		"resource": {
			"data_source": [
				{
					"source": "study_development resource data_source"
				}
			],
			"source_origin": "study_development resource source_origin",
			"source_char": "study_development resource source_char"
		},
		"outcome": "study_development outcome"
	},
	"method": {
		"data_collection": {
			"time_method": "panel survey",  # The time method or time dimension of the data collection. Examples: panel survey, h>cross-section, trend study, time-series
			"data_collectors": [
				{
					"name": "method data_collection data_collector name",
					"abbr": "method data_collection data_collector abbr",
					"affiliation": "method data_collection data_collector affiliation"
				}
			],
			"collector_training": {
				"type": "method data_collection collector_training type",
				"training": "method data_collection collector_training training"
			},
			"frequency": "monthly",  # For data collected at more than one point in time, the frequency with which the data were collected. Examples monthly, quarterly, yearly
			"sampling_procedure": "National multistage area probability sample",  # The type of sample and sample design used to select the survey respondents to represent the population. This field only applies to sample surveys. Information on sampling procedure is crucial
			"sample_frame": {
				"name": "method data_collection sample_frame name",
				"valid_period": [
					{
						"event": "method data_collection sample_frame valid_period event",
						"date": "2020-12-31"
					}
				],
				"custodian": "method data_collection sample_frame custodian",
				"universe": "method data_collection sample_frame universe",
				"frame_unit": {
					"is_primary": True,
					"unit_type": "method data_collection sample_frame frame_unit unit_type",
					"num_of_units": "10"
				},
				"reference_period": [
					{
						"event": "method data_collection sample_frame reference_period event",
						"date": "2020-12-31"
					}
				],
				"update_procedure": "method data_collection sample_frame update_procedure"
			},
			"sampling_deviation": "method data_collection sampling_deviation",
			"coll_mode": "method data_collection coll_mode",
			"research_instrument": "Structured",  # The type of data collection instrument used. Structured | Semi-structured | Unstructured
			"instru_development": "method data_collection instru_development",
			"instru_development_type": "method data_collection instru_development_type",
			"sources": {
				"data_source": [
					{
						"source": "method data_collection source data_source"
					}
				],
				"source_origin": "method data_collection source source_origin",
				"source_char": "method data_collection source source_char",
				"source_doc": "method data_collection source source_doc"
			},
			"coll_situation": "method data_collection coll_situation",
			"act_min": "method data_collection act_min",
			"control_operations": "method data_collection control_operations",
			"weight": "method data_collection weight",
			"cleaning_operations": "method data_collection cleaning_operations"
		},
		"method_notes": "method_notes",
		"analysis_info": {
			"response_rate": "50%",  # The percentage of sample members who provided information
			"sampling_error_estimates": "method analysis_info sampling_error_estimates",
			"data_appraisal": "method analysis_info data_appraisal"
		},
		"study_class": "method study_class",
		"data_processing": "method data_processing",
		"data_processing_type": "method data_processing_type",
		"coding_instructions": {
			"related_processes": "method coding_instruction related_processes",
			"type": "method coding_instruction type",
			"txt": "method coding_instruction txt",
			"command": "method coding_instruction command",
			"command_language": "STATA"  # Identifies the language of the command code.
		}
	},
	"data_access": {
		"dataset_availability": {
			"access_place": "dataset_availability access_place",
			"access_place_url": "http://example.org/study_desc/data_access/dataset_availability/access_place_url",
			"original_archive": "dataset_availability original_archive",
			"status": "dataset_availability status",
			"coll_size": "dataset_availability coll_size",
			"complete": "dataset_availability complete",
			"file_quantity": "dataset_availability file_quantity",
			"notes": "dataset_availability notes"
		},
		"dataset_use": {
			"conf_dec": [
				{
					"txt": "dataset_use conf_dec txt",
					"required": "dataset_use conf_dec required",
					"form_url": "dataset_use conf_dec form_url",
					"form_id": "dataset_use conf_dec form_id"
				}
			],
			"spec_perm": [
				{
					"txt": "dataset_use spec_perm txt",
					"required": "dataset_use spec_perm required",
					"form_url": "dataset_use spec_perm form_url",
					"form_id": "dataset_use spec_perm form_id"
				}
			],
			"restrictions": "dataset_use restrictions",
			"contact": [
				{
					"name": "dataset_use contact name",
					"affiliation": "dataset_use contact affiliation",
					"uri": "http://example.org/study_desc/data_access/dataset_use/contact/uri",
					"email": "dataset_use.contact.email@example.org"
				}
			],
			"cit_req": "dataset_use cit_req",
			"deposit_req": "dataset_use deposit_req",
			"conditions": "dataset_use conditions",
			"disclaimer": "dataset_use disclaimer"
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
# 		"file_id": "variable_file_id",
# 		"vid": "variable_vid",
# 		"name": "variable_name",
# 		"labl": "variable_labl",
# 		"var_intrvl": "discrete",  # valid values: "discrete" "contin"
# 		"var_dcml": "3",  # Number of decimal points in the variable
# 		"var_wgt": 0,
# 		"var_start_pos": 0,
# 		"var_end_pos": 0,
# 		"var_width": 0,
# 		"var_imputation": "variable var_imputation",
# 		"var_security": "variable var_security",
# 		"var_respunit": "variable var_respunit",
# 		"var_qstn_preqtxt": "variable var_qstn_preqtxt",
# 		"var_qstn_qstnlit": "variable var_qstn_qstnlit",
# 		"var_qstn_postqtxt": "variable var_qstn_postqtxt",
# 		"var_qstn_ivulnstr": "variable var_qstn_ivulnstr",
# 		"var_universe": "variable var_universe",
# 		"var_sumstat": [
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
# 		"var_format": {
# 			"type": "variable var_format",
# 			"name": "variable name",
# 			"value": "variable value"
# 		},
# 		"var_notes": "variable var_notes"
# 	}
# ]
# variable_groups = [
# 	{
# 		"vgid": "variable_group_vgid",
# 		"variables": "variable_group_variables",
# 		"variable_groups": "variable_group_variable_groups",
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

response = create_and_import.add_survey_dataset(
	idno=idno,
	repositoryid=repositoryid,
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

print(response)

utils.text_to_thumbnail("Survey\nDataset")
create_and_import.add_thumbnail(idno, "temp_thumbnail.jpg")