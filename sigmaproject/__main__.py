# -*- coding: utf-8 -*-

"""
==--------------------------------------------==
==             SigmaProject v0.1              ==
==                                            ==
== WS: https://github.com/k-zen/SigmaProject  ==
== Author: Andreas Koenzen <akoenzen@uvic.ca> ==
==                                            ==
== -------------------------------------------==
== Disclaimer: NOT to be used in production.  ==
==             ONLY for educational purposes. ==
==--------------------------------------------==

Uses:
=====
sigmaproject [--monte-carlo] [-t=type] [i=1000] [-f=function] [-a=0] [-b=1]
             [--bayes]       [-t=type] TODO
             [--classifier]  [-t=type] [--input=] [--output]
             [--regression]  [-t=type] TODO
             [--tensorflow]  [-t=type] TODO
             [--clustering]  [-t=type] TODO

Options:
========
    Available Functions:
    ====================
    --monte-carlo Uses the "Monte Carlo" procedure to estimate some value
                  defined by the parameter *-t*.
    --bayes       Bayesian computation.
    --classifier  Executes a classifier to perform some classification task.
    --regression  Executes a regression algorithm on some data set.
    --tensorflow  Executes an algorithm using tensorflow library on some data set.
    --clustering  Executes a clustering algorithm on some data set.

    Parameters:
    ===========
    -t The type of calculation to perform. Posible values are:

        Monte Carlo:
            Type #1: Numerical Integration. Calculate the area under the curve defined by parameter *f* and between the interval (b - a).

        Bayes:
            Type #1: Cookie problem from book Think Bayes

        Classifier:
            Type #1: Naive Bayes Text Classifier
            Type #2: Decision Tree / ID3

        Regression:
            Type #1: Simple Linear Regression TODO
            ========
            Makes a prediction using a Simple Linear Regression model.

        TensorFlow:
            Type #1: TODO
            ========
            TODO

        Clustering:
        ===========
            Type #1: DBSCAN TODO
            ========
            TODO

    -i The amount of iterations to perform.
    -a The X coordinate of *a*. Must the smaller than *b*.
    -b The X coordinate of *b*. Must be bigger than *a*.

    Others:
    =======
    --plot   Plot the aproximation using a scatter plot.
    --input  The input file to classify. Usually in text format, where each line is a sentence.
    --output The output file. Should be a file name.

Flags:
======
    --help Shows this message.
"""

import sigmaproject.utils as utils
import sigmaproject.cookie as cookie
import sigmaproject.montecarlo as montecarlo
import sigmaproject.naive_bayes_text_classifier as nbtc
import getopt
import sys


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
    plot = False
    input: str = ''
    output: str = ''

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
                    'bayes',
                    'classifier',
                    'regression',
                    'tensorflow',
                    'clustering'

                    'plot',
                    'input',
                    'output'
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
            elif opt == '--bayes':
                command = 2
            elif opt == '--classifier':
                command = 3
            elif opt == '--regression':
                command = 4
            elif opt == '--tensorflow':
                command = 5
            elif opt == '--clustering':
                command = 6
            elif opt == '--plot':
                plot = True
            elif opt == '--input':
                input = str(arg)
            elif opt == '--output':
                output = str(arg)
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
                print(utils.Colors.FAIL + 'ERROR: Function not defined.' + utils.Colors.ENDC)
                return 2
            if xa == -1.0 or xb == -1.0:
                print(utils.Colors.FAIL + 'ERROR: Interval not defined.' + utils.Colors.ENDC)
                return 2

            if type == 1:
                montecarlo.MonteCarlo.area_under_curve(iterations, function, xa, xb, plot)
            else:
                print(utils.Colors.FAIL + 'ERROR: The type is invalid.' + utils.Colors.ENDC)
                return 2
        elif command == 2:  # Bayes
            if type == 1:
                cookie.Cookie.compute()
            else:
                print(utils.Colors.FAIL + 'ERROR: The type is invalid.' + utils.Colors.ENDC)
                return 2
        elif command == 3:  # Classifier
            if type == 1:
                if False and (input == "" or output == ""):  # disable this for the moment. only deal with static urls
                    print(utils.Colors.FAIL + 'ERROR: Input or output not defined.' + utils.Colors.ENDC)
                    return 2

                nbtc.NaiveBayesTextClassifier().classify(model=nbtc.NaiveBayesTextClassifier().train())
            else:
                print(utils.Colors.FAIL + 'ERROR: The type is invalid.' + utils.Colors.ENDC)
                return 2
        elif command == 4:  # Regression
            if type == 1:
                return 2
            else:
                print(utils.Colors.FAIL + 'ERROR: The type is invalid.' + utils.Colors.ENDC)
                return 2
        elif command == 5:  # TensorFlow
            if type == 1:
                return 2
            else:
                print(utils.Colors.FAIL + 'ERROR: The type is invalid.' + utils.Colors.ENDC)
                return 2
        elif command == 6:  # Clustering
            if type == 1:
                return 2
            else:
                print(utils.Colors.FAIL + 'ERROR: The type is invalid.' + utils.Colors.ENDC)
                return 2
    except Usage as err:
        print(utils.Colors.FAIL + 'ERROR: {0}'.format(err.msg) + utils.Colors.ENDC)
        print(utils.Colors.BOLD + 'INFO: For help use --help' + utils.Colors.ENDC)
        return 2


if __name__ == '__main__':
    sys.exit(main())
