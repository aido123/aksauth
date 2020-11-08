# AZ AKS Auth Azure az cli extension

![version-image][version-image]

Authenticate NON Interactively to AKS Clusters

## Sample

az aksauth connect --resource-group adrian-group --subscription xxxxxx–1ef5–4ba4-bdd0–xxxxxx --cluster-name adrian-cluster --tenant zzzzzz–6cd9–4672–9034-zzzz --username clusteruser@mydmn.com --password "hard2Guess"

## Installation

### Prerequisites
* Python3
* PIP3
* Az Cli

### Running Instructions

1. Create Python Wheel

```
python setup.py bdist_wheel
```

2. Add as an extension to Azure's AZ CLI

```
az extension add --source C:\Users\Adrian\aksauth\dist\aksauth-0.0.1-py2.py3-none-any.whl
```


### Parameters

*tenant* - tenant id

*subscription* - subscription id

*resource-group* - resource group name

*cluster-name* - cluster name

*username* - tenant username

*password* - password


[version-image]: https://img.shields.io/badge/version-0.0.1-green.svg?style=plastic