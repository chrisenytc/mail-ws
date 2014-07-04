# -*- coding: utf-8 -*-

""""
ProjectName: mail-ws
Repo: https://github.com/chrisenytc/mail-ws
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# version
__version__ = '0.1.0'

# Dependencies
import os
from api.config.development import Development
from api.config.production import Production
from api.config.test import Test
from api.errors.invalid_request import InvalidRequest
from flask import Flask
from flask_mail import Mail
from flask import jsonify as JSON

# Start Flesk
app = Flask('mail-ws')

# Configs
env = os.environ.get('PY_ENV', 'development')

if env == 'development':
    app.config.from_object(Development)
elif env == 'production':
    app.config.from_object(Production)
elif env == 'test':
    app.config.from_object(Test)
else:
    print 'Environment not found'

# Debug mode
app.debug = app.config['API']['debug']

app.config.update(
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=app.config['MAIL']['email'],
    MAIL_PASSWORD=app.config['MAIL']['password'],
    MAIL_DEFAULT_SENDER='Liv <%s>' % app.config['MAIL']['email']
)

# Start MailApp
mail = Mail(app)


@app.errorhandler(Exception)
def handle_all_errors(error):
    try:
        response = JSON(error=error.to_dict().get('__all__'))
    except Exception:
        response = JSON(error=str(error))

    response.status_code = 500
    return response


@app.errorhandler(InvalidRequest)
def handle_invalid_request(error):
    response = JSON(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(500)
def internal_server_error(error):
    response = JSON(error=str(app.config['ERRORS']['500']))
    response.status_code = 500
    return response


@app.errorhandler(503)
def service_unavailable_error(error):
    response = JSON(error=str(app.config['ERRORS']['503']))
    response.status_code = 503
    return response


@app.errorhandler(400)
def bad_request(error):
    response = JSON(error=str(app.config['ERRORS']['400']))
    response.status_code = 400
    return response


@app.errorhandler(401)
def unauthorized(error):
    response = JSON(error=str(app.config['ERRORS']['401']))
    response.status_code = 401
    return response


@app.errorhandler(404)
def page_not_found(error):
    response = JSON(error=str(app.config['ERRORS']['404']))
    response.status_code = 404
    return response


# Import
from api.controllers import *
