# -*- coding: utf-8 -*-

"""
Utility file.

.. module:: utils
   :platform: Unix
   :synopsis: Utility functions

.. moduleauthor:: Andreas P. Koenzen <akc@apkc.net>
"""

__author__ = "Andreas P. Koenzen"
__copyright__ = "Copyright 2018. Andreas P. Koenzen"
__credits__ = "Andreas P. Koenzen"
__license__ = "BSD"
__version__ = "0.1"
__maintainer__ = "Andreas P. Koenzen"
__email__ = "akc@apkc.net"
__status__ = "Prototype"


class Colors:
    """
    Terminal colors.
    """

    def __init__(self):
        pass

    BOLD = "\033[1m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


class Terminal:
    CLEAR_CONSOLE = "\033[H\033[J"
