# -*- coding: utf-8 -*-

class Colors:
    def __init__(self):
        pass

    BOLD = "\033[1m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"


class Terminal:
    CLEAR_CONSOLE = "\033[H\033[J"
