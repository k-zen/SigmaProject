#!/usr/bin/env bash

#
#  Copyright (c) 2019, Andreas Koenzen <akoenzen | uvic.ca>
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
#

# ============================================================ #
# Edited by K-Zen on 2020.03.21.                               #
# Script to start a custom Python version and a custom virtual #
# environment.                                                 #
#                                                              #
# @author: Andreas P. Koenzen <akoenzen@uvic.ca>               #
# @date: 2019.06.20                                            #
#                                                              #
# Execution command: $ source start-jupyter.sh                 #
#                                                              #
# Note: Must be executed using the source command              #
# to allow all other commands to execute in the current        #
# shell instead of a sub-shell.                                #
# See: https://askubuntu.com/questions/965475/                 #
#      cannot-activate-virtual-environment-with-a-shell-script #
# ============================================================ #
PYTHON_VERSION="3.6.6"

export PYENV_VERSION=${PYTHON_VERSION}

eval "$(pyenv init -)" # Important for "pyenv shell" command to work.
eval "$(pyenv shell ${PYTHON_VERSION})"
eval "source venv-${PYTHON_VERSION}/bin/activate"
eval "clear"

# Add flag *--watch* to enable development of plugins mode.
eval "jupyter lab notebooks --no-browser"

