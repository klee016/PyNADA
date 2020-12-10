# PyNADA
A Python client for NADA API

## Setup
This library is currently under development. A pip installation is available through Test PyPI using:
 ```sh
pip install -i https://test.pypi.org/simple/ pynada
 ```

## Examples
Jupyter Notebooks under examples folder show some use cases utilizing PyNADA. The examples are grouped into three categories:
* Search & Browse: codes for finding specific datasets and resources
    - search by partial id, partial title, ...
    - list all datasets
    
* Create & Import: codes for adding datasets to the catalog
    - add survey, document, ... 
    
* Manage & Update: codes for managing existing datasets and resources
    - delete dataset
    - upload thumbnail
    - ...
  

## Bug Report
Some identified bugs in NADA API (5.0.5) are:
* (12/09/2020) Delete file API (/api/datasets/{datasetIDNo}/files/{filename}) deletes the whole dataset that the file belongs to.
* (12/09/2020) Input form error (training.ihsn.org -> site administration -> Studies -> Manage Studies -> Add study)
  IDNO form expects email address instead of Dataset IDNo.
* (12/10/2020) Unable to create a new dataset (PHP error)
