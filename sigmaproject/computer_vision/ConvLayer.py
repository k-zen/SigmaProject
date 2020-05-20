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

from .Convolution import Convolution


class ConvLayer(object):
    """
    Class for mimicking a convolutional layer in a neural net. This class is mainly for testing purposes.
    """
    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """

    def __init__(self):
        pass

    def conv_layer(self,
                   input: np.array,
                   kernel: np.array,
                   padding: int) -> np.array:
        """
        Mockup of a convolutional layer in a neural net.

        :param input: The input. Can be an image or the output of a previous convolutional layer.
        :param kernel: The filters to apply to this layer. Is in the shape of: (# of filters, w, h, channels).
        :param padding: The padding to apply.

        :return: The feature map.
        """
        # Hyper-parameters.
        stride: int = 1

        # Temporary image with padding.
        tmp_image = np.zeros((input.shape[0] + 2 * padding, input.shape[1] + 2 * padding, input.shape[2]))

        # Go through all channels from input image, add padding and image to *tmp_image*.
        for c in range(input.shape[2]):
            tmp_image[:, :, c] = np.pad(input[:, :, c], (padding, padding), mode='constant', constant_values=0)

        w = int(((input.shape[0] - kernel.shape[1] + 2 * padding) / stride) + 1)
        h = int(((input.shape[1] - kernel.shape[2] + 2 * padding) / stride) + 1)

        # Creating zero valued array for output feature maps
        feature_maps = np.zeros((w, h, kernel.shape[0]))

        # Convolve each filter.
        for i in range(kernel.shape[0]):
            feature_map = np.zeros((w, h))

            # Convolve for every channel of the image.
            for j in range(input.shape[-1]):
                # Add all channels of the image into ONE feature map.
                feature_map += Convolution.convolution2d(tmp_image[:, :, j], kernel[i, :, :, :], padding, False)

                # Writing results into current output feature map
                feature_maps[:, :, i] = feature_map

        return feature_maps
