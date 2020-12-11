from pynada import create_and_import

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
		"prod_date": "study production_statement prod_date",
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
				"name": "study distribution distributors name",
				"abbr": "study distribution distributors abbr",
				"affiliation": "study distribution distributors affiliation"
			}
		],
		"contact": [
			{
				"name": "study distribution contact name",
				"affiliation": "study distribution contact affiliation",
				"email": "study distribution contact email"
			}
		],
		"depositor": [
			{
				"name": "study distribution depositor name",
				"abbr": "study distribution depositor abbr",
				"affiliation": "study distribution depositor affiliation"
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
		"version": "study version",
		"version_date": "study version_date",
		"version_resp": "study version_resp",
		"version_notes": "study version_notes"
	},
	"bib_citation": "study bib_citation",
	"bib_citation_format": "study bib_citation_format",
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
		"date": "study_authorization date",
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
				"uri": "study_info keyword uri"
			}
		],
		"topics": [
			{
				"topic": "study_info topic",
				"vocab": "study_info topic vocab",
				"uri": "study_info topic tui"
			}
		],
		"abstract": "study_info abstract",
		"time_periods": [
			{
				"start": "study time_periods start",
				"end": "study time_periods end",
				"cycle": "study time_periods cycle"
			}
		],
		"coll_dates": [
			{
				"start": "study coll_dates start",
				"end": "study coll_dates end",
				"cycle": "study coll_dates cycle"
			}
		],
		"nation": [
			{
				"name": "study nation name",
				"abbreviation": "study nation abb"
			}
		],
		"bbox": [
			{
				"west": "study_info bbox west",
				"east": "study_info bbox east",
				"south": "study_info bbox south",
				"north": "study_info bbox north"
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
		"geog_coverage": "study_info geog_coverage",
		"geog_coverage_notes": "study_info geog_coverage_notes",
		"geog_unit": "study_info geog_unit",
		"analysis_unit": "study_info analysis_unit",
		"universe": "study_info universe",
		"data_kind": "study_info data_kind",
		"notes": "study_info notes",
		"quality_statement": {
			"standard_name": "study_info quality standard_name",
			"standard_producer": "study_info quality standard_producer",
			"standard_compliance_desc": "study_info quality standard_compliance_desc",
			"other_quality_statement": "study_info quality other_quality_statement"
		},
		"ex_post_evaluation": {
			"completion_date": "study_info ex_post_evaluation completion_date",
			"type": "study_info ex_post_evaluation type",
			"evaluator": [
				{
					"name": "study_info ex_post_evaluation evaluator name",
					"abbr": "study_info ex_post_evaluation evaluator abbr",
					"role": "study_info ex_post_evaluation evaluator role"
				}
			],
			"evaluation_process": "study_info ex_post_evaluation evaluation_process",
			"outcomes": "study_info ex_post_evaluation outcomes"
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
			"time_method": "method data_collection time_method",
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
			"frequency": "method data_collection frequency",
			"sampling_procedure": "method data_collection sampling_procedure",
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
					"num_of_units": "method data_collection sample_frame frame_unit num_of_units"
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
			"research_instrument": "Structured | Semi-structured | Unstructured",
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
			"response_rate": "method analysis_info response_rate",
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
			"command_language": "method coding_instruction command_language"
		}
	},
	"data_access": {
		"dataset_availability": {
			"access_place": "dataset_availability access_place",
			"access_place_url": "dataset_availability access_place_url",
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
					"uri": "dataset_use contact uri",
					"email": "dataset_use contact email"
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
		"file_id": "data_file id",
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
variables = [
	{
		"file_id": "variable file_id",
		"vid": "variable vid",
		"name": "variable name",
		"labl": "variable labl",
		"var_intrvl": "variable var_intrvl",
		"var_dcml": "variable var_dcml",
		"var_wgt": 0,
		"var_start_pos": 0,
		"var_end_pos": 0,
		"var_width": 0,
		"var_imputation": "variable var_imputation",
		"var_security": "variable var_security",
		"var_respunit": "variable var_respunit",
		"var_qstn_preqtxt": "variable var_qstn_preqtxt",
		"var_qstn_qstnlit": "variable var_qstn_qstnlit",
		"var_qstn_postqtxt": "variable var_qstn_postqtxt",
		"var_qstn_ivulnstr": "variable var_qstn_ivulnstr",
		"var_universe": "variable var_universe",
		"var_sumstat": [
			{
				"type": "variable var_sumstat type",
				"value": "variable var_sumstat value",
				"wgtd": "variable var_sumstat wgtd"
			}
		],
		"var_txt": "variable var_txt",
		"var_catgry": [
			{
				"value": "variable var_catgry value",
				"label": "variable var_catgry label",
				"stats": [
					{
						"type": "variable var_catgry stats type",
						"value": "variable var_catgry stats value",
						"wgtd": "variable var_catgry stats wgtd"
					}
				]
			}
		],
		"var_codinstr": "variable var_codinstr",
		"var_concept": [
			{
				"title": "variable var_concept title",
				"vocab": "variable var_concept vocab",
				"uri": "variable var_concept uri"
			}
		],
		"var_format": {
			"type": "variable var_format",
			"name": "variable name",
			"value": "variable value"
		},
		"var_notes": "variable var_notes"
	}
]
variable_groups = [
	{
		"vgid": "variable_group vgid",
		"variables": "variable_group variables",
		"variable_groups": "variable_group variable_groups",
		"group_type": "variable_group group_type",
		"label": "variable_group label",
		"universe": "variable_group universe",
		"notes": "variable_group notes",
		"txt": "variable_group txt",
		"definition": "variable_group definition"
	}
]
additional = {
	"additional": "additional info"
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
	variables=variables,
	variable_groups=variable_groups,
	additional=additional
)

print(response)
