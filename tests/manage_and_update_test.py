from pynada import manage_and_update

manage_and_update.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = open("API Key.txt", "r").read()
manage_and_update.set_api_key(api_key)

# idno = "WPS8038"
# manage_catalog.delete_dataset(idno)

#print(manage_and_update.update_survey('ALB_2000_MICS_V01_M'))

#manage_and_update.delete_dataset('string')

#manage_and_update.upload_file('study_id', 'WBG-logo.jpg')

#manage_and_update.delete_file('study_id', 'WBG-logo.jpg')

#manage_and_update.upload_file('SCRIPT_DATASET_SAMPLE_01', 'predicting_food_crises.R')

# manage_and_update.add_resource(
# 	dataset_id="SCRIPT_DATASET_SAMPLE_01",
# 	dctype="Document [doc/oth]",
# 	title="predicting_food_crises",
# 	filename="predicting_food_crises.R",
# 	overwrite="yes"
# )
