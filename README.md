# README #

*praudio* provides objects and a script for performing complex 
preprocessing operations on entire audio datasets with one command.

*praudio* is implemented having Deep Learning audio/music applications in mind.

Operations are carried out on CPU. Preprocessing can also be run on-the-fly,
for example, while training a model.

The library uses `librosa` as an audio processing backend.


### How do I install the library? ###

You can install *praudio* both with `pip` via PyPi, and by cloning the 
*praudio* repo from GitHub. 

For both approaches, it's advisable to use a dedicated Python virtual 
environment.

#### Installing from PyPi ####

Installing from PyPi is the easiest option. In the terminal type:

```shell
$ pip install praudio
```

#### Installing from GitHub ####

First, you should clone the repository from GitHub:

```shell
$ git clone git@github.com:musikalkemist/praudio.git
```

Then, move to the project root and, to install the package, type in the terminal:
```shell
$ pip install .
```

You can also use a rule in the available Makefile (see below):
```shell
$ make install 
```

To install the package in development mode use:
```shell
$ pip install -e .[testing]
```

You can also use a rule in Makefile:
```shell
$ make install_dev 
```

This will install all the packages necessary to run the tests, lint, 
type checker. It will also install the package in 'editable' mode, which is 
ideal for development.

### Python version ###
*praudio* works in Python 3.6, 3.7, 3.8.


### How do I preprocess an audio dataset? ###
The core of the library is the *preprocess* entry point. This script works 
with a config file. You set the type of preprocessing you want to apply in a 
yaml file, and then run the script. Your dataset will be entirely 
preprocessed and the results recursively stored in a directory of your 
choice that can potentially be created from scratch.

To run the entry point, ensure the library is installed and then type:
```shell
$ preprocess /path/to/config.yml
```

In the config.yml, you should provide the following parameters:
- `dataset_dir`: Path to the directory where your audio dataset is stored
- `save_dir`: Path where to save the preprocessed audio.
- Under `file_preprocessor`, you should provide settings for `loader` and `transforms_chain`.
- `loader`: Provide settings for the loader.
- `transforms_chain`: Parameters for each transform in the sequence. 
  of transforms which are applied to your data (i.e., TransformChain).

These config parameters are used to dinamically initialise the relative 
objects in the library. To learn what parameters are available at each 
level in the config file, please refer to the docstrings in the relative 
objects.

Check out `test/config.sampleconfig.yml` to see an example of a valid config 
file.


### Package structure ###
The package is divided into a number of subpackages:
- config
- creation
- io
- preprocessors
- transforms

`config` has facilities to load, save, and validate configuration files, 
which are used to specify the types of preprocessing pipelines to use.

`creation` has classes that are responsible to instantiate key objects in 
the library.

`io` contains facilities to load / save audio signals from / to files.

`preprocessors` features objects which are responsible to preprocess single 
audio files, from loading to storing, as well as, batch of files.

`transforms` contains a series of objects which manipulate audio signals, 
such as short-time Fourier transform, log, scaling.


### What's the Makefile for? ###

The Makefile has a series of rules that can be used to ensure quality of 
the code, and automate repetitive tasks.

#### Linter ####
The project uses `pylint`. The linter helps enforcing a coding 
standard, sniffs for code smells and offers simple refactoring suggestions.

To run the linter type:
```shell
$ make lint
```

#### Typehint ####
The project uses `mypy`. `mypy` is an optional static type checker for 
Python. You can add type hints (PEP 484) to your Python programs, 
and use mypy to type check them statically. 

To run the type checker type:
```shell
$ make typehint
```

#### Testing ####
The project uses `pytest` for unittests. Tests can be run in one go using 
`coverage`. This package suggests the percentage of code that is covered in 
unittests.

To run all the unittests type:
```shell
$ make test
```

#### Checklist ####
Checklist is a utility rule that runs the linter, type checker, and the 
test suite in one go:

```shell
$ make checklist
```

#### Clean ####
Use the clean rule to get rid of `pyc` files and `__pychache__`:
```shell
$ make clean
```

### Dependencies ###
*praudio* has the following dependencies:
- librosa==0.8.1
- pyyaml==5.4.1
- types-PyYAML==5.4.6

`librosa` is extensively used to extract audio features in transform objects. 


### Current limitations ###
The *praudio* preprocessors are capable of operating only on mono signals. 
This is a significant limitation if you are working in generative music. 
If you are using the library for audio / music analysis, this shouldn't 
be a problem.


### Future improvements ###
- Add audio augmentation / padding / cropping transforms. 
- Enable preprocessing of signals with multiple channels.
- Turn transform parameters into full-fledged objects (e.g., STFTParams)
- Instead of using a dictionary for configurations, instantiate parameter 
  objects with validation
- Implement different types of Savers / Loaders with factories to produce 
  them.








