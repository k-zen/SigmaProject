# -*- coding: utf-8 -*-

"""
Class to perform Monte Carlo simulations.

.. module:: montecarlo
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
    def area_under_curve(iterations, function, xa, xb, plot):
        """
        Uses the Monte Carlo procedure to compute the area under the curve for
        a given function (Numerical integration). The logic for this method was extracted
        from `this <https://www.scratchapixel.com/lessons/mathematics-physics-for-computer-graphics/monte-carlo-methods-in-practice/monte-carlo-integration>`_
        URL.

        See `this <http://people.math.sc.edu/meade/Bb-CalcI-WMI/Unit5/HTML-GIF/MVTIntegral.html>`_ site for more
        information about the "Average Value of a Function".

        :param iterations: How many iterations to make.
        :param function:   The f(x)
        :param xa:         The X value of *a*.
        :param xb:         The X value of *b*.
        :param plot:       If TRUE a scatter plot will be generated.

        :return: void
        """
        ev = 0  # expected value
        sum = 0  # summation
        n = iterations

        if MonteCarlo.DEBUG == 1:
            print("\t=== DEBUG ===")

        for k in range(0, n):
            x = xa + (random.uniform(0.0, 1.0) * (xb - xa))

            if MonteCarlo.DEBUG == 1:
                print("\t{0}".format(x))

            sum += eval(function)

        ev = ((xb - xa) / n) * sum

        print(utils.Colors.BOLD + "=======" + utils.Colors.ENDC)
        print(utils.Colors.BOLD + "RESULT:" + utils.Colors.ENDC)
        print(utils.Colors.BOLD + "> Area of E: \"{0}\"".format(ev) + utils.Colors.ENDC)
        print(utils.Colors.BOLD + "> Error Margin: +-\"{0}\"".format(1 / n ** 0.5) + utils.Colors.ENDC)
        print(utils.Colors.BOLD + "=======" + utils.Colors.ENDC)
