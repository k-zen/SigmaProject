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
            return np.exp(output) / np.sum(np.exp(output), axis=1, keepdims=True)

        return None
