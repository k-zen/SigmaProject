# -*- coding: utf-8 -*-

"""
==-------------------------------------------==
==             SigmaProject v0.1             ==
==   https://github.com/k-zen/SigmaProject   ==
== Author: Andreas P. Koenzen <akc@apkc.net> ==
==-------------------------------------------==

Uses:
=====
sigmaproject [--monte-carlo] [-t=type] [i=1000] [-f=function] [-a=0] [-b=1] [--plot]

Options:
========
    Available Functions:
    ====================
    --monte-carlo Uses the "Monte Carlo" procedure to estimate some value
                  defined by the parameter *-t*.

    Parameters:
    ===========
    -t The type of calculation to perform. Posible values are:

        Type #1:
        ========
        Calculate the area under the curve defined by parameter *f*
        and between the interval (b - a).

    -i The amount of iterations to perform.
    -a The X coordinate of *a*. Must the smaller than *b*.
    -b The X coordinate of *b*. Must be bigger than *a*.

    Others:
    =======
    --plot Plot the aproximation using a scatter plot.

Flags:
======
    --help Shows this message.
"""

import sigmaproject.utils as utils
import sigmaproject.montecarlo as montecarlo
import getopt
import sys

__author__ = "Andreas P. Koenzen"
__copyright__ = "Copyright 2018. Andreas P. Koenzen"
__credits__ = "Andreas P. Koenzen"
__license__ = "BSD"
__version__ = "0.1"
__maintainer__ = "Andreas P. Koenzen"
__email__ = "akc@apkc.net"
__status__ = "Prototype"


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def usage():
    print(sys.exit(__doc__))


def main(argv=None):
    command = 0
    type = -1
    iterations = 1000
    function = ""
    xa = -1.0
    xb = -1.0
    plot = False

    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(
                argv[1:],
                "t:i:f:a:b:",
                [
                    "help",
                    "monte-carlo",
                    "plot"
                ]
            )
            if not opts:
                usage()
        except getopt.error as msg:
            raise Usage(msg)

        # DEBUG:
        # print opts

        for opt, arg in opts:
            if opt == "--help":
                usage()
            elif opt == "--monte-carlo":
                command = 1
            elif opt == "--plot":
                plot = True
            elif opt == "-t":
                type = int(arg)
            elif opt == "-i":
                iterations = int(arg)
            elif opt == "-f":
                function = arg
            elif opt == "-a":
                xa = float(arg)
            elif opt == "-b":
                xb = float(arg)

        # tomar la decision.
        if command == 1:
            if function == "":
                print(utils.Colors.FAIL + "ERROR: Function not defined." + utils.Colors.ENDC)
                return 2
            if xa == -1.0 or xb == -1.0:
                print(utils.Colors.FAIL + "ERROR: Interval not defined." + utils.Colors.ENDC)
                return 2

            if type == 1:
                montecarlo.MonteCarlo.area_under_curve(iterations, function, xa, xb, plot)
            else:
                print(utils.Colors.FAIL + "ERROR: The type is invalid." + utils.Colors.ENDC)
                return 2
    except Usage as err:
        print(utils.Colors.FAIL + "ERROR: {0}".format(err.msg) + utils.Colors.ENDC)
        print(utils.Colors.BOLD + "INFO: For help use --help" + utils.Colors.ENDC)
        return 2


if __name__ == "__main__":
    sys.exit(main())
