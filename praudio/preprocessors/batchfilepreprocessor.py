"""
This module contains BatchFilePreprocessor, an object responsible to
preprocess all files in a path.
"""

import logging
import os

from praudio.preprocessors.filepreprocessor import FilePreprocessor
from praudio.utils import remove_extension_from_file, create_dir_hierarchy_from_file


logger = logging.getLogger(__name__)


class BatchFilePreprocessor:
    """BatchFilePreprocessor preprocesses all files in a directory recursively
    and stores them on disk respecting their hierarchy. It's a wrapper
    around a file processor that handles multiple files.

    Attributes:
        - preprocessor: Preprocess single file
        - dataset_dir: Path to dataset to preprocess
        - save_dir: Where to store preprocessed signals
    """

    def __init__(self,
                 preprocessor: FilePreprocessor,
                 dataset_dir: str,
                 save_dir: str):
        self.preprocessor = preprocessor
        self.dataset_dir = dataset_dir
        self.save_dir =save_dir
        logger.info("Initialised BatchFilePreprocessor object")

    def preprocess(self):
        """Batch preprocess all data in a dir recursively."""
        for root, _, files in os.walk(self.dataset_dir):
            for file in files:
                file_path = os.path.join(root, file)
                save_path = self._infer_save_path(file_path)
                create_dir_hierarchy_from_file(save_path)
                self.preprocessor.preprocess(file_path, save_path)
        logger.info("Preprocessed all dataset at %s", self.dataset_dir)

    def _infer_save_path(self, file_path: str) -> str:
        relative_path = os.path.relpath(file_path, self.dataset_dir)
        save_path = os.path.join(self.save_dir, relative_path)
        save_path_without_extension = remove_extension_from_file(save_path)
        return save_path_without_extension
