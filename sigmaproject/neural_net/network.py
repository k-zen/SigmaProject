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

from .activation_function import ActivationFunction, ActivationFunctionType
from .layer import Layer


class Network(object):
    """
    Class representing a Neural Network.
    """

    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """

    LAMBDA = 0.0001
    """
    float: Regularization strength.
    """

    ALPHA = 0.0001
    """
    float: Learning rate for gradient descent.
    """

    def __init__(self):
        self.initial_input = None
        self.layers = [Layer]  # Initialize to cero layers.

    def add_layer(self, layer: Layer) -> None:
        """
        Add a new layer to the Network.

        :param layer: The layer object to add.

        :returns: Void
        """
        self.layers.append(layer)

        return None

    def forward(self, initial_input: np.ndarray) -> None:
        self.initial_input = initial_input

        self.layers[1].a = self.layers[1].af.activate(
            np.matmul(
                initial_input,
                self.layers[1].W
            ) + self.layers[1].b
        )
        self.layers[2].a = self.layers[2].af.activate(
            np.matmul(
                self.layers[1].a,
                self.layers[2].W
            ) + self.layers[2].b
        )

        return self.layers[2].a

    def backward(self, X_train: np.ndarray, labels: np.ndarray) -> None:
        delta3 = self.layers[2].a.copy()
        delta3[range(self.layers[2].a.shape[0]), labels] -= 1
        dW2 = (self.layers[1].a.T).dot(delta3)
        db2 = np.sum(delta3, axis=0, keepdims=True)

        if self.layers[1].af.type == ActivationFunctionType.TANH:
            delta2 = delta3.dot(self.layers[2].W.T) * (1 - np.power(self.layers[1].a, 2))
        elif self.layers[1].af.type == ActivationFunctionType.SIGMOID:
            delta2 = delta3.dot(self.layers[2].W.T) * (
                    (1 - (np.exp(self.layers[1].a) / np.sum(np.exp(self.layers[1].a), axis=1, keepdims=True))) * (
                    np.exp(self.layers[1].a) / np.sum(np.exp(self.layers[1].a), axis=1, keepdims=True)))
        dW1 = np.dot(X_train.T, delta2)
        db1 = np.sum(delta2, axis=0)

        # Add regularization terms (b1 and b2 don't have regularization terms).
        dW2 += self.LAMBDA * self.layers[2].W
        dW1 += self.LAMBDA * self.layers[1].W

        # Gradient descent parameter update
        self.layers[1].W += -self.ALPHA * dW1
        self.layers[1].b += -self.ALPHA * db1
        self.layers[2].W += -self.ALPHA * dW2
        self.layers[2].b += -self.ALPHA * db2

        return None

    def loss(self, labels: np.ndarray) -> None:
        data_loss = np.sum(-np.log(self.layers[2].a[range(self.layers[2].a.shape[0]), labels]))

        # Add regulatization term to loss (optional)
        data_loss += (self.LAMBDA / 2) \
                     * \
                     (np.sum(np.square(self.layers[1].W)) + np.sum(np.square(self.layers[2].W)))

        return 1. / self.layers[2].a.shape[0] * data_loss

    def predict(self, instance: np.ndarray) -> float:
        return np.argmax(self.forward(instance), axis=1)
