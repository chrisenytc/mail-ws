# -*- coding: utf-8 -*-

""""
ProjectName: mail-ws
Repo: https://github.com/chrisenytc/mail-ws
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

import os


class Development():
    API = {
        'name': 'mailWS - Development',
        'description': 'An simple implementation of a mail web service',
        'version': 'v1',
        'debug': True,
        'documentation_url': ''
    }
    MAIL = {
        'email': os.environ.get('MAIL_EMAIL', ''),
        'password': os.environ.get('MAIL_PASSWORD', '')
    }
    ERRORS = {
        '500': 'Internal Server Error',
        '503': 'Service Unavailable',
        '400': 'Bad Request',
        '401': 'Bad Authentication. You do not have permission to access the API',
        '404': 'Not Found'
    }
