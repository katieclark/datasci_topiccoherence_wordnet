#!/usr/bin/python -*- coding: utf-8 -*-
#
# Merlin - Almost Pure Python Machine Learning Library
#
# Copyright (C) 2014-2015 alvations
# URL:
# For license information, see LICENSE.md

"""
Merlin is a simple machine learning library, largely derived from LXMLS-toolkit
from https://github.com/LxMLS/lxmls-toolkit

This is to support python libraries that wants to rely on minimal dependencies.
"""

import linear_classifier
from mira import Mira
from naive_bayes import NaiveBayes
from perceptron import Perceptron
from svm import SVM

from pyswd.merlin.simple_data_set import SimpleDataSet