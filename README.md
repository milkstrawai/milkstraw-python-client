# Milkstraw Python Client

Python SDK for interacting with Milkstraw APIs.

![formatter](https://github.com/milkstrawai/milkstraw-python-client/workflows/Formatter/badge.svg)

# Installation
To install the latest development version of the SDK:
``` shell
pip install git+ssh://git@github.com/milkstrawai/milkstraw-python-client@main
```

# Setup
Export the required environment variables:
``` shell
export MILKSTRAW_EDGE_SERVICE_URL="http://localhost/api/v1"
export MILKSTRAW_USER_EMAIL=[YOUR_EMAIL]
export MILKSTRAW_USER_PASS=[YOUR_PASSWORD]
```

# Usage
## Add Generator
``` shell
$ python
>>> import milkstraw_client
>>> milkstraw_client.Generator.add("my_generator", 100, "path_to_data_folder/my_dataset.csv")
Generator(id='646886dec71f830027c65889', name='my_generator', status='pending')
```

## List Generators
``` shell
$ python
>>> import milkstraw_client
>>> milkstraw_client.Generator.list()
[Generator(id='646886dec71f830027c65889', name='my_generator', status='pending')]
```

## Get Generator
``` shell
$ python
>>> import milkstraw_client
>>> milkstraw_client.Generator.get("646886dec71f830027c65889")
Generator(id='646886dec71f830027c65889', name='my_generator', status='done')
```

## Download Generator
``` shell
$ python
>>> import milkstraw_client
>>> milkstraw_client.Generator.download("64686be9419ba3003fb17045", "data/generated_dataset.csv")
"data/generated_data.csv"
```
