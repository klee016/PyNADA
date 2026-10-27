# PyNADA
A Python client for NADA API

## Setup
You can installl PyNADA using pip:
 ```sh
pip install -U pynada
 ```

## Examples
Jupyter Notebooks under examples folder show some use cases utilizing PyNADA. The examples are grouped into three categories:
* Search & Browse: codes for finding specific datasets and resources

    
* Create & Import: codes for adding datasets to the catalog

    
* Manage & Update: codes for managing existing datasets and resources

Indicator studies, codelists, data structures, and observations are under `nada.indicators`. Large CSV files go through `nada.uploads`.

```python
import pynada as nada

nada.set_api_url("https://example.org/index.php/api/")
nada.set_api_key("your-api-key")

nada.indicators.create("POP_SEX", series_description={"idno": "POP_SEX", "name": "Population by sex"})
nada.indicators.codelists.import_json({"idno": "NADA_SEX_1.0", "name": "SEX", "items": [{"code": "F", "label": "Female"}]})
nada.indicators.data.import_csv("POP_SEX", csv_path="observations.csv", dsd_idno="AGENCY.POP.1.0")
nada.indicators.catalog.query("POP_SEX", time_from=2010, time_to=2020)
```

`create_timeseries_dataset` and `create_timeseries_database` remain available.

  


