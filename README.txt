==-------------------------------------------==
==             SigmaProject v0.1             ==
==   https://github.com/k-zen/SigmaProject   ==
== Author: Andreas P. Koenzen <akc@apkc.net> ==
==-------------------------------------------==

Uses:
=====
sigmaproject [--monte-carlo] [-t=type] [i=1000]

    For type 1:
    ===========
    [-f=function] [-a=0] [-b=1]

Options:
========
    --monte-carlo Uses the "Monte Carlo" procedure to estimate some value
                  defined by the parameter *-t*.

    ---

    -t The type of calculation to perform. Posible values are:

        Type #1:
        ========
        Calculate the area under the curve defined by parameter *f*
        and between the interval (b - a).

    -i The amount of iterations to perform.
    -a The X coordinate of *a*. Must the smaller than *b*.
    -b The X coordinate of *b*. Must be bigger than *a*.

    ---

Flags:
======
    --help Shows this message.