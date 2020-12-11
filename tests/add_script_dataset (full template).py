from pynada import create_and_import

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

##########################
# add_script_dataset test
##########################
idno = "SCRIPT_DATASET_SAMPLE_01"

repositoryid = "central"
published = 0
overwrite = "yes"
doc_desc = {
	"title": "metadata document title",
	"idno": "metadata document idno",
	"producers": [
		{
			"name": "doc producer name",
			"abbr": "doc producer abbr",
			"affiliation": "doc producer affiliation",
			"role": "doc producer role"
		}
	],
	"prod_date": "2020-12-31",
	"version": "doc version"
}
project_desc = {
	"title_statement": {
		"idno": "SCRIPT_DATASET_SAMPLE_01",
		"title": "SCRIPT DATASET SAMPLE 01 (full title)",
		"sub_title": "SCRIPT DATASET SAMPLE 01 (sub_title)",
		"alternate_title": "SCRIPT DATASET SAMPLE 01 (alternate_title)",
		"translated_title": "SCRIPT DATASET SAMPLE 01 (translated_title)"
	},
	"abstract": "project abstract",
	"review_board": "project review_board",
	"output": [
		{
			"type": "project output type",
			"title": "project output title",
			"authors": "project output authors",
			"description": "project output description",
			"abstract": "project output abstract",
			"uri": "project output uri",
			"doi": "project output doi"
		}
	],
	"approval_process": [
		{
			"approval_phase": "project approval_phase",
			"approval_authority": "project approval_authority",
			"submission_date": "project approval submission_date",
			"reviewer": "project approval reviewer",
			"review_status": "project approval review_status",
			"approval_date": "project approval_date"
		}
	],
	"project_website": [
		"project_website"
	],
	"language": [
		{
			"name": "English",
			"code": "EN"
		}
	],
	"production_date": [
		"2020-12-31"
	],
	"version_statement": {
		"version": "project version",
		"version_date": "project version_date",
		"version_resp": "project version_resp",
		"version_notes": "project version_notes"
	},
	"errata": {
		"erratum_date": "project erratum_date",
		"erratum_description": "project erratum_description"
	},
	"process": [
		{
			"name": "project process name",
			"date_start": "project process date_start",
			"date_end": "project process date_end",
			"description": "project process description"
		}
	],
	"authoring_entity": [
		{
			"name": "project authoring_entity name",
			"role": "project authoring_entity role",
			"affiliation": "project authoring_entity affiliation",
			"abbreviation": "project authoring_entity abbreviation",
			"email": "project authoring_entity email",
			"author_id": [
				{
					"type": "project author_id type",
					"id": "project author_id id"
				}
			]
		}
	],
	"contributors": [
		{
			"name": "project contributor name",
			"role": "project contributor role",
			"affiliation": "project contributor affiliation",
			"abbreviation": "project contributor abbreviation",
			"email": "project contributor email",
			"url": "project contributor url"
		}
	],
	"sponsors": [
		{
			"name": "project sponsors name",
			"abbr": "project sponsors abbr",
			"role": "project sponsors role",
			"grant_no": "project sponsors grant_no"
		}
	],
	"curators": [
		{
			"name": "project curator name",
			"role": "project curator role",
			"affiliation": "project curator affiliation",
			"abbreviation": "project curator abbreviation",
			"email": "project curator email",
			"url": "project curator url"
		}
	],
	"reviews_comments": {
		"comment_date": "project review comment_date",
		"comment_by": "project review comment_by",
		"comment_description": "project review comment_description",
		"comment_response": "project review comment_response"
	},
	"acknowledgements": [
		{
			"name": "project acknowledgement name",
			"affiliation": "project acknowledgement affiliation",
			"role": "project acknowledgement role"
		}
	],
	"acknowledgement_statement": "project acknowledgement_statement",
	"related_projects": [
		{
			"name": "project related_project name",
			"uri": "project related_project uri",
			"note": "project related_project note"
		}
	],
	"geographic_units": [
		{
			"name": "project geographic_unit name",
			"code": "project geographic_unit code",
			"type": "project geographic_unit type"
		}
	],
	"keywords": [
		{
			"name": "project keyword name",
			"vocabulary": "project keyword vocabulary",
			"uri": "project keyword uri"
		}
	],
	"themes": [
		{
			"name": "project theme name",
			"vocabulary": "project theme vocabulary",
			"uri": "project theme uri"
		}
	],
	"topics": [
		{
			"id": "project topic id",
			"name": "project topic name",
			"parent_id": "project topic parent_id",
			"vocabulary": "project topic vocabulary",
			"uri": "project topic uri"
		}
	],
	"disciplines": [
		{
			"name": "project disciplines name",
			"vocabulary": "project disciplines vocabulary",
			"uri": "project disciplines uri"
		}
	],
	"repository_uri": [
		{
			"name": "project repository name",
			"type": "project repository type",
			"uri": "project repository uri"
		}
	],
	"license": [
		{
			"name": "project license name",
			"uri": "project license uri"
		}
	],
	"technology_environment": "project technology_environment",
	"technology_requirements": "project technology_requirements",
	"reproduction_instructions": "project reproduction_instructions",
	"methods": [
		{
			"name": "project method name",
			"note": "project method note"
		}
	],
	"software": [
		{
			"name": "project software name",
			"version": "project software version",
			"library": [
				"project software library"
			]
		}
	],
	"scripts": [
		{
			"file_name": "script file_name",
			"zip_package": "script zip_package",
			"title": "script title",
			"authors": [
				{
					"name": "script author name",
					"abbr": "script author abbr",
					"role": "script author role"
				}
			],
			"date": "script date",
			"format": "script format",
			"software": "script software",
			"description": "script description",
			"methods": "script methods",
			"dependencies": "script dependencies",
			"instructions": "script instructions",
			"source_code_repo": "script source_code_repo",
			"notes": "script notes",
			"license": [
				{
					"name": "script license name",
					"uri": "script license uri"
				}
			]
		}
	],
	"data_statement": "project data_statement",
	"datasets": [
		{
			"name": "project dataset name",
			"idno": "project dataset idno",
			"note": "project dataset note",
			"access_type": "project dataset access_type",
			"license": "project dataset license",
			"license_uri": "project dataset license_uri",
			"uri": "project dataset uri"
		}
	],
	"contacts": [
		{
			"name": "project contact name",
			"affiliation": "project contact affiliation",
			"role": "project contact role",
			"uri": "project contact uri",
			"phone": "project contact phone"
		}
	],
	"tags": [
		{
			"tag": "project tag"
		}
	],
	"copyright": "project copyright",
	"disclaimer": "project disclaimer",
	"confidentiality": "project confidentiality",
	"citation_requirement": "project citation_requirement"
}

response = create_and_import.add_script_dataset(
	idno=idno,
	repositoryid=repositoryid,
	published=published,
	overwrite=overwrite,
	doc_desc=doc_desc,
	project_desc=project_desc
)

print(response)
