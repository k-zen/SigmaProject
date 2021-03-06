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

from .utilities import Utilities
from typing import Dict


class Convolution(object):
    """
    Class for computing convolutions.
    """
    IDENTITY = 1
    EDGES_1 = 2
    EDGES_2 = 3
    EDGES_3 = 4

    KERNELS: Dict[int, np.array] = {
        IDENTITY: np.array([
            [+0, +0, +0],
            [+0, +1, +0],
            [+0, +0, +0]
        ]),
        EDGES_1: np.array([
            [+1, +0, -1],
            [+0, +0, +0],
            [-1, +0, +1]
        ]),
        EDGES_2: np.array([
            [+0, +1, +0],
            [+1, -4, +1],
            [+0, +1, +0]
        ]),
        EDGES_3: np.array([
            [-1, -1, -1],
            [-1, +8, -1],
            [-1, -1, -1]
        ])
    }

    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """

    def __init__(self):
        pass

    @staticmethod
    def convolution2d(img: np.array,
                      kernel: np.array,
                      padding: int,
                      normalize_pixels: bool = True) -> np.array:
        """
        Performs a convolution in 2 dimensions.

        :return: The convolved image.
        """
        stride: int = 1

        # We must calculate the final size of the output image BEFORE adding the padding to the input image!
        w = int(((img.shape[0] - kernel.shape[0] + 2 * padding) / stride) + 1)
        h = int(((img.shape[1] - kernel.shape[1] + 2 * padding) / stride) + 1)

        # Output image.
        out = np.zeros((w - 2 * padding, h - 2 * padding))

        for i in range(0, img.shape[0] - kernel.shape[0] + 1, stride):
            for j in range(0, img.shape[1] - kernel.shape[1] + 1, stride):
                rec_field = img[i: i + kernel.shape[0], j: j + kernel.shape[0]]
                out[i, j] = np.sum(rec_field * kernel)

        return Utilities.normalize_pixels(out) if normalize_pixels else out
