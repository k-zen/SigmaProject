# -*- coding: utf-8 -*-

import numpy as np

from enum import Enum


class ActivationFunctionType(Enum):
    """
    Enum to represent the different types of
    activation functions available to the network.
    """
    SIGMOID = 1
    TANH = 2
    RELU = 3
    LEAKY_RELU = 4
    MAXOUT = 5
    ELU = 6


class ActivationFunction(object):
    """
    Class representing an Activation Function.
    """

    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """

    def __init__(self, type: ActivationFunctionType):
        """
        Initializes an ActivationFunction object.

        :param type: The type of function.
        """
        self.type = type

    def activate(self, output: np.ndarray) -> np.ndarray:
        """
        Run the activation function on the neuron output data.

        :param output: The output matrix.

        :return: An n-dimensional array with the output matrix.
        """
        if self.type == ActivationFunctionType.TANH:
            return np.tanh(output)
        elif self.type == ActivationFunctionType.SIGMOID:
            return np.exp(output) / np.sum(np.exp(output),
                                           axis=1,
                                           keepdims=True)

        # TODO: Implement other functions.

        return None
