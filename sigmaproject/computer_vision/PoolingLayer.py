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


class PoolingLayer(object):
    """
    Class for mimicking a pooling layer in a neural net. This class is mainly for testing purposes.
    """
    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """

    def __init__(self):
        pass

    def pooling_layer(self,
                      input: np.array,
                      padding: int,
                      stride: int) -> np.array:
        """
        Mockup of a pooling layer in a neural net.

        :param input: The input. Can be an image or the output of a previous convolutional layer.
        :param padding: The padding to apply.
        :param stride: The stride.

        :return: The feature map.
        """
        w = int(((input.shape[0] - padding) / stride) + 1)
        h = int(((input.shape[1] - padding) / stride) + 1)

        out = np.zeros((w, h, input.shape[-1]))

        # Implementing pooling operation for all channels.
        for c in range(input.shape[-1]):
            ii = 0
            for i in range(0, input.shape[0] - padding + 1, stride):
                jj = 0
                for j in range(0, input.shape[1] - padding + 1, stride):
                    # Extracting patch (the same size with filter) from input image.
                    patch_from_image = input[i:i + padding, j:j + padding, c]
                    # Applying max pooling operation - choosing maximum element from the current patch
                    out[ii, jj, c] = np.max(patch_from_image)
                    # Increasing indexing for polling array
                    jj += 1
                # Increasing indexing for polling array
                ii += 1

        return out
