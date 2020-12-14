from pynada import manage_and_update

manage_and_update.set_api_url('http://training.ihsn.org/index.php/api/')
api_key = 'cf16a23a3cfc6a928f63dd3c8daf8796'
manage_and_update.set_api_key(api_key)

# idno = "WPS8038"
# manage_catalog.delete_dataset(idno)

#print(manage_and_update.update_survey('ALB_2000_MICS_V01_M'))

#manage_and_update.delete_dataset('survey-add-test-01')

#manage_and_update.upload_file('study_id', 'WBG-logo.jpg')

#manage_and_update.delete_file('study_id', 'WBG-logo.jpg')