# -*- coding: utf-8 -*-

""""
ProjectName: mail-ws
Repo: https://github.com/chrisenytc/mail-ws
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
import threading
from api import app, mail
from flask import request, redirect, url_for, copy_current_request_context
from flask import jsonify as JSON
from flask_mail import Message
from cors import cors


@app.route('/')
@cors(origin='*', methods=['GET'])
def index():
    return JSON(welcome='Welcome to mailWS')


@app.route('/', methods=['POST'])
def mail_sender():

    msg = Message('New message', recipients=[request.form['email']])

    msg.html = """
    <h2>Hi, %s <%s></h2>
    <p>Message content</p>
    """ % (request.form['name'], request.form['email'])

    @copy_current_request_context
    def send_message(message):
        mail.send(message)

    sender = threading.Thread(
        name='mail_signup_sender', target=send_message, args=(msg,))
    sender.start()
    # Returns a response
    return redirect('http://example.com/')


@app.route('/status')
@cors(origin='*')
def status():
    return JSON(apiStatus=True, storageStatus=True)
