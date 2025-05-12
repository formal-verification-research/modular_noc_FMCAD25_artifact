# Artifact for Probabilistic Verification for Modular Network-on-Chip Systems

Authors: Nick Waddoups, Jonah Boe, Arnd Hartmanns, Prabal Basu, Sanghamitra Roy, Koushik Chakraborty,
Zhen Zhang

This is the artifact for the Probabilistic Verification for Modular Network-on-Chip Systems
paper submitted to FMCAD 25.

## Prerequisites for Running the Modular NoC model

The following software must be installed to run the modular NoC model or generate new model
templates using the Python library.

- [Modest Toolset](https://www.modestchecker.net/) Version 3.1.290 or greater.
- Python 3.10 or greater.

Additionally, you can use the provided Docker image which has both the Modest Toolset and
Python installed. For verification of larger NoCs, using a local installation of Modest
is recommended as the model checking is a CPU and RAM intensive process.

## Setting up the Docker Container

This artifact has a Docker image that contains the build of the Modest Toolset used in the
paper.

To build the docker image you first need to download Version 3.1.290 of the Modest Toolset
from [modestchecker.net](https://www.modestchecker.net/Downloads/) and place the zip file 
in this directory.

Build the Docker image using the following command.

```sh
docker build -t modular_noc .
```

Then start the docker image using the following command.

```sh
docker run -it modular_noc
```

## Files in this Artifact

This artifact contains the modular 2x2 model used to verify functional correctness of the
modular NoC design and the results from the verification in the [models/](./models/)
directory.

Additionally, two python scripts are provided for generating arbitrarily-sized NoC models
and for running the `modest` tool from Python in the [python/](./python/) directory. 
