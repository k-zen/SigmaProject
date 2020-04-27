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

from IPython import get_ipython
from IPython.core.interactiveshell import InteractiveShell
from IPython.display import set_matplotlib_formats

#
# Run magic commands.
#
get_ipython().run_line_magic("matplotlib", "inline")
# Enable autoreload for some modules.
# See: https://ipython.org/ipython-doc/3/config/extensions/autoreload.html
get_ipython().run_line_magic("load_ext", "autoreload")
get_ipython().run_line_magic("autoreload", "2")

#
# IPython configs.
#
InteractiveShell.ast_node_interactivity = 'all'
set_matplotlib_formats('svg')

#
# General imports.
#
import cv2 as cv
import datetime
import h5py as h5
import json
import matplotlib.animation as ani
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import requests as rq
import scipy.stats as ss
import seaborn as sbn

from ast import literal_eval
from colorama import Back, Style
from datetime import datetime
from io import StringIO
from mpl_toolkits import mplot3d
from scipy.io import arff
from sklearn.linear_model import LogisticRegressionCV
from sklearn.neighbors import BallTree

#
# Specific imports from within the main project.
#
# Add specific paths.
# sys.path.append(
#     os.path.join(
#         os.path.dirname(os.path.abspath('')),
#         '../../'
#     )
# )
from sigmaproject.data.Data import Data
from sigmaproject.plotting.Plotting import Plotting
from sigmaproject.neural_net.ActivationFunction import ActivationFunction
from sigmaproject.neural_net.ActivationFunction import ActivationFunctionType
from sigmaproject.neural_net.Layer import Layer
from sigmaproject.neural_net.Layer import LayerType
from sigmaproject.neural_net.Network import Network

#
# Output.
#
print("")
print("All modules have been imported correctly.")
print("")