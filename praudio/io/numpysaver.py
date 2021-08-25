"""
This module contains facilities to store numpy arrays. It can be used to
store audio features (e.g., MFCC, Spectrogram).
"""

import logging

import numpy as np

from praudio.io.saver import Saver
from praudio.utils import add_extension_to_file


logger = logging.getLogger(__name__)


class NumpySaver(Saver):
    """NumpySaver saves arrays as npy files. It's a wrapper around numpy
    saving facilities.
    """
    def __init__(self):
        super().__init__("npy")
        logger.info("Initialised NumpySaver object")

    def save(self,
             file: str,
             array: np.ndarray):
        """Store array as an npy file.

        :param file: Path where to save file without extension
        :param array: Numpy array to store
        """
        file_with_extension = add_extension_to_file(file, self.extension)
        np.save(file_with_extension, array)
        logger.info("Array saved at %s", file_with_extension)
