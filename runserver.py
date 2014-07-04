#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""
ProjectName: mail-ws
Repo: https://github.com/chrisenytc/mail-ws
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
import os
from api import app

# Start mailWS
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 22792))
    app.run('0.0.0.0', port=port)
