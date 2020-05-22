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

from sklearn import *


class Data(object):
    """
    Utility class to generate data sets.
    """

    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """

    def __init__(self):
        self.data = None

    def generate_data(self, type: int = 0) -> None:
        """
        Generate data to train the network.

        :param type: The type of data to generate.

        :returns: Void
        """
        if type == 0:
            self.data = datasets.make_moons(
                n_samples=200,
                shuffle=True,
                noise=0.2,
                random_state=42
            )
        elif type == 1:
            self.data = datasets.make_circles(
                n_samples=200,
                shuffle=True,
                noise=0.2,
                factor=0.5,
                random_state=1
            )
        elif type == 2:
            rng = np.random.RandomState(0)
            x = rng.randn(200, 2)
            y = np.logical_xor(x[:, 0] > 0, x[:, 1] > 0).astype(int)
            self.data = (x, y)

        return None
