# Milkstraw Python Client

<p align="center">
    <a href="https://milkstraw.ai/"><img width="256px" src="./docs/milkstraw-ai.jpg" alt="Milkstraw AI" /></a><br />
    <i>⚡ Python SDK for interacting with Milkstraw APIs ⚡</i>
</p>

![formatter](https://github.com/milkstrawai/milkstraw-python-client/workflows/Formatter/badge.svg)

## Table of Contents
- [Quick Install](#quick-install)
- [What is this?](#what-is-this)
- [What can this help with?](#what-can-this-help-with)
- [Usage](#usage)

## Quick Install
Using python 3.9 or above, install the library with pip:
``` shell
pip install milkstraw-client
```

## 🤔 What is this?
Artificial intelligence is emerging as a transformative technology, enabling developers to build applications that they previously could not. However, building these AIs without sufficient data is often a problem for creating a truly powerful AI - the real power comes when you can combine amazing data + awesome model. You can't have one without the other.

This library aims to assist in generating datasets that are clean, unbiased, and rich!

## 🚀 What can this help with?
There are six main areas that MilkStraw generative data is designed to help with:

### 📚 Data Augmentation:
Data Augmentation has one specific job: making your data richer. Examples include uploading a small dataset and turning it into a big rich dataset.

### 📃 Balancing data:
This includes taking a biased dataset and asking the Milkstraw AI to generate a new dataset where the bias is lowered. Examples include mitigating demographic biases by generating a more evenly distributed representation of various groups. This can help in developing more fair and unbiased AI models.

### 🔐 Anonymize:
Take an unusable dataset and turn it into an anonymized one that can be used and shared with others. Safeguard personal and confidential data while maintaining its utility and usability.

### 🤖 Scenario simulation:
"What if this happened?" Take a dataset and ask Milkstraw AI to create certain scenarios that can happen. Enhance the quality and diversity of your training data, empowering your models to achieve higher accuracy, robustness, and generalization capabilities.

### 🧠 Generate On Demand:
If more data is needed for model training or validation, it can be produced quickly without additional costs or privacy concerns associated with data collection. This means that AI projects can move at a faster pace and at a lower cost.

### 🧐 Evaluation:
Get instant insights into data accuracy, completeness, and consistency. Benefits of this include addressing data quality issues promptly to minimize impact and gaining insights into data accuracy, consistency, and reliability.


## Usage
If you don't already have an account, please create one on the [Milkstraw Sign Up](https://signup.milkstraw.ai/) page.

To generate a dataset of 10K elements from a given dataset, run the following code:
``` python
import milkstraw_client
from milkstraw_client import GeneratedData, Model, SourceData

# Setup credentials
milkstraw_client.user_email = "[YOUR_EMAIL]"
milkstraw_client.user_password = "[YOUR_PASSWORD]"

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
Instead, you can setup credentials from environment variables:
``` shell
export MILKSTRAW_USER_EMAIL="[YOUR_EMAIL]"
export MILKSTRAW_USER_PASS="[YOUR_PASSWORD]"
```
