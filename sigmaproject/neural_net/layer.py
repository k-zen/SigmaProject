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
from .activation_function import ActivationFunction


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
