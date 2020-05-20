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

from IPython.core.display import HTML
from IPython.display import Javascript, IFrame

_ = HTML(
    "<style>"
    "ol           {counter-reset:item;}"
    "ol li        {display:block;}"
    "ol li:before {content:counter(item) \". \";counter-increment:item;font-weight:bold;}"
    "iframe       {border:0px;}"
    "table        {float:left;}"
    "table th,td  {font-size:100%;}"
    "</style>"
)

_ = plt.style.use(["default"])
_ = plt.rcParams.update(
    {
        'font.size': 8,
        'font.weight': 600,
        'font.family': 'Arial',
        'legend.fontsize': 9,
        'legend.frameon': False,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'figure.figsize': '5.3, 4',
        'axes.grid': True,
        'axes.prop_cycle': 'cycler(\'color\', [\'#23679f\', \'#b5b6d7\'])',
        'grid.color': '#dddddd',
        'grid.linestyle': '--',
        'grid.linewidth': 0.5
    }
)
_ = mpl.rcParams['animation.embed_limit'] = 100
