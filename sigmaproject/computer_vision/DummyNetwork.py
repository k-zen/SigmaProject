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

import matplotlib.pyplot as plt
import numpy as np

from .Activations import Activations
from .ConvLayer import ConvLayer
from .PoolingLayer import PoolingLayer
from .Utilities import Utilities


class DummyNetwork(object):
    """
    Class for mimicking a CNN. This class is mainly for testing purposes.
    """
    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """

    def __init__(self, layers: [], kernels: np.array):
        self.layers = layers
        self.kernels = kernels
        self.out = None

    def conv_layer_forward(self,
                           input_img: np.array,
                           padding: int,
                           plot: bool = True) -> None:
        # Plot the result.
        n_rows = self.kernels.shape[0]
        widths = []
        heights = []
        for k in range(1 + len(self.layers)):
            widths.append(4) if k == 0 else widths.append(1)
        for k in range(n_rows):
            heights.append(1)
        fig = plt.figure(figsize=(14, 8))
        gs = fig.add_gridspec(n_rows, 1 + len(self.layers), width_ratios=widths, height_ratios=heights)
        axes = [fig.add_subplot(gs[:, 0])]
        for i in range(len(self.layers)):
            sub_axis = []
            for j in range(n_rows):
                sub_axis.append(fig.add_subplot(gs[j, i + 1]))
            axes.append(sub_axis)

        if plot:
            # Plot the original image.
            _ = axes[0].imshow(input_img, aspect='equal')

        for index, layer in enumerate(self.layers):
            if isinstance(layer, ConvLayer):
                self.out = layer.conv_layer(input=(input_img if index == 0 else self.out),
                                            kernel=self.kernels,
                                            padding=padding)
                # Normalize in 3D.
                self.out = Utilities.normalize_pixels3d(self.out)
                print('Shape of Convolutional Layer: {}'.format(self.out.shape))
                if plot:
                    _ = axes[index + 1][0].set_title('Conv'.format(index + 1))
            if isinstance(layer, Activations):
                self.out = Activations.relu(self.out)
                print('Shape of ReLU Activations: {}'.format(self.out.shape))
                if plot:
                    _ = axes[index + 1][0].set_title('ReLU'.format(index + 1))
            if isinstance(layer, PoolingLayer):
                self.out = layer.pooling_layer(input=self.out, padding=2, stride=2)
                print('Shape of Pooling Layer: {}'.format(self.out.shape))
                if plot:
                    _ = axes[index + 1][0].set_title('Pooling'.format(index + 1))
            if plot:
                for i in range(n_rows):
                    _ = axes[index + 1][i].imshow(self.out[:, :, i], aspect='equal', cmap='Greys_r')
                    _ = axes[index + 1][i].set_axis_off()
