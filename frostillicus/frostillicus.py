#!/usr/bin/env python

from socket import socket
class frostillicus(object):
    HOST = "irc.freenode.net"
    PORT = 6667
    IDENT = "frostillicus"
    NICK = "frostillicus"
    REALNAME = "frostillicus"
    CHAN = "#phpmentoring"
   
    def connect(self,host=""):
        s = socket()
        s.connect((self.HOST, self.PORT))
        self.identify(s)
        self.joinChannel(s,self.CHAN)
        return s 
    def identify(self, socket):
        socket.sendall("NICK %s\r\n" % self.NICK)
        socket.sendall("USER %s %s bla :%s\r\n" % (self.IDENT,self.HOST,self.REALNAME))

    def joinChannel(self, socket,channel):
        socket.sendall("JOIN :%s\r\n" % channel)
    def getNick(self):
        return self.NICK 
    def getChannel(self):
        return self.CHAN
