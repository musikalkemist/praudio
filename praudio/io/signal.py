"""
This module provides a data structure that stores an audio signal with
additional info.
"""

from dataclasses import dataclass

import numpy as np


@dataclass
class Signal:
    """Signal is a data structure that represents a signal. It can be used
    for storing waveforms, as well as other audio features (e.g., MFCC,
    MelSpectrogram).

    Attributes:
        - name: Type of signal (e.g., waveform, mfcc)
        - sample_rate: Sampling rate of signal
        - data: Signal data
        - file: File path where signal was originally loaded from
    """
    name: str
    sample_rate: int
    data: np.ndarray
    file: str = ""
