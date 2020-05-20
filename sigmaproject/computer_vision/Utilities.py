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

import cv2
import numpy as np
import urllib3


class Utilities(object):
    """
    Utility class for computer vision.
    """

    DEBUG = False
    """
    boolean: Flag to enable debug mode.
    """

    def __init__(self):
        pass

    @staticmethod
    def read_image(url: str) -> None:
        """
        Reads an image from a URL.

        :param url: The URL of the image.

        :returns: The decoded image as BGR.
        """
        req = urllib3.PoolManager().request('GET', url)
        arr = np.asarray(bytearray(req.data), dtype=np.uint8)

        return cv2.imdecode(arr, cv2.IMREAD_COLOR)

    @staticmethod
    def normalize_pixels(img: np.array) -> np.array:
        out = np.zeros(img.shape)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                out[i, j] = img[i, j] if 0 <= img[i, j] <= 255 else (0 if img[i, j] < 0 else 255)

        return out

    @staticmethod
    def normalize_pixels3d(img: np.array) -> np.array:
        out = np.zeros(img.shape)
        for c in range(img.shape[2]):
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    out[i, j, c] = img[i, j, c] if img[i, j, c] <= 255 else 255

        return out
