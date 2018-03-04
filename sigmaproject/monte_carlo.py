# -*- coding: utf-8 -*-

"""
Class to perform Monte Carlo simulations.

.. module:: monte_carlo
   :platform: Unix
   :synopsis: Monte Carlo functions.

.. moduleauthor:: Andreas P. Koenzen <akc@apkc.net>
"""

import sigmaproject.utils as utils
import random

__author__ = "Andreas P. Koenzen"
__copyright__ = "Copyright 2018. Andreas P. Koenzen"
__credits__ = "Andreas P. Koenzen"
__license__ = "BSD"
__version__ = "0.1"
__maintainer__ = "Andreas P. Koenzen"
__email__ = "akc@apkc.net"
__status__ = "Prototype"


class MonteCarlo:
    """
    Monte Carlo simulation's functions.
    """

    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """

    def __init__(self):
        pass

    @staticmethod
    def area_under_curve(iterations, function, xa, xb):
        """
        Uses the Monte Carlo procedure to compute the area under the curve of
        a given curve. Numerical integration.

        :param iterations: How many iterations to make.
        :param function: The f(x)
        :param xa: The X value of *a*.
        :param xb: The X value of *b*.

        :return: void
        """
        result = 0

        if MonteCarlo.DEBUG == 1:
            print("\t=== DEBUG ===")

        for k in range(0, iterations):
            x = xa + (random.uniform(0.0, 1.0) * (xb - xa))

            if MonteCarlo.DEBUG == 1:
                print("\t{0}".format(x))

            result += eval(function) * (xb - xa)

        print(utils.Colors.BOLD + "=======" + utils.Colors.ENDC)
        print(utils.Colors.BOLD + "RESULT:" + utils.Colors.ENDC)
        print(utils.Colors.BOLD + "> Area of E: \"{0}\"".format(result / iterations) + utils.Colors.ENDC)
        print(utils.Colors.BOLD + "> Error Margin: +-\"{0}\"".format(1 / iterations ** 0.5) + utils.Colors.ENDC)
        print(utils.Colors.BOLD + "=======" + utils.Colors.ENDC)
