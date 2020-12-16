from pynada import create_and_import
from pynada import utils

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

##########################
# add_script_dataset test
##########################
dataset_id = "SCRIPT_DATASET_SAMPLE_01"

repository_id = "central"
published = 0
overwrite = "yes"
doc_desc = {
	"title": "metadata document title",
	"idno": "metadata document idno",
	"producers": [
		{
			"name": "metadata producer name",
			"abbr": "metadata producer abbr",
			"affiliation": "metadata producer affiliation",
			"role": "metadata producer role"
		}
	],
	"prod_date": "2020-12-31",
	"version": "metadata version"
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
			"uri": "http://example.org/project_desc/output/uri",
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
			"url": "http://example.org/project_desc/contributor/uri"
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
			"url": "http://example.org/project_desc/curator/uri"
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
			"uri": "http://example.org/project_desc/related_project/uri",
			"note": "project related_project note"
		}
	],
	"geographic_units": [
		{
			"name": "geographic_unit name",
			"code": "geographic_unit code",
			"type": "geographic_unit type"
		}
	],
	"keywords": [
		{
			"name": "keyword name",
			"vocabulary": "keyword vocabulary",
			"uri": "http://example.org/project_desc/keyword/uri"
		}
	],
	"themes": [
		{
			"name": "theme name",
			"vocabulary": "theme vocabulary",
			"uri": "http://example.org/project_desc/theme/uri"
		}
	],
	"topics": [
		{
			"id": "topic id",
			"name": "topic name",
			"parent_id": "topic parent_id",
			"vocabulary": "topic vocabulary",
			"uri": "http://example.org/project_desc/topic/uri"
		}
	],
	"disciplines": [
		{
			"name": "disciplines name",
			"vocabulary": "disciplines vocabulary",
			"uri": "http://example.org/project_desc/discipline/uri"
		}
	],
	"repository_uri": [
		{
			"name": "repository name",
			"type": "repository type",
			"uri": "http://example.org/project_desc/repository_uri/uri"
		}
	],
	"license": [
		{
			"name": "license name",
			"uri": "http://example.org/project_desc/license/uri"
		}
	],
	"technology_environment": "technology_environment",
	"technology_requirements": "technology_requirements",
	"reproduction_instructions": "reproduction_instructions",
	"methods": [
		{
			"name": "method name",
			"note": "method note"
		}
	],
	"software": [
		{
			"name": "software name",
			"version": "software version",
			"library": [
				"software library"
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
			"license_uri": "http://example.org/project_desc/dataset/license_uri",
			"uri": "http://example.org/project_desc/dataset/uri"
		}
	],
	"contacts": [
		{
			"name": "contact name",
			"affiliation": "contact affiliation",
			"role": "contact role",
			"uri": "http://example.org/project_desc/contact/uri",
			"phone": "contact phone"
		}
	],
	"tags": [
		{
			"tag": "tag"
		}
	],
	"copyright": "copyright",
	"disclaimer": "disclaimer",
	"confidentiality": "confidentiality",
	"citation_requirement": "citation_requirement"
}

response = create_and_import.add_script_dataset(
	dataset_id=dataset_id,
	repository_id=repository_id,
	published=published,
	overwrite=overwrite,
	doc_desc=doc_desc,
	project_desc=project_desc
)

print(response)

utils.text_to_thumbnail("Geospatial\nDataset")
create_and_import.add_thumbnail(dataset_id, "temp_thumbnail.jpg")