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

"""
==--------------------------------------------==
== SigmaProject v0.1                          ==
== https://github.com/k-zen/SigmaProject      ==
== Author: Andreas Koenzen <akoenzen@uvic.ca> ==
== -------------------------------------------==
== Disclaimer: NOT to be used in production.  ==
==             ONLY for educational purposes. ==
==--------------------------------------------==

Uses:
=====
sigmaproject [--monte-carlo] [-t=type] [i=1000] [-f=function] [-a=0] [-b=1]
             [--classifier]  [-t=type]

Options:
========
    Available Functions:
    ====================
    --monte-carlo Uses the "Monte Carlo" procedure to estimate some value
                  defined by the parameter *-t*.
    --classifier  Executes a classifier to perform some classification task.

    Parameters:
    ===========
    -t The type of calculation to perform. Posible values are:

        Monte Carlo:
            Type #1: Numerical Integration. Calculate the area under the curve defined by parameter *f* and between the interval (b - a).

        Classifier:
            Type #1: Naive Bayes Text Classifier. Done for CSC 578D at UVic.

    -i The amount of iterations to perform.
    -a The X coordinate of *a*. Must the smaller than *b*.
    -b The X coordinate of *b*. Must be bigger than *a*.

Flags:
======
    --help Shows this message.
"""

import sigmaproject.montecarlo as montecarlo
import sigmaproject.naive_bayes_text_classifier as nbtc
import getopt
import sys

from colorama import Back, Style


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def usage():
    print(sys.exit(__doc__))


def main(argv=None):
    command = 0
    type = -1
    iterations = 1000
    function = ''
    xa = -1.0
    xb = -1.0

    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(
                argv[1:],
                't:i:f:a:b:',
                [
                    'help',

                    'monte-carlo',
                    'classifier'
                ]
            )
            if not opts:
                usage()
        except getopt.error as msg:
            raise Usage(msg)

        # DEBUG:
        # print opts

        for opt, arg in opts:
            if opt == '--help':
                usage()
            elif opt == '--monte-carlo':
                command = 1
            elif opt == '--classifier':
                command = 2
            elif opt == '-t':
                type = int(arg)
            elif opt == '-i':
                iterations = int(arg)
            elif opt == '-f':
                function = arg
            elif opt == '-a':
                xa = float(arg)
            elif opt == '-b':
                xb = float(arg)

        if command == 1:  # Monte Carlo
            if function == '':
                print(Back.RED + 'ERROR: Function not defined.' + Style.RESET_ALL)
                return 2
            if xa == -1.0 or xb == -1.0:
                print(Back.RED + 'ERROR: Interval not defined.' + Style.RESET_ALL)
                return 2

            if type == 1:
                montecarlo.MonteCarlo.area_under_curve(iterations, function, xa, xb)
            else:
                print(Back.RED + 'ERROR: The type is invalid.' + Style.RESET_ALL)
                return 2
        elif command == 2:  # Classifier
            if type == 1:
                classifier = nbtc.NaiveBayesTextClassifier()
                classifier.classify(model=classifier.train())
            else:
                print(Back.RED + 'ERROR: The type is invalid.' + Style.RESET_ALL)
                return 2
    except Usage as err:
        print(Back.RED + 'ERROR: {0}'.format(err.msg) + Style.RESET_ALL)
        print(Style.BRIGHT + 'INFO: For help use --help' + Style.RESET_ALL)
        return 2


if __name__ == '__main__':
    sys.exit(main())
