"""This module features a class that preprocesses an audio file in one go."""

import logging

from praudio.transformschain import TransformsChain
from praudio.io.loader import Loader
from praudio.io.saver import Saver


logger = logging.getLogger(__name__)


class FilePreprocessor:
    """FilePreprocessor is responsible to preprocess a an audio file stored
    on disk and to save the preprocessed signal on disk.

    Attributes:
        - loader: Loader object
        - transforms_chain: Sequence of transforms to apply to signal
        - saver: Object responsible for saving a transformed signal to disk
    """

    def __init__(self,
                 loader: Loader,
                 transforms_chain: TransformsChain,
                 saver: Saver):
        self.loader = loader
        self.transforms_chain = transforms_chain
        self.saver = saver
        logger.info("Initialised FilePreprocessor object")


    def preprocess(self, audio_file: str, save_path: str):
        """Preprocess an audio file with the followiing steps:
            1- load audio file
            2- apply chain of transformations to signal
            3- store transformed signal

        :param audio_file: Path to audio file to preprocess
        :param save_path: Path where to save preprocessed signal. The path
            shouldn't have an extension
        """
        signal = self.loader.load(audio_file)
        signal = self.transforms_chain.process(signal)
        self.saver.save(save_path, signal.data)
        logger.info("Preprocessed file %s", audio_file)
