"""This module contains a class to extract MFCCs from a signal."""


from praudio.transform.transform import Transform


class MFCC(Transform):
    """This class extracts MFCCs from a signal. It's a concrete Transform.
    librosa facilities are used to extract MFCCs.

    Attributes:
        -
    """
