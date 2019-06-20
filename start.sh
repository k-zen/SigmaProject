#!/usr/bin/env bash

################################################################
# Edited by K-Zen on 2019.06.20.                               #
# Script to start a custom Python version and a custom virtual #
# environment.                                                 #
#                                                              #
# @author: Andreas P. Koenzen <akoenzen@uvic.ca>               #
# @date: 2019.06.20                                            #
#                                                              #
# Execution command: $ source start.sh                         #
#                                                              #
# Note: Must be executed using the source command              #
# to allow all other commands to execute in the current        #
# shell instead of a sub-shell.                                #
# See: https://askubuntu.com/questions/965475/                 #
#      cannot-activate-virtual-environment-with-a-shell-script #
################################################################
PYTHON_VERSION="3.6.6"

export PYENV_VERSION=${PYTHON_VERSION}

eval "$(pyenv init -)" # Important for "pyenv shell" command to work.
eval "$(pyenv shell -)"
eval "source venv-${PYTHON_VERSION}/bin/activate"
eval "clear"

eval "git status"
