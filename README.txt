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