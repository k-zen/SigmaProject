# -*- coding: utf-8 -*-

"""
Copyright (c) 2019, Andreas Koenzen <akoenzen | uvic.ca>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

import random

from math import *
from colorama import Style


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
        Uses the Monte Carlo procedure to compute the area under the curve for
        a given function (Numerical integration). The logic for this method was extracted
        from `<https://www.scratchapixel.com/lessons/mathematics-physics-for-computer-graphics/monte-carlo-methods-in-practice/monte-carlo-integration>`_.

        See `<http://people.math.sc.edu/meade/Bb-CalcI-WMI/Unit5/HTML-GIF/MVTIntegral.html>`_ for more
        information about the "Average Value of a Function".

        ``Example``::

            $ python -m sigmaproject --monte-carlo -t 1 -i 1000000 -f "sin(x) + (1/3 * sin(3*x))" -a 0 -b 3.141592653589793

        :param iterations: How many iterations to make.
        :param function:   The f(x)
        :param xa:         The X value of *a*.
        :param xb:         The X value of *b*.

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

        print(Style.BRIGHT + "=======" + Style.RESET_ALL)
        print(Style.BRIGHT + "RESULT:" + Style.RESET_ALL)
        print(Style.BRIGHT + "> Area of E: \"{0}\"".format(ev) + Style.RESET_ALL)
        print(Style.BRIGHT + "> Error Margin: +-\"{0}\"".format(1 / n ** 0.5) + Style.RESET_ALL)
        print(Style.BRIGHT + "=======" + Style.RESET_ALL)
