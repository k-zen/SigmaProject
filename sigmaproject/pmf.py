# -*- coding: utf-8 -*-

import random
import sigmaproject.probability_map as pm


class PMF(pm.ProbabilityMap):
    """
    Represents a probability mass function. Values can be any hashable type; probabilities
    are floating-point. PMFs are not necessarily normalized.
    """

    DEBUG = True
    """
    boolean: Flag to enable debug mode.
    """

    def get_probability(self, x: int, default: float = 0.0):
        """
        Gets the probability associated with the value x.

        :param x: Value for the random variable.
        :param default: Default value to return if the key is not there.

        :returns float The probability for the random variable.
        """
        return self.probability_map.get(x, default)

    def get_probabilities(self, xs: [int]):
        """
        Get the probabilities for a list of random variable.

        :param xs: A list of random variables.

        :returns list A list of probabilities.
        """
        return [self.get_probability(x) for x in xs]

    def random(self):
        """
        Chooses a random value from this PMF.

        :returns float The probability associated with the random value.
        """
        if len(self.probability_map) == 0.0:
            raise ValueError('PMF contains no values.')

        target = random.random()
        total = 0.0
        for x, p in self.probability_map.items():
            total += p
            if total >= target:
                return x
