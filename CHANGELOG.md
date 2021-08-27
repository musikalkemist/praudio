# CHANGELOG
This file provides a history of the changes in the repo.

# [0.1.0] - 27.08.21 - Valerio Velardo
- Implemented deployment to PyPi in GitHub workflow
- Outlined how to install praudio via GitHub and PyPi in README

# [0.0.26] - 27.08.21 - Valerio Velardo
- Implemented deployment to TestPyPi conditional to tagging

# [0.0.25] - 27.08.21 - Valerio Velardo
- Implemented build-n-deploy job in Github actions to build distribution and
upload it on Test PyPi
- Added README.md as long_description in setup.py
- Fixed numpy to version 1.20.3 in requirements.txt

# [0.0.21] - 27.08.21 - Valerio Velardo
- Compiled README file

# [0.0.20] - 27.08.21 - Valerio Velardo
- Implemented ConfigSaver with unittests
- Storing configurations in preprocess entry point

# [0.0.19] - 26.08.21 - Valerio Velardo
- Implemented preprocess endpoint
- Implemented creation function for ConfigLoader
- Implemented creation function for BatchFilePreprocessorCreator
- Implemented unittests

# [0.0.18] - 26.08.21 - Valerio Velardo
- Fixed bug in test_configvalidator. Now we remove the temporary dir hierarchy
at the end of unittest

# [0.0.17] - 26.08.21 - Valerio Velardo
- Implemented configuration loading and validation
- Implemented unittests for ConfigLoader and ConfigValidator

# [0.0.16] - 26.08.21 - Valerio Velardo
- Implemented FilePreprocessorCreator
- Implemented BatchFilePreprocessorCreator
- Implemented relative unittests

# [0.0.15] - 25.08.21 - Valerio Velardo
- Implemented TransformationsChainCreator with unittests

# [0.0.14] - 25.08.21 - Valerio Velardo
- Implemented TransformationFactory with unittests

# [0.0.13] - 25.08.21 - Valerio Velardo
- Removed dummy.wav file at root of test directory. Using file in dummydataset
folder instead for tests.

# [0.0.12] - 25.08.21 - Valerio Velardo
- Implemented FilePreprocessor
- Implemented BatchFilePreprocessor
- Implemented abstract Saver
- Implemented utility functions to create directory hierarchy with and without
file in input
- Implemented relative unittests

# [0.0.11] - 24.08.21 - Valerio Velardo
- Using an enumeration class for referring to transforms types instead of
strings
- Updated all transforms to use TransformTypes class
- MagnitudeSpectrogram and PowerSpectrogram have an STFT object, instead of
inheriting from it
- Updated unittests to reflect changes

# [0.0.10] - 24.08.21 - Valerio Velardo
- Implemented batch transformations in TransformsChain
- Implemented unittests for TransformsChain

# [0.0.9] - 24.08.21 - Valerio Velardo
- Implemented Log transform with unittests

# [0.0.8] - 24.08.21 - Valerio Velardo
- Implemented scaling transforms (Scaler base class, MinMaxScaler,
Standardiser, RowStandardiser)
- Added NotA2DSignalError
- Implemented unittests

# [0.0.7] - 23.08.21 - Valerio Velardo
- Implemented MagnitudeSpectrogram
- Implemented PowerSpectrogram
- Implemented MelSpectrogram
- Implemented MFCCSpectrogram
- Implemented unittests

# [0.0.6] - 23.08.21 - Valerio Velardo
- Implemented Short-Time Fourier Transform object
- Implemented STFT unittests

# [0.0.5] - 21.08.21 - Valerio Velardo
- Implemented NumpySaver object
- Implemented abstract interface for transforms
- Implemented unittests for NumpySaver

# [0.0.4] - 21.08.21 - Valerio Velardo
- Implemented Loader object
- Implemented Signal object
- Implemented FileExtensionError
- Implemented unittests for all new objects

# [0.0.3] - 21.08.21 - Valerio Velardo
- Added Makefile with quick commands for installing, linter, testing, typehint
- Added mypy and pylint config files

# [0.0.2] - 11.10.20 - Valerio Velardo
- Added dummy file and unittest for testing Github Actions works

# [0.0.1] - 11.10.20 - Valerio Velardo
- Laid out repo structure