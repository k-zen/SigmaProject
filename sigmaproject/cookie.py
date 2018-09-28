# -*- coding: utf-8 -*-

import sigmaproject.probability_tree as pt


class Cookie(pt.ProbabilityTree):
    """
    Class to compute odds for the cookie problem. It supports multiple events and updating of probabilities
    through a decision tree.

    Problem:
    ========
    Suppose there are two bowls of cookies. Bowl #1 contains 30 vanilla cookies and 10
    chocolate cookies. Bowl #2 contains 20 of each. Now suppose you choose one of the
    bowls at random and, without looking, select a cookie at random. The cookie is vanilla.

    Question:
    =========
    Find the probability that the cookie came from bowl #1 GIVEN it was vainilla's.

    Solution:
    =========
    p(Bowl #1 / Vainilla) = ?

    p(Bowl #1 / Vainilla) = p(Bowl #1) * p (Vainilla / Bowl #1)
                            -----------------------------------
                                        p(Vainilla)

    p(Bowl #1) = 1/2 (The prior is 1/2 for each bowl. Uniform distribution)
    p(Vainilla / Bowl #1) = 30/40 (To estimate the likelihood we always count!)
    p(Vainilla) = p(Vainilla / Bowl #1) * p(Bowl #1) + p(Vainilla / Bowl #2) * p(Bowl #2) (Law of total probabilities)

    Updating:
    =========
    Now we can support updating through a decision tree. So the following is supported:

        1. If we draw a vainilla cookie from Bowl #1, what is the probability of drawing another vainilla cookie
        from Bowl #1.
        2. If we draw two vainilla cookies from Bowl #1, what is the probability of drawing a chocolate cookie from
        Bowl #2.
        3. And so on until we don't have any more cookies.

    This solution is based on the fact that the cookies are not replaceable, that is we can draw cookies until we don't have
    any in either bowl.

    Experiment:
    ===========
    We can conduct an experiment in the following manner:

        1. Extract a cookie, verify what type it is.
        2. Compute the probability that it came from each bowl.
        3. Verify and see from which bowl it came.
        4. Update the likelihood.
        5. Repeat.

    We can use a Monte Carlo simulation to select cookie type and bowl randomly.
    """

    def __init__(self):
        pt.ProbabilityTree.__init__(self)  # initialize the parent first!

        # load the decision tree with the initial values
        self.update_tree(self.probability_tree, self.NODE_1, pt.Fraction(1, 2))
        self.update_tree(self.probability_tree, self.NODE_2, pt.Fraction(1, 2))
        self.update_tree(self.probability_tree, self.NODE_3, pt.Fraction(30, 40))
        self.update_tree(self.probability_tree, self.NODE_4, pt.Fraction(10, 40))
        self.update_tree(self.probability_tree, self.NODE_5, pt.Fraction(20, 40))
        self.update_tree(self.probability_tree, self.NODE_6, pt.Fraction(20, 40))

    @staticmethod
    def compute():
        cookie = Cookie()
        cookie.print()  # print the initial values

        # iterate, update and print
        return
