import pynq
from pynq import GPIO

__author__ = "Omer Can Akgun"
__email__ = "oca@ocakgun.com"


class UltraOverlay(pynq.Overlay):
    """The Ultra96 overlay for Ultra96 board

    """
    def __init__(self, bitfile, **kwargs):
        super().__init__(bitfile, **kwargs)
        if self.is_loaded():
            pass
