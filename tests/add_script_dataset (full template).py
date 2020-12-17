from pynada import create_and_import
from pynada import utils
import inspect

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

##############################
# add_script_dataset template
##############################
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
		"title": "[Template] Script Dataset Sample 01",
		"sub_title": "Script Dataset Sample 01 (sub_title)",
		"alternate_title": "Script Dataset Sample 01 (alternate_title)",
		"translated_title": "Script Dataset Sample 01 (translated_title)"
	},
	"abstract": inspect.cleandoc("""\
		
		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
		Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. 
		Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, 
		non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, 
		sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. 
		
	"""),
	"review_board": "project review_board",
	"output": [
		{
			"type": "project output type",
			"title": "project output title",
			"authors": "project output authors",
			"description": inspect.cleandoc("""\
				
				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur.
				Nulla eget lacinia leo, at rutrum nibh. 
				Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue.
				
			"""),
			"abstract": inspect.cleandoc("""\
				
				Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. Mauris porttitor ante quis semper elementum. Nullam malesuada porta pellentesque. Sed at arcu vitae odio iaculis scelerisque in quis massa. 
				Mauris in leo interdum, ultricies justo et, convallis nulla. Curabitur vel turpis tincidunt, dictum ligula eu, ultrices mi.
				
			"""),
			"uri": "http://example.org/project_desc/output/uri",
			"doi": "project output doi"
		}
	],
	"approval_process": [
		{
			"approval_phase": "project approval_phase",
			"approval_authority": "project approval_authority",
			"submission_date": "2020-10-01",
			"reviewer": "project approval reviewer",
			"review_status": "project approval review_status",
			"approval_date": "202012-31"
		}
	],
	"project_website": [
		"http://example.org/project_desc/project_website"
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
		"erratum_description": inspect.cleandoc("""\
				
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
			
		"""),
	},
	"process": [
		{
			"name": "project process name",
			"date_start": "project process date_start",
			"date_end": "project process date_end",
			"description": inspect.cleandoc("""\
					
				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
				
			""")
		}
	],
	"authoring_entity": [
		{
			"name": "project authoring_entity name",
			"role": "project authoring_entity role",
			"affiliation": "project authoring_entity affiliation",
			"abbreviation": "project authoring_entity abbreviation",
			"email": "project.authoring_entity@example.org",
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
			"email": "project.curator@example.org",
			"url": "http://example.org/project_desc/curator/uri"
		}
	],
	"reviews_comments": {
		"comment_date": "project review comment_date",
		"comment_by": "project review comment_by",
		"comment_description": inspect.cleandoc("""\
				
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
			Fusce vel ante venenatis, dictum leo in, eleifend lectus. 
			Fusce blandit at nisl eu pellentesque. 
			Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
			
		"""),
		"comment_response": inspect.cleandoc("""\
				
			Aliquam luctus dolor sem, ac accumsan sapien elementum a. 
			Aenean porttitor vel turpis ac consectetur. 
			Nulla eget lacinia leo, at rutrum nibh. 
			Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. 
			Aenean lobortis augue et massa interdum faucibus. 
			
		""")
	},
	"acknowledgements": [
		{
			"name": "project acknowledgement name",
			"affiliation": "project acknowledgement affiliation",
			"role": "project acknowledgement role"
		}
	],
	"acknowledgement_statement": inspect.cleandoc("""\
				
		Vivamus mattis imperdiet urna, sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. Mauris porttitor ante quis semper elementum. Nullam malesuada porta pellentesque. Sed at arcu vitae odio iaculis scelerisque in quis massa. Mauris in leo interdum, ultricies justo et, convallis nulla. 
		Curabitur vel turpis tincidunt, dictum ligula eu, ultrices mi.
		
	"""),
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
	"technology_environment": inspect.cleandoc("""\
				
		Vivamus mattis imperdiet urna, 
		sit amet tempus eros tristique eu. 
		Morbi ultrices mauris dignissim lacus dapibus efficitur. 
		Mauris porttitor ante quis semper elementum. 
		Nullam malesuada porta pellentesque. 
		Sed at arcu vitae odio iaculis scelerisque in quis massa. 
		Mauris in leo interdum, ultricies justo et, convallis nulla. 
		Curabitur vel turpis tincidunt, dictum ligula eu, ultrices mi.
		
	"""),
	"technology_requirements": inspect.cleandoc("""\
				
		Maecenas sed odio sem. 
		In ut sapien luctus, 
		lacinia est ut, 
		rutrum nunc. 
		Nam dignissim lacus a elit auctor, 
		sed ultricies dui vestibulum. 
		Interdum et malesuada fames ac ante ipsum primis in faucibus. 
		
	"""),
	"reproduction_instructions": inspect.cleandoc("""\
				
		Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
		Donec nec ex egestas, 
		congue libero sit amet, 
		tincidunt risus. 
		Cras sed ligula pellentesque, 
		efficitur ex nec, 
		gravida sapien. 
		Nulla mollis, 
		tortor vitae ullamcorper iaculis, 
		felis metus molestie massa, 
		nec fringilla eros arcu quis tortor.
		
	"""),
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
			"file_name": "predicting_food_crises.R",
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
			"description": inspect.cleandoc("""\
						
				Donec at ultricies justo. Nulla porta felis libero, nec ultrices enim faucibus id. Suspendisse auctor dui in pretium aliquam. Pellentesque elementum massa mauris, ac tincidunt orci scelerisque nec. 
				Sed mattis mauris sed dolor elementum, eget facilisis purus aliquet. 
				Praesent eget iaculis augue, vel elementum purus. 
				
			"""),
			"methods": "script methods",
			"dependencies": "script dependencies",
			"instructions": inspect.cleandoc("""\
						
				Proin aliquam eleifend urna, ut rhoncus neque semper in. Integer a viverra tellus, quis tincidunt sem. Fusce nulla dui, commodo sit amet sem id, mattis eleifend lectus. Suspendisse eget tempus tortor. In quis cursus nulla.
				
			"""),
			"source_code_repo": "script source_code_repo",
			"notes": "script notes",
			"license": [
				{
					"name": "script license name",
					"uri": "http://example.org/project_desc/scripts/license"
				}
			]
		}
	],
	"data_statement": inspect.cleandoc("""\
						
		data_statement
		Proin aliquam eleifend urna, ut rhoncus neque semper in. Integer a viverra tellus, quis tincidunt sem. 
		Fusce nulla dui, commodo sit amet sem id, mattis eleifend lectus. Suspendisse eget tempus tortor. In quis cursus nulla.
		
	"""),
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
	"disclaimer": inspect.cleandoc("""\
						
		Proin aliquam eleifend urna, ut rhoncus neque semper in. Integer a viverra tellus, quis tincidunt sem. 
		
	"""),
	"confidentiality": inspect.cleandoc("""\
						
		Praesent auctor neque vel neque tristique facilisis vel non purus.
		
	"""),
	"citation_requirement": inspect.cleandoc("""\
						
		Mauris semper nibh eu erat elementum congue nec quis ligula. In in imperdiet lorem, et consectetur erat. Nam elit odio, ultrices eu tempus at, fringilla at tortor. Integer id rutrum est, sed ornare metus. 
		Praesent sollicitudin vitae est vel tristique.
		
	"""),
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

# upload temporary thumbnail
thumbnail_path = utils.text_to_thumbnail("Script\nDataset")
create_and_import.add_thumbnail(dataset_id, thumbnail_path)