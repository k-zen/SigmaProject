# -*- coding: utf-8 -*-


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
    """
    Terminal interactions.
    """
    CLEAR_CONSOLE = "\033[H\033[J"
