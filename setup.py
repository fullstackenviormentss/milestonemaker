#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2015-2017 Lionheart Software LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import runpy

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

metadata = runpy.run_path("statictastic/metadata.py")

setup(
    name='milestonemaker',
    version=metadata['__version__'],
    license=metadata['__license__'],
    description="Create milestones in GitHub automatically",
    author=metadata['__author__'],
    author_email=metadata['__email__'],
    url="http://lionheartsw.com/",
    packages=[
        'milestonemaker',
    ],
    scripts=[
        'bin/milestonemaker',
    ],
)

