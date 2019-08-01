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

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


class Plotting(object):
    """
    Plotting utilities. This class represents only one graph (axis) where different plots can
    overlap.
    """

    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """

    def __init__(self):
        self.fig = plt.figure(figsize=(10.0, 8.0))
        self.axis = self.fig.gca()

    def scatter(self, x: np.ndarray, y: np.ndarray) -> None:
        """
        Scatter plot wrapper function.

        :param x: Points to plot. X will be at least 2 columns.
        :param y: Labels for points.

        :returns: Void
        """
        self.axis.scatter(x[:, 0],
                          x[:, 1],
                          s=30,
                          c=y,
                          marker='o',
                          cmap=mpl.colors.ListedColormap(['red', 'blue']))

        self.axis.grid(True)
        plt.box(on=None)

        return None

    def decision_boundary(self, x, z_func, h: float = 0.01) -> None:
        """
        Plots a decision boundary using a contour plot.

        :param x: Points to plot. This will be used mostly to know the size of the contour.
        :param z_func: The function used to calculate the z-axis value.
        :param h: The separation of points in the meshgrid used to calculate the contour.

        :returns: Void
        """
        # Set min and max values and give it some padding.
        x_min, x_max = x[:, 0].min() - .5, x[:, 0].max() + .5
        y_min, y_max = x[:, 1].min() - .5, x[:, 1].max() + .5

        # Generate a grid of points with distance h between them.
        xx, yy = np.meshgrid(
            np.arange(x_min, x_max, h),
            np.arange(y_min, y_max, h)
        )

        # Predict the function value for the whole gid.
        z = z_func(np.c_[xx.ravel(), yy.ravel()])
        z = z.reshape(xx.shape)

        # Plot the contour and training examples
        self.axis.contourf(xx,
                           yy,
                           z,
                           cmap=mpl.colors.ListedColormap(['#D0E0EB', '#EBF7F8']))

        self.axis.grid(True)
        plt.box(on=None)

        return None

    def loss(self, loss: [float]) -> None:
        self.axis.plot(loss)
        self.axis.set_xlabel("Epoch", fontsize=14)
        self.axis.set_ylabel("Loss", fontsize=14)

        self.axis.grid(True)
        plt.box(on=None)

        return None
