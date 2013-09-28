#!/usr/bin/env python

import unittest
from frostillicus import frostillicus
import socket
from mock import MagicMock
from mock import call

class TestFrostillicus(unittest.TestCase):

    def setUp(self):
        self.nick = "frostillicus"
        self.host = "irc.freenode.net"
        self.port = 6667
        self.channel = "#phpmentoring"
        self.socketMock = MagicMock(name='socket', spec=socket.socket)
        self.bot = frostillicus.frostillicus(self.socketMock, self.channel, self.host)
	
    def test_getChannel(self):
        expected = self.channel
        channel = self.bot.getChannel()
        self.assertEqual(expected, channel)

    def test_getNick(self):
        expected = self.nick
        nick = self.bot.getNick()
        self.assertEqual(expected, nick)

    def test_BotCanConnect(self):
        self.bot.connect(self.host)
        self.socketMock.connect.assert_called_with((self.host, self.port))

    def test_BotCanJoinChannel(self):
        self.bot.joinChannel("#phpmentoring")
        self.socketMock.sendall.assert_called_with("JOIN :%s\r\n" % "#phpmentoring")

    def test_BotCanSetNick(self):
        nick = "frostillicus"
        self.bot.setNick(nick)
        retrieved = self.bot.getNick()
        self.assertEqual(nick, retrieved)

    def test_BotCanSetChannel(self):
        channel = "#testchannel"
        self.bot.setChannel(channel)
        retrieved = self.bot.getChannel()
        self.assertEqual(channel, retrieved)

    def test_BotCanIdentify(self):
        self.bot.identify()
        expected = [call.sendall('NICK frostillicus\r\n'), call.sendall('USER frostillicus irc.freenode.net bla :frostillicus\r\n')]
        self.assertEqual(self.socketMock.mock_calls, expected)

if __name__ == '__main__':
    unittest.main()
