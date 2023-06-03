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
## Source Datasets
``` python
from milkstraw_client import SourceDataset

### Upload source dataset
my_source_dataset = SourceDataset.upload("dataset_name", "data/source_dataset.csv")
print(my_source_dataset)
# SourceDataset(id='123', name='dataset_name', status='pending')

### Get source dataset
my_source_dataset = SourceDataset.get(my_source_dataset.id)
print(my_source_dataset)
# SourceDataset(id='123', name='dataset_name', status='pending')

### List all source datasets
my_source_datasets = SourceDataset.list()
for index, dataset in enumerate(my_source_datasets):
    print(f"SourceDataset #{index + 1}: {dataset}")
# SourceDataset #1: SourceDataset(id='123', name='dataset_name', status='pending')

### Download source dataset
dataset_file_path = SourceDataset.download(my_source_dataset.id, "data/source_dataset_copy.csv")
print(f"Downloaded file path: {dataset_file_path}")
# Downloaded file path: data/source_dataset_copy.csv
```
