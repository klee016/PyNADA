from pynada import create_and_import
import inspect

create_and_import.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
create_and_import.set_api_key(api_key)

##########################
# add_script_dataset test
##########################
idno = "RR_WLD_2020_PFC_v01"

repositoryid = "central"
published = 1
overwrite = "yes"
doc_desc = None
project_desc = {
	"title_statement": {
		"idno": "RR_WLD_2020_PFC_v01",
		"title": "Reproducible code for the World Bank Policy Research Working Paper No 9142 - Predicting Food Crises"
	},
	"abstract": inspect.cleandoc("""\
		
		This package contains code and data for a statistical forecasting approach to predict the outbreak of food crises.
		
	"""),
	"output": [
		{
			"type": "Working paper",
			"title": "Predicting Food Crises",
			"authors": "Bo Pieter Johannes Andrée, Andres Chamorro, Aart Kraay, Phoebe Spencer, Dieter Wang",
			"description": inspect.cleandoc("""\
				
				World Bank Policy Research Working Paper No 9412.
				This paper is a product of the Fragility, Conflict and Violence Global Theme and the Development Economics Vice Presidency. It is part of a larger effort by the World Bank to provide open access to its research and make a contribution to development policy discussions around the world.
				
			"""),
			"abstract": inspect.cleandoc("""\
				
				Globally, more than 130 million people are estimated to be in food crisis. These humanitarian disasters are associated with severe impacts on livelihoods that can reverse years of development gains. 
				The existing outlooks of crisis-affected populations rely on expert assessment of evidence and are limited in their temporal frequency and ability to look beyond several months.
				This paper presents a statistical forecasting approach to predict the outbreak of food crises with sufficient lead time for preventive action. 
				Different use cases are explored related to possible alternative targeting policies and the levels at which finance is typically unlocked. 
				The results indicate that, particularly at longer forecasting horizons, the statistical predictions compare favorably to expert-based outlooks. 
				The paper concludes that statistical models demonstrate good ability to detect future outbreaks of food crises and that using statistical forecasting approaches may help increase lead time for action.
				
			"""),
			"uri": "http://hdl.handle.net/10986/34510"
		}
	],
	"language": [
		{
			"name": "English",
			"code": "EN"
		}
	],
	"production_date": [
		"2020-10-07"
	],
	"version_statement": {
		"version": "1.0",
		"version_date": "September 2020"
	},
	"authoring_entity": [
		{
			"name": "Bo Pieter Johannes Andree",
			"affiliation": "World Bank",
		}
	],
	"acknowledgement_statement": inspect.cleandoc("""\
		
		This work was prepared as background for the Famine Action Mechanism (FAM). 
		The authors would like to thank Nadia Piffaretti, Zacharey Carmichael, Harun Dogo, Arif Hussain, Luca Russo, Jose Lopez, Colin Bruce, Nick Haan, Frank Davenport, Dan Maxwell, Joanna Macrae, Soomin Park, Marco Zambotti, Sardar Azari, Therese Norman-Monroe, Jacob LaRiviere, and the IPC, WFP mVAM, and FAO teams for invaluable contributions in the initial phase of this work. 
		In particular, we'd like to thank the participants of the FAM Workshop in Geneva on February 2018 hosted by ICRC, Artemis Working Days in Rome on April 2018 hosted by WFP, the FAM Data and Analytics meetings with global tech partners in Rome and New York on September 2018, and the participants to the Predictive Analytics workshop hosted by UN OCHA, at the Center for Humanitarian data in the Hague in April 2019.
		
	"""),
	"geographic_units": [
		{"name": "Afghanistan", "code": "AFG", "type": "Country"},
		{"name": "Burkina Faso", "code": "BFA", "type": "Country"},
		{"name": "Chad", "code": "TCD", "type": "Country"},
		{"name": "Congo, Dem. Rep.", "code": "COD", "type": "Country"},
		{"name": "Ethiopia", "code": "ETH", "type": "Country"},
		{"name": "Guatemala", "code": "GTM", "type": "Country"},
		{"name": "Haiti", "code": "HTI", "type": "Country"},
		{"name": "Kenya", "code": "KEN", "type": "Country"},
		{"name": "Malawi", "code": "MWI", "type": "Country"},
		{"name": "Mali", "code": "MLI", "type": "Country"},
		{"name": "Mauritania", "code": "MRT", "type": "Country"},
		{"name": "Mozambique", "code": "MOZ", "type": "Country"},
		{"name": "Niger", "code": "NER", "type": "Country"},
		{"name": "Nigeria", "code": "NGA", "type": "Country"},
		{"name": "Somalia", "code": "SOM", "type": "Country"},
		{"name": "South Sudan", "code": "SSD", "type": "Country"},
		{"name": "Sudan", "code": "SDN", "type": "Country"},
		{"name": "Uganda", "code": "UGA", "type": "Country"},
		{"name": "Yemen, Rep.", "code": "YEM", "type": "Country"},
		{"name": "Zambia", "code": "ZMB", "type": "Country"},
		{"name": "Zimbabwe", "code": "ZWE", "type": "Country"}
	],
	"keywords": [
		{"name": "crisis"},
		{"name": "malnutrition"},
		{"name": "food price"},
		{"name": "food security"},
		{"name": "food insecurity"},
		{"name": "extreme events"},
		{"name": "unbalanced data"},
		{"name": "costsensitive learning"},
		{"name": "cost-sensitive learning"},
		{"name": "fragility"},
		{"name": "famine"},
		{"name": "famine action mechanism FAM"}
	],
	"topics": [
		{
			"id": "C01",
			"name": "Econometrics",
			"vocabulary": "Journal of Economic Literature (JEL)",
			"uri": "https://www.aeaweb.org/econlit/jelCodes.php"
		},
		{
			"id": "C14",
			"name": "Semiparametric and Nonparametric Methods: General",
			"vocabulary": "Journal of Economic Literature (JEL)",
			"uri": "https://www.aeaweb.org/econlit/jelCodes.php"
		},
		{
			"id": "C25",
			"name": "Discrete Regression and Qualitative Choice Models - Discrete Regressors - Proportions - Probabilities",
			"vocabulary": "Journal of Economic Literature (JEL)",
			"uri": "https://www.aeaweb.org/econlit/jelCodes.php"
		},
		{
			"id": "C53",
			"name": "Forecasting and Prediction Methods - Simulation Methods",
			"vocabulary": "Journal of Economic Literature (JEL)",
			"uri": "https://www.aeaweb.org/econlit/jelCodes.php"
		},
		{
			"id": "O10",
			"name": "Economic Development - General",
			"vocabulary": "Journal of Economic Literature (JEL)",
			"uri": "https://www.aeaweb.org/econlit/jelCodes.php"
		}
	],
	"license": [
		{
			"name": "CCA 4.0",
			"uri": "https://creativecommons.org/licenses/by/4.0"
		}
	],
	"technology_requirements": inspect.cleandoc("""\
		
		- The code was developed and last ran in Microsoft Open R 3.5.1, on Ubuntu 16.04.5 LTS and has not been tested on other OS. It should run in R 3.5.1 but the code benefits from multithreaded BLAS/LAPACK and contains a call to automatically sets MKL threads. This may throw an error in R 3.5.1 but should not break the remainder of the code.
		- The results presented in the paper have been generated on a virtual machine with 64 CPUs and 256GB RAM. Producing the full set of results in the paper consumed around 12,000 core hours and was run on a D64s_v3 VM with 64CPUs and 256 GiB RAM. Some simplifications have been made to make the final code more usable, comments are left in the main R file.
		- Viewing plots: R Studio server is recommended.
		
	"""),
	"reproduction_instructions": inspect.cleandoc("""\
		
		>> INSTALLATION
		
		The user will need to follow standard installation instructions for R. 
		* To avoid unexpected issues, it is recommended to run this code on a similar R installation and OS, i.e. Microsoft Open R 3.5.1. on Ubuntu 16.04.5 and r-studio-server 1.2.5001.
		
		Install the required R packages (lines 5 - 34 in predicting_food_crises_dependencies.R). 
		* Note that many R packages require the user to install dependencies on ubuntu OS itself.
		* User will need to install packages manually, since currently, there is no good way to automatize this. This is due to the large number of (in)direct dependencies in and outside R.
		- At the end of this readme file, a print out of sessionInfo() is provided such that versions of all packages can be viewed.
		* Note that the main R code (predicting_food_crises.R) sources the dependencies, the balanced learners, and reads the data. 
		- The user needs to specify the folder that contains these files in line 8. The default value is:'/home/predicting _food_crisis_package/' which assumes this package is unzipped in the home folder of ubuntu.
		
		The code can be run in a terminal, in which case the data plots will not be visible to the user.
		* One solution is to run the code on R Studio server. When set up correctly, one can access the RStudio IDE from anywhere via a web browser and use plot functionality. The code was developed on r-studio-server 1.2.5001. This can be isntalled by following standard installation procedures.
		
		>> CONFIGURATION
		
		There are a number of choices that the user can make to control the behavior of the main program:
		
		* Lines 15-26 are options to control the definition of the dependent variable and the treatment of independent variables. 
		The default settings runs a model on all countries, using ipc 3 and above as positive class, uses only exogenous covariates as predictors, adds synthetic cases to the training data, calculates additional features, and restricts linear correlation to .75. These are the settings that correspond to the paper.
		* Lines 31-32 control the type of learner used, default settings correspond to a simplified RF algorithm that delivers good results (nearly identical to the paper) but runs much faster.
		See also the comments in the code.
		* Lines 35-37 control an imputation strategy in case a missing value is encountered, settings should not matter when the supplied data is used.
		* Lines 40-43 control the cross-validation, note that repetitions have been reduced to make the runtime and RAM requirements more manageable.
		* Lines 46-55 control the compute environment.
		
		Default settings:
		* Note that parallel processing works differently on ubuntu than on other OS, but generally it involves generating copies of dependencies or compute environments and so memory requirements can be extremely high even when the initial data set seems manageable. For this reason the following simplifications have been made to default seetings:  
		- The number of validation samples has been reduced from 50 to 10.
		- The tuning parameters of the default RF model have been fixed at recommended values. To run full tuning or use one of the alternative balanced classifiers, change MODEL_METHOD to one of the classifiers from predicting_food_crises_balanced_learners.R
		- When an alterantive model is used, the length of the tuning grid has been reduced to 5, the paper uses 10.
		* These settings produce similar results as those presented in the main paper, but the runtime and RAM requirements have been drastically reduced (depending of course on the number of CPUs available). 
		- The final code at (recommended) default settings was last run on a D32s_v3 VM with 32CPUs and 128 GiB RAM, reaching 100% CPU utilization and approx 60% RAM utilization, and took just below 2.5 hours to complete.
		- By default, the code runs on the entire data set that is provided. Note that the paper only trains and cross-validates on data up to February 2019. With the current settings, it is thus straightforward to update the data set and make real forecasts.
		
		>> EXECUTION
		
		Running code:
		* After installation, simply unpack the folder, point the code (line 8) to the correct folder and run predicting_food_crises.R.
		* The code is currently not set up to write results to disk. As always, complex R objects can be saved for re-use using saveRDS() and text can be written using write.csv().
		
		>> TROUBLESHOOTING
		
		Dependencies:
		* Make sure all OS dependencies are installed such that all libraries can be installed. Then make sure that all R libraries are installed and that also their dependencies are installed.
		* See the sessionInfo() readout at the end of this file. 
		* Make sure the predicting_food_crises_dependencies.R and predicting_food_crises_balanced_learners.R files are correctly sourced.
		
		Unexpected crash with different compute settings:
		* If a different VM is used or if changes are made to the settings and the program crashes halfway, then keep an eye on the RAM usage. On ubuntu this can be monitored using > htop
		If RAM usage is too high, reduce the number of cores used in lines 46-55.
		
		NA values in validation metrics:
		* A common issue with caret is that validation metrics return as NA. This is likely result of a missing dependency in the slave environment, which may occur because different OS handle parallelization differently. See if the issue persists when setting MODEL_METHOD to another value, for example 'multinom'.
		
	"""),
	"methods": [
		{"name": "inverse distance interpolation", "note": ""},
		{"name": "outliers smoothing", "note": ""},
		{"name": "seasonal decomposition", "note": ""},
		{"name": "moving average", "note": ""},
		{"name": "k-neighbors", "note": ""},
		{"name": "K-fold cross validation", "note": ""},
		{"name": "random forest", "note": ""},
		{"name": "confusion matrix", "note": ""},
		{"name": "pseudo-out-of-sample", "note": ""},
		{"name": "temporal holdout validation", "note": ""},
		{"name": "logistic regression with Lasso penalty", "note": ""},
		{"name": "multi-layer perceptron neural network", "note": ""},
		{"name": "forecast decomposition", "note": ""}
	],
	"software": [
		{
			"name": "R",
			"version": "Version 3.5.1 (2018-07-02)",
			"library": [
				"TTR", "forecast", "timeSeries", "KRLS", "zoo", "spdep", "pROC", "MASS", "mice", "phylin", "imputeTS",
				"plyr", "dplyr", "gplots", "parallel", "foreach", "caret", "doSNOW", "doParallel", "doFuture", "downloader",
				"CDM", "miceadds", "janitor", "psych", "xts", "fpp", "Ecdat", "DescTools", "devtools"
			]
		}
	],
	"scripts": [
		{
			"file_name": "readme.txt",
			"title": "Readme file",
			"authors": [{"name": "Bo P.J. Andree", "abbr": "", "role": ""}],
			"date": "2020-09",
			"format": "txt (ASCII)",
			"description": "Readme file on Introduction, Requirements, Installation, Configuration, Execution, Troubleshooting, Maintainers, sessionInfo"
		},
		{
			"file_name": "predicting_food_crises.R",
			"title": "Predicting food crises (main code)",
			"authors": [{"name": "Bo P.J. Andree"}],
			"date": "2020-09",
			"format": "R script",
			"software": "R version 3.5.1 (2018-07-02)",
			"description": "The main R code used to produce to process data, train and cross-validate models for 1 to 12 month ahead forecasts and generate useful plots and results"
		},
		{
			"file_name": "predicting_food_crises_dependencies.R",
			"title": "Predicting food crises (dependencies)",
			"authors": [{"name": "Bo P.J. Andree"}],
			"date": "2020-09",
			"format": "R script",
			"software": "R version 3.5.1 (2018-07-02)",
			"description": "Dependencies required to run the main R code contained in predicting_food_crises.R"
		},
		{
			"file_name": "predicting_food_crises_balanced_learners.R",
			"title": "Predicting food crises (balanced learners)",
			"authors": [{"name": "Bo P.J. Andree"}],
			"date": "2020-09",
			"format": "R script",
			"software": "R version 3.5.1 (2018-07-02)",
			"description": "Popular classifiers with cross-validated probability balancing as described in the paper",
			"instructions": "The code can be run"
		}
	],
	"datasets": [
		{
			"name": "predicting_food_crises_data.csv",
			"idno": "WLD_2020_PFC_v01_M",
			"note": "Data set used to produce results of the paper",
			"access_type": "Open",
			"uri": "http://fcv.ihsn.org//catalog/1325"
		}
	],
	"contacts": [
		{"name": "Bo P.J. Andree", "affiliation": "World Bank", "uri": "bandree@worldbank.org",
		 "role": "For technical questions on the paper and code"},
		{"name": "Andres Chamorro", "affiliation": "World Bank", "uri": "achamorroelizond@worldbank.org",
		 "role": "For data-related questions"},
		{"name": "Nadia Piffaretti", "affiliation": "World Bank", "uri": "npiffaretti@worldbank.org",
		 "role": "For other questions"}
	],
	"tags": [
		{
			"tag": "project tag"
		}
	],
	"disclaimer": "These results and the related working paper reflect the views of the authors, and do not reflect the official views of the World Bank, its Executive Directors, or the countries they represent.",
	"confidentiality": "The published materials do not contain any confidential information.",
	"citation_requirement": "The citation of this work is Andree, Bo Pieter Johannes; Chamorro, Andres; Kraay, Aart; Spencer, Phoebe; Wang, Dieter. 2020. Predicting Food Crises. Policy Research Working Paper; No. 9412. World Bank, Washington, DC."
}

response = create_and_import.add_script_dataset(
	idno=idno,
	repositoryid=repositoryid,
	published=published,
	overwrite=overwrite,
	#doc_desc=doc_desc,
	project_desc=project_desc
)

print(response)
