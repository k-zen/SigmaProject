# -*- coding: utf-8 -*-

from sklearn import *


class Data(object):
    """
    Utility class to generate data sets.
    """

    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """

    def __init__(self):
        self.data = None

    def generate_data(self, type: int = 0) -> None:
        """
        Generate data to train the network.

        :param type: The type of data to generate.

        :returns: Void
        """
        if type == 0:
            self.data = datasets.make_moons(
                n_samples=200,
                shuffle=True,
                noise=0.2,
                random_state=42
            )
        elif type == 1:
            self.data = datasets.make_circles(
                n_samples=200,
                shuffle=True,
                noise=0.2,
                factor=0.5,
                random_state=1
            )

        return None
