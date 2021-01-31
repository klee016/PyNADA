import pynada as nada

nada.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = open("API Key.txt", "r").read()
nada.set_api_key(api_key)

# idno = "WPS8038"
# nada.delete_dataset(idno)

#print(nada.update_survey('ALB_2000_MICS_V01_M'))

#nada.delete_dataset('string')

#nada.upload_file('study_id', 'WBG-logo.jpg')

#nada.delete_file('study_id', 'WBG-logo.jpg')

#nada.upload_file('SCRIPT_DATASET_SAMPLE_01', 'predicting_food_crises.R')

nada.add_resource(
	dataset_id="SCRIPT_DATASET_SAMPLE_01",
	dctype="Document [doc/oth]",
	title="predicting_food_crises",
	filename="predicting_food_crises.R",
	overwrite="yes"
)