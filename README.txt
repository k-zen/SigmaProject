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