# -*- coding: utf-8 -*-

""""
ProjectName: mail-ws
Repo: https://github.com/chrisenytc/mail-ws
Copyright (c) 2014 Christopher EnyTC
Licensed under the MIT license.
"""

# Dependencies
import unittest


class TestmailWS(unittest.TestCase):

    def setUp(self):
        self.test = "Welcome to mailWS"

    def test_returns_a_hello_world(self):
        self.assertEqual(self.test, 'Welcome to mailWS')

if __name__ == '__main__':
    unittest.main()
