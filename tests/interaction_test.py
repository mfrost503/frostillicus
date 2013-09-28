#!/usr/bin/env python

import unittest
import mock
from mock import MagicMock
import string
import random
from frostillicus import interaction

class InteractionTest(unittest.TestCase):

    def setUp(self):
        self.greetings = ['hello', 'hi', 'howdy', 'whaddup', 'yo']
	self.nick = "frostillicus"
        self.randomMock = MagicMock(name='random', spec=random) 

    def test_InteractionShouldReturnTrue(self):
        raw_line = ':mfrost503!~mfrost503@cpe-173-88-210-64.neo.res.rr.com PRIVMSG #dayly :frostillicus: yo\r'  
        line = string.rstrip(raw_line)
	line = string.split(line)
        int = interaction.interaction(line, self.nick, self.greetings)
	self.assertTrue(int.isInteraction())

    def test_NonInteractionShouldReturnFalse(self):
        raw_line = ':mfrost503!~mfrost503@cpe-173-88-210-64.neo.res.rr.com PRIVMSG #dayly :hello'
	line = string.rstrip(raw_line)
	line = string.split(line)
	int = interaction.interaction(line, self.nick, self.greetings)
	self.assertFalse(int.isInteraction())

    def test_GetSender(self):
        raw_line = ':mfrost503!~mfrost503@cpe-173-88-210-64.neo.res.rr.com PRIVMSG #dayly :hello'
	line = string.rstrip(raw_line)
	line = string.split(line)
	int = interaction.interaction(line, self.nick, self.greetings)
	self.assertEqual('mfrost503', int.getSender())

    def test_GetResponseToInteraction(self):
        raw_line = ':mfrost503!~mfrost503@cpe-173-88-210-64.neo.res.rr.com PRIVMSG #dayly :frostillicus: yo\r'  
	line = string.rstrip(raw_line)
	line = string.split(line)
        int = interaction.interaction(line, self.nick, self.greetings)
	key = 'mfrost503:'
	actual = int.getResponse()
	self.assertTrue(key in actual)

if __name__ == '__main__':
    unittest.main()
