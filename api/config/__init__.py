# -*- coding: utf-8 -*-

""""
ProjectName: mail-ws
Repo: https://github.com/chrisenytc/mail-ws
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
import os
import glob


__all__ = [os.path.basename(
    f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
