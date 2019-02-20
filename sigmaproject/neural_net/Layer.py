# -*- coding: utf-8 -*-

import numpy as np

from enum import Enum
from .ActivationFunction import ActivationFunction


class LayerType(Enum):
    INPUT = 1
    HIDDEN = 2
    OUTPUT = 3


class Layer(object):
    """
    Class representing a Neural Network Layer.
    """

    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """

    def __init__(self,
                 input_size: int,
                 output_size: int,
                 type: LayerType,
                 af: ActivationFunction):
        """
        Initializes a Layer object.

        :param input_size: The number of rows.
        :param output_size: The number of columns.
        :param type: The type of layer.
        :param af: The activation function to use in this layer.
        """
        # Initialize the weights matrix according to the paper by
        # He et al., 2015. See slide 16 "Preventing Overfitting" of CSC 586B.
        self.W = np.random.randn(input_size, output_size) / np.sqrt(input_size / 2)
        self.b = np.zeros(shape=(1, output_size))
        self.a = None
        self.type = type
        self.af = af
