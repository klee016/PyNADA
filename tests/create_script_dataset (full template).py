from pynada import create_and_import
from pynada import utils
import inspect

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = open("API Key.txt", "r").read()
create_and_import.set_api_key(api_key)

#################################
# create_script_dataset template
#################################

dataset_id = "SCRIPT_DATASET_SAMPLE_01"
repository_id = "central"  # Collection ID that owns the project
published = 0  # Status of the project: 0=draft, 1=published
overwrite = "yes"  # Overwrite document if already exists? Valid values: "yes" "no"
doc_desc = {  # Document description; the Document is the file containing the structured metadata
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
	"prod_date": "2020-12-31",  # Document production date using format(YYYY-MM-DD)
	"version": "metadata version"  # Identify and describe the current version of the document
}
project_desc = {  # Description of the research project
	"title_statement": {
		"idno": dataset_id, # Must be same as dataset_id
		"title": "[Template] Script Dataset Sample 01",  # The title is the name of the project, which may correspond to the title of an academic paper, of a project impact evaluation, etc.
		"sub_title": "Script Dataset Sample 01 (sub_title)",  # A short subtitle for the project
		"alternate_title": "Script Dataset Sample 01 (alternate_title)",  # The abbreviation of a project is usually the first letter of each word of the project title. The project reference year(s) may be included.
		"translated_title": "Script Dataset Sample 01 (translated_title)"  # In countries with more than one official language, a translation of the title may be provided.
	},
	"abstract": inspect.cleandoc("""\
		
		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
		Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. 
		Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, 
		non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, 
		sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. 
		
	"""),
	"review_board": inspect.cleandoc("""\
		
		Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
		Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur. 
		Nulla eget lacinia leo, at rutrum nibh. Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, 
		non elementum lorem nisl quis augue. Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, 
		sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. 
		
	"""),  # Information on whether and when the project was submitted, reviewed, and approved by an institutional review board (or independent ethics committee, ethical review board (ERB), research ethics board, or equivalent).
	"output": [  # Description of outputs of the research project
		{
			"type": "Working paper",  # Type of outputs of the script/research project. Example: Working paper, On-line interactive data visualization (ideally, a controlled vocabulary should be used)
			"title": "project output title",  # Title of the output
			"authors": "project output authors",
			"description": inspect.cleandoc("""\
				
				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. Aliquam luctus dolor sem, ac accumsan sapien elementum a. Aenean porttitor vel turpis ac consectetur.
				Nulla eget lacinia leo, at rutrum nibh. 
				Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue.
				
			"""),  # Brief description of the output; for articles and working papers, this can include the bibliographic citation.
			"abstract": inspect.cleandoc("""\
				
				Aenean lobortis augue et massa interdum faucibus. Vivamus mattis imperdiet urna, sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. Mauris porttitor ante quis semper elementum. Nullam malesuada porta pellentesque. Sed at arcu vitae odio iaculis scelerisque in quis massa. 
				Mauris in leo interdum, ultricies justo et, convallis nulla. Curabitur vel turpis tincidunt, dictum ligula eu, ultrices mi.
				
			"""),
			"uri": "http://example.org/project_desc/output/uri",
			"doi": "project output doi"  # Digital Object Identifier (DOI) of the output
		}
	],
	"approval_process": [  # A description of the project output review process
		{
			"approval_phase": "project approval_phase",
			"approval_authority": "project approval_authority",
			"submission_date": "2020-10-01",
			"reviewer": "project approval reviewer",
			"review_status": "project approval review_status",
			"approval_date": "202012-31"
		}
	],
	"project_website": [  # Project website link
		"http://example.org/project_desc/project_website"
	],
	"language": [  # Documentation language e.g. English, French, etc.
		{
			"name": "English",
			"code": "EN"
		}
	],
	"production_date": [  # Date in ISO format when the dissemination-ready version of the research project was produced. It can be a year (YYYY), year-month (YYYY-MM), or year-month-day (YYYY-MM-DD)
		"2020-12-31"
	],
	"version_statement": {
		"version": "project version",
		"version_date": "project version_date",
		"version_resp": "project version_resp",  # The organization or person responsible for the version of the work
		"version_notes": "project version_notes"
	},
	"errata": {  # List of corrected errors in data, scripts or output
		"erratum_date": "project erratum_date",
		"erratum_description": inspect.cleandoc("""\
				
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
			
		"""),
	},
	"process": [  # A description, following a logical sequence, of the various phases of the research project implementation. This field may be used to document explorations steps that may have resulted in dead ends, to document intermediary steps at which a project may have been reviewed and approved, etc.
		{
			"name": "project process name",  # A short name for the implementation phase
			"date_start": "project process date_start",  # Start date of the phase period (as a string; recommended ISO format YYY or YYY-MM or YYY-MM-DD)
			"date_end": "project process date_end",  # End date of the phase period (as a string; recommended ISO format YYY or YYY-MM or YYY-MM-DD)
			"description": inspect.cleandoc("""\
					
				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vel ante venenatis, dictum leo in, eleifend lectus. Fusce blandit at nisl eu pellentesque. Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
				
			""")  # Description of the implementation phase
		}
	],
	"authoring_entity": [  # The person, corporate body, or agency responsible for the project's substantive and intellectual content. Repeat the element for each author/primary investigator, and use 'affiliation' attribute if available. Invert first and last name and use commas.
		{
			"name": "project authoring_entity name",  # Name of the person, corporate body, or agency responsible for the work's substantive and intellectual content. If a person, invert first and last name and use commas.
			"role": "project authoring_entity role",  # Title of the person (if any) responsible for the work's substantive and intellectual content.
			"affiliation": "project authoring_entity affiliation",
			"abbreviation": "project authoring_entity abbreviation",
			"email": "project.authoring_entity@example.org",
			"author_id": [  # Unique identifier of an author, which may be provided by services like ORCID or other
				{
					"type": "ORCID",  # Source of identifier, e.g. ORCID
					"id": "project author_id id"  # Author's unique identifier for the corresponding source
				}
			]
		}
	],
	"contributors": [  # The person, corporate body, or agency who contributed to the project.
		{
			"name": "project contributor name",  # Name of the person, corporate body, or agency responsible for the work's substantive and intellectual content. If a person, invert first and last name and use commas.
			"role": "project contributor role",  # Title of the person (if any) responsible for the work's substantive and intellectual content.
			"affiliation": "project contributor affiliation",
			"abbreviation": "project contributor abbreviation",
			"email": "project.contributor@example.org",
			"url": "http://example.org/project_desc/contributor/uri"
		}
	],
	"sponsors": [  # The source(s) of funds for production of the work. If different funding agencies sponsored different stages of the production process, use the 'role' attribute to distinguish them.
		{
			"name": "project sponsors name",
			"abbr": "project sponsors abbr",
			"role": "project sponsors role",
			"grant_no": "project sponsors grant_no"
		}
	],
	"curators": [  # The person, corporate body, or agency who curated the project.
		{
			"name": "project curator name",  # Name of the person, corporate body, or agency responsible for the project curation. If a person, invert first and last name and use commas.
			"role": "project curator role",
			"affiliation": "project curator affiliation",
			"abbreviation": "project curator abbreviation",
			"email": "project.curator@example.org",
			"url": "http://example.org/project_desc/curator/uri"
		}
	],
	"reviews_comments": {  # List and description of reviews and comments received on the project
		"comment_date": "project review comment_date",  # Date when the comment was provided
		"comment_by": "project review comment_by",  # Name and title of the comment provider (individual or organization)
		"comment_description": inspect.cleandoc("""\
				
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
			Fusce vel ante venenatis, dictum leo in, eleifend lectus. 
			Fusce blandit at nisl eu pellentesque. 
			Curabitur massa ante, rutrum vitae nibh nec, volutpat dignissim urna. 
			
		"""),  # A description of the comment
		"comment_response": inspect.cleandoc("""\
				
			Aliquam luctus dolor sem, ac accumsan sapien elementum a. 
			Aenean porttitor vel turpis ac consectetur. 
			Nulla eget lacinia leo, at rutrum nibh. 
			Phasellus vestibulum, lorem in ullamcorper lacinia, neque tellus convallis est, non elementum lorem nisl quis augue. 
			Aenean lobortis augue et massa interdum faucibus. 
			
		""")  # Response by the primary investigator or research team on the comment
	},
	"acknowledgements": [  # Acknowledgments of persons or organizations (other than sponsors) who contributed to the project.
		{
			"name": "project acknowledgement name",
			"affiliation": "project acknowledgement affiliation",
			"role": "project acknowledgement role"
		}
	],
	"acknowledgement_statement": inspect.cleandoc("""\
				
		Vivamus mattis imperdiet urna, sit amet tempus eros tristique eu. Morbi ultrices mauris dignissim lacus dapibus efficitur. Mauris porttitor ante quis semper elementum. Nullam malesuada porta pellentesque. Sed at arcu vitae odio iaculis scelerisque in quis massa. Mauris in leo interdum, ultricies justo et, convallis nulla. 
		Curabitur vel turpis tincidunt, dictum ligula eu, ultrices mi.
		
	"""),  # Acknowledgement statement
	"related_projects": [  # A list and bried description of related research projects
		{
			"name": "project related_project name",
			"uri": "http://example.org/project_desc/related_project/uri",
			"note": "project related_project note"
		}
	],
	"geographic_units": [  # List of geographic locations (regions, countries, states, provinces, etc.) describing the geographic coverahe of the research project.
		{
			"name": "World",  # Name of the geographic unit e.g. 'World', 'Africa', 'Afghanistan'
			"code": "geographic_unit code",  # Code of the geographic unit (for countries, preferred = ISO3 code)
			"type": "geographic_unit type"  # Type of geographic unit e.g. country, state, region, province, town, etc
		}
	],
	"keywords": [
		{
			"name": "keyword name",  # Keyword, composed of one or multiple words
			"vocabulary": "keyword vocabulary",  # Vocabulary name (for keywords extracted from controlled vocabularies)
			"uri": "http://example.org/project_desc/keyword/uri"
		}
	],
	"themes": [  # Themes covered by the project (ideally, a controlled vocabulary should be used)
		{
			"name": "theme name",  # Theme label, typically extracted from a pre-defined taxonomy
			"vocabulary": "theme vocabulary",  # Vocabulary name (for themes extracted from controlled vocabularies)
			"uri": "http://example.org/project_desc/theme/uri"
		}
	],
	"topics": [  # Topics covered by the project (ideally, a controlled vocabulary should be used). This can be a hierarchical list of topics.
		{
			"id": "topic id",
			"name": "topic name",
			"parent_id": "topic parent_id",  # For subtopics, provide the ID of the parent topic
			"vocabulary": "topic vocabulary",  # Name of the controlled vocabulary, if the topic is from a taxonomy.
			"uri": "http://example.org/project_desc/topic/uri"  # Link to the controlled vocabulary web page, if the topic is from a taxonomy.
		}
	],
	"disciplines": [
		{
			"name": "Social sciences",  # Disciplines e.g. Social sciences, economics, Natural sciences, biology (ideally, a controlled vocabulary should be used)
			"vocabulary": "disciplines vocabulary",  # Vocabulary name (for disciplines extracted from controlled vocabularies)
			"uri": "http://example.org/project_desc/discipline/uri"
		}
	],
	"repository_uri": [  # Source code repository
		{
			"name": "Github",  # Name of the repository where code is hosted. e.g. Github, Bitbucket, etc.
			"type": "git",  # Repo type e.g. git, svn, other
			"uri": "http://example.org/project_desc/repository_uri/uri"  # URI of the project repository
		}
	],
	"license": [  # Overall statement on license. Note: information on license specific to scripts and/or datasets should be provided in the documentation of scripts and datasets.
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
		
	"""),  # Notes about the technology environment used by the authors to implement the project
	"technology_requirements": inspect.cleandoc("""\
				
		Maecenas sed odio sem. 
		In ut sapien luctus, 
		lacinia est ut, 
		rutrum nunc. 
		Nam dignissim lacus a elit auctor, 
		sed ultricies dui vestibulum. 
		Interdum et malesuada fames ac ante ipsum primis in faucibus. 
		
	"""),  # Software/hardware or other technology requirements needed to replicate the scripts
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
		
	"""),  # Reproduction instructions
	"methods": [  # Methods or algorithms applied
		{
			"name": "method name",
			"note": "method note"
		}
	],
	"software": [  # List of software applications used for the project
		{
			"name": "software name",
			"version": "software version",
			"library": [  # Software-specific libraries or packages used
				"software library"
			]
		}
	],
	"scripts": [  # Description of each script file
		{
			"file_name": "script_file_name.R",
			"zip_package": "script zip_package",  # Provide the name of the zip file, if the file is included in a zip
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
				
			"""),  # Instructions or note for running the script
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
		
	"""),  # Overall statement on data used by the project. More detailed description of the datasets should be provided in the 'datasets' field.
	"datasets": [  # List and description of datasets used by the research project
		{
			"name": "project dataset name",
			"idno": "project dataset idno",  # unique ID of the dataset
			"note": "project dataset note",  # Brief description of the dataset (note: ideally, the dataset will be documented using a specific metadata schema like the DDI).
			"access_type": "project dataset access_type",
			"license": "project dataset license",
			"license_uri": "http://example.org/project_desc/dataset/license_uri",
			"uri": "http://example.org/project_desc/dataset/uri"  # Link to the website where the data may be accessed or more information on access can be found
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
		
	"""),  # Citation requirement (can include a specific recommended citation)
}

response = create_and_import.create_script_dataset(
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
create_and_import.upload_thumbnail(dataset_id, thumbnail_path)