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
- 16 GB RAM or greater.

Additionally, you can use the provided Docker image which, once set up, will have both the
Modest Toolset and Python installed. For verification of larger NoCs, using a local
installation of Modest is recommended as the model checking is a CPU and RAM intensive
process.

## Setting up the Docker Container

This artifact has a Docker image that contains the build of the Modest Toolset used in the
paper.

### Obtaining Modest for the Docker Container

To build the docker image you first need to download the x86-64 Version 3.1.290 of the Modest
Toolset from [modestchecker.net](https://www.modestchecker.net/Downloads/) and place the zip
file in this directory. Due to the licensing agreements of Modest we cannot include it in the
Docker image.

After downloading the Modest Toolset your directory should contain the following entries:

```sh
$ ls
Dockerfile    models/    Modest-Toolset-v3.1.290-gff8cae090-linux-x64.zip    python/    README.md
```

### Installing Docker Desktop

Next, you need to ensure Docker is installed. Follow the instructions located at
[docs.docker.com](https://docs.docker.com/desktop/) to install the desktop version of
Docker for you specific operating system. Once enstalled, make sure to start Docker
Desktop in order for the following commands to work correctly.

### Building the Docker Image

Move your shell into this directory (the one containing the [Dockerfile](Dockerfile)) and then
run the following command to build the Docker image.

```sh
docker build -t modular_noc .
```

Then start the docker image using the following command.

```sh
docker run -it modular_noc
```

You should now be in the docker environment. You can check that Modest and Python are correctly
installed by running the following commands.

```sh
modest --version 
python3 --version
```

## Installing Modest on a Local Machine

Go to [modestchecker.net](https://www.modestchecker.net/Downloads/) and read and
agree to the license terms. Then, download the zipped executable for your specific
operating system. Options are available for Linux, Mac, and Windows.

Unzip the Modest executable and add it to your path. You can test that you have
correctly added the tool to the path by going to a shell of your choice and
running the following command.

```sh
modest --version
```

The output should match the following:

```text
The Modest Toolset (www.modestchecker.net), version v3.1.290-gff8cae090+ff8cae0903ec136f9c4c15123e444b0b0399ff6b.
Command: modest --version
Usage:    modest <tool> <parameters>
Tools: benchmark         (mobench)
       check             (mcsta)
       check-symblicit   (mcsta-symblicit)
       convert           (moconv)
       export-to-dot     (mosta)
       export-to-python  (mopy)
       initialize        (init)
       plan              (modysh)
       plot              (moplot)
       prohver           (prohver)
       simulate          (modes)
```

## Files in this Artifact

This artifact contains the modular 2x2 model used to verify functional correctness of the
modular NoC design and the results from the verification in the [models/](./models/)
directory.

Additionally, two python scripts are provided for generating arbitrarily-sized NoC models
and for running the `modest` tool from Python in the [python/](./python/) directory.

## Replicating Results From the Paper

### 2x2 Correctness

To verify 2x2 correctness run the following command from this directory to produce the
correctness guarantees from Modest. This should take approximately 10 minutes and use
10 GB of memory.

```sh
modest check models/functional_2x2.modest --unsafe --chainopt
```

### PSN Characterization

To generate the PSN characterization results for basic 2x2, 3x3, and 4x4 setups (Figures 2-5
of the paper) run the following from this directory. This should take approximately 1.75 hrs,
and should use only a small amount of memory as it is simulating the model, not exploring the
statespace.

```sh
python3 python/fmcad.py
```

### Interpreting the Results

The output of running modest on the 2x2 correctness model demonstrate that all properties hold
for the model. Each property listed in the output represents a CTL property in the model, and
is either marked `True` if the property held or `False` if it did not hold. You can see the CTL
properties in Section V. of our paper or on lines 227-361 of
[functional_2x2.modest](models/functional_2x2.modest).

The output of the PSN characterization is stored in the result/ directory. This directory has
subdirectories for 2x2, 3x3, and 4x4. Inside of each of these directories is a list of .csv
and .txt files containing the results of each simulation run. The files are of the following
naming convention:

```text
noc_<size>_<type>_<threshold>_<clk cycle stride>_<cycles per analysis>
```

For example, simulation results (e.g. CDF of PSN probability vs. clk cycles) for inductive noise
with a `INDUCTIVE_THRESHOLD` of 1, a clock cycle stride of 6, and 300 cycles per analysis would
be named as follows:

```text
noc_2x2_inductive_noise_threshold_1_stride_6_block_size_300
```

The files ending in .csv are the raw data from `modest simulate` formatted in a csv file, and the
files ending in .time.txt contain the simulation specification and time that it took to complete
the simulation.
