# mail-ws
# https://github.com/chrisenytc/mail-ws
#
# Copyright (c) 2014 Christopher EnyTC
# Licensed under the MIT license.


install:
	pip install -r requirements.txt

start:
	@PY_ENV=production python runserver.py

test:
	@PY_ENV=test python test/test_mail_ws.py

.PHONY: install test