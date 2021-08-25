"""
This module contains a class that applies multiple transforms
sequentially on a signal.
"""

from typing import List

from praudio.transforms.transform import Transform
from praudio.io.signal import Signal


class TransformsChain():
    """Apply multiple transforms on a signal in a sequential manner."""

    def __init__(self, transforms: List[Transform]):
        self.transforms = transforms

    @property
    def transforms_names(self):
        transform_names = [transform.name.value for transform in
                           self.transforms]
        return transform_names

    def process(self, signal: Signal) -> Signal:
        """Apply multiple transforms sequentially to a signal.

        :param signal: Signal to transform

        :return: Modified signal
        """
        for transform in self.transforms:
            signal = transform.process(signal)
        return signal
