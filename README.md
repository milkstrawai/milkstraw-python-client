# Milkstraw Python Client

Python SDK for interacting with Milkstraw APIs.

![formatter](https://github.com/milkstrawai/milkstraw-python-client/workflows/Formatter/badge.svg)

# Installation
To install the latest development version of the SDK:
``` shell
pip install git+https://github.com/milkstrawai/milkstraw-python-client@main
```

# Setup
Export the required environment variables:
``` shell
export MILKSTRAW_USER_EMAIL=[YOUR_EMAIL]
export MILKSTRAW_USER_PASS=[YOUR_PASSWORD]
```

# Usage
## Source Data
``` python
from milkstraw_client import SourceData

### Upload source data
my_source_data = SourceData.upload("my_source_data_name", "data/source_data.csv")
print(my_source_data)
# SourceData(id='123', name='my_source_data_name', status='pending')

### Get source data
my_source_data = SourceData.get(my_source_data.id)
print(my_source_data)
# SourceData(id='123', name='my_source_data_name', status='pending')

### List all source data
all_source_data = SourceData.list()
for index, data in enumerate(all_source_data):
    print(f"SourceData #{index + 1}: {data}")
# SourceData #1: SourceData(id='123', name='my_source_data_name', status='pending')

### Download source data
data_file_path = SourceData.download(my_source_data.id, "data/source_data_copy.csv")
print(f"Downloaded file path: {data_file_path}")
# Downloaded file path: data/source_data_copy.csv
```

## Models
``` python
from milkstraw_client import Model

### Upload model
my_model = Model.create("my_model_name", "123")
print(my_model)
# Model(id='456', name='my_model_name', status='pending', source_data='123')

### Get model
my_model = Model.get(my_model.id)
print(my_model)
# Model(id='456', name='my_model_name', status='pending', source_data='123')

### List all models
my_models = Model.list()
for index, model in enumerate(my_models):
    print(f"Model #{index + 1}: {model}")
# Model #1: Model(id='456', name='my_model_name', status='pending', source_data='123')
```

## Generated Data
``` python
from milkstraw_client import GeneratedData

### Generate data
my_generated_data = GeneratedData.generate("456", 10000)
print(my_generated_data)
# GeneratedData(id='789', model='456', status='pending')

### Get generated data
my_generated_data = GeneratedData.get(my_generated_data.id)
print(my_generated_data)
# GeneratedData(id='789', model='456', status='pending')

### List all generated data
all_generated_data = GeneratedData.list()
for index, data in enumerate(all_generated_data):
    print(f"GeneratedData #{index + 1}: {data}")
# GeneratedData #1: GeneratedData(id='789', model='456', status='pending')

### Download generated data
data_file_path = GeneratedData.download(my_generated_data.id, "data/generated_data.csv")
print(f"Downloaded data file path: {data_file_path}")
# Downloaded data file path: data/generated_data.csv

### Download generated data report
report_file_path = GeneratedData.download_report(my_generated_data.id, "data/generated_data_report.zip")
print(f"Downloaded report file path: {report_file_path}")
# Downloaded report file path: data/generated_data_report.csv
```
