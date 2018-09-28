# -*- coding: utf-8 -*-


class ProbabilityMap(object):
    """
    A probability map object. The map is as follows:

        Hypothesis:STRING => Probability:FLOAT (Can be normalized or unnormalized)
        ...
        ...
    """

    DEBUG = True
    """
    boolean: Flag to enable debug mode.
    """

    def __init__(self, hypotheses: [str] = None, map_name: str = ""):
        """
        Initializes a probability map using given hypotheses. Each hypothesis is given
        a value according to a discrete uniform distribution. This map will be normalized
        when this function returns.

        :param hypotheses: The list of hypotheses.
        :param map_name: The name of the map.

        :returns A probability map object.
        """
        self.map_name: str = map_name
        self.probability_map: {str: float} = dict()

        # flag whether the distribution is under a log transform
        self.log = False

        if hypotheses is None:
            return

        init_methods = [
            self.init_sequence,
            self.init_failure
        ]

        for method in init_methods:
            try:
                method(hypotheses)
                break
            except AttributeError:
                continue

        if len(self.probability_map) > 0:
            self.normalize()

    def init_sequence(self, hypotheses: [str]):
        """
        Initializes the probability map using a discrete uniform distribution. This sequence
        needs to be normalized before it can be used.

        :param hypotheses: The hypotheses.
        """
        for hypothesis in hypotheses:
            self.set(hypothesis, 1.0)

    def init_failure(self, values):
        """
        Raises an error.
        """
        raise ValueError('None of the initialization methods worked.')

    def normalize(self):
        """
        Normalizes this PMF so the sum of all probabilities equals 1.

        :returns The denominator.
        """
        if self.log:
            raise ValueError("PMF is under a log transform")

        denominator = self.total()
        if denominator == 0.0:
            raise ValueError('Denominator is zero.')

        factor = 1.0 / denominator
        for x in self.probability_map:
            self.probability_map[x] *= factor

        return denominator

    def __len__(self):
        return len(self.probability_map)

    def __iter__(self):
        return iter(self.probability_map)

    def iterkeys(self):
        return iter(self.probability_map)

    def __contains__(self, value):
        return value in self.probability_map

    def get_dict(self):
        return self.probability_map

    def set_dict(self, probability_map):
        self.probability_map = probability_map

    def keys(self):
        return self.probability_map.keys()

    def values(self):
        return self.probability_map.values()

    def items(self):
        return self.probability_map.items()

    def render(self):
        """
        Generates a key sorted sequence of tuples (hypothesis, probability).

        :returns Tuple of (hypothesis, probability).
        """
        return zip(*sorted(self.items()))

    def print(self):
        """
        Prints the hypotheses and probabilities in ascending order.
        """
        for k, v in sorted(self.probability_map.items()):
            print(k, v)

    def set(self, hypothesis: str, probability=0.0):
        """
        Sets the probability associated with hypothesis.

        :param hypothesis: The hypothesis.
        :param probability: The probability.
        """
        self.probability_map[hypothesis] = probability

    def increment(self, hypothesis: str, value: float = 1.0):
        """
        Increments the probability associated with hypothesis.

        :param hypothesis: The hypothesis.
        :param value: How much to increment.
        """
        self.probability_map[hypothesis] = self.probability_map.get(hypothesis, 0.0) + value

    def multiply(self, hypothesis: str, multiplier: float):
        """
        Multiplies the probability associated with the value of X times the multiplier.
        Each hypothesis has a probability associated to it, and that value will be multiplied
        againts the multiplier. Also updates the value of X after.

        :param hypothesis: The name associated with the probability X.
        :param multiplier: The multiplier.

        :returns void
        """
        self.probability_map[hypothesis] = self.probability_map.get(hypothesis, 0.0) * multiplier

    def remove(self, hypothesis: str):
        """
        Removes an hypothesis. Throws an exception if it's not there.

        :param hypothesis: Hypothesis to remove.
        """
        del self.probability_map[hypothesis]

    def total(self):
        """
        Returns the total sum of the probabilities in the map.
        """
        return sum(self.probability_map.values())

    def maximum_likelihood(self):
        """
        Returns the largest probability in the map.
        """
        return max(self.probability_map.values())
