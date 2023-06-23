# Milkstraw Python Client

Python SDK for interacting with Milkstraw APIs.

![formatter](https://github.com/milkstrawai/milkstraw-python-client/workflows/Formatter/badge.svg)

# Installation
To install the latest development version of the SDK:
``` shell
pip install milkstraw-client
```

# Setup
Export the required environment variables:
``` shell
export MILKSTRAW_USER_EMAIL=[YOUR_EMAIL]
export MILKSTRAW_USER_PASS=[YOUR_PASSWORD]
```

# Usage
``` python
from milkstraw_client import GeneratedData, Model, SourceData

# Upload source data
my_source_data = SourceData.upload("my_source_data_name", "data/source_data.csv")

# Create model (After `my_source_data` status becomes `done`)
my_model = Model.create("my_model_name", my_source_data.id)

# Generate data (After `my_model` status becomes `done`)
my_generated_data = GeneratedData.generate(my_model.id, records_num=10000)

# Download generated data (After `my_generated_data` status becomes `done`)
data_file_path = GeneratedData.download(my_generated_data.id, "data/generated_data.csv")

# Download generated data report
report_file_path = GeneratedData.download_report(my_generated_data.id, "data/generated_data_report.zip")
```
