#!/usr/bin/env python

import unittest
from frostillicus import response
from mock import MagicMock
import pprint

class ResponseTest(unittest.TestCase):
    resp = None

    def setUp(self):
        self.resp = response.Response()
        self.resp.clearList()

    def tearDown(self):
        del self.resp

    def test_AddResponses(self):
	self.resp.addResponse('hi')
	self.resp.addResponse('hello')
	responses = self.resp.getResponses()
	self.assertEqual(responses[0], 'hi')
	self.assertEqual(responses[1], 'hello')

    def test_getRandomResponse(self):
        self.resp.addResponse('hi')
        self.resp.addResponse('hello')
        self.resp.addResponse('howdy')
        response_list = ['hi', 'hello', 'howdy']
        random = self.resp.getRandomResponse()
        self.assertTrue(random in response_list)

    def test_checkResponse(self):
        self.resp.addResponse('hi')
        self.resp.addResponse('hello')
        self.resp.addResponse('hey')
        line = 'mfrost503!~mfrost503@cpe-173-88-210-64.neo.res.rr.com PRIVMSG #dayly :frostillicus: hey'
        self.assertTrue(self.resp.isResponse(line))

    def test_checkResponseFailed(self):
        self.resp.addResponse('hi')
        line = 'mfrost503!~mfrost503@cpe-173-88-210-64.neo.res.rr.com PRIVMSG #dayly :frostillicus: hello'
        self.assertFalse(self.resp.isResponse(line))

if __name__ == '__main__':
    unittest.main()
