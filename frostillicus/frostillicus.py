#!/usr/bin/env python

class frostillicus():
    HOST = "irc.freenode.net"
    PORT = 6667
    IDENT = "frostillicus"
    NICK = "frostillicus"
    REALNAME = "frostillicus"
    CHAN = "#dayly"

    def __init__(self, socket, chan="", host=""):
        if chan != "":
            self.CHAN = chan
        if host != "" :
            self.HOST = host
        self.socket = socket

    def connect(self,host=""):
        s = self.socket
        s.connect((self.HOST, self.PORT))
        self.identify()
        self.joinChannel(self.CHAN)
        return s 

    def identify(self):
        self.socket.sendall("NICK %s\r\n" % self.NICK)
        self.socket.sendall("USER %s %s bla :%s\r\n" % (self.IDENT,self.HOST,self.REALNAME))

    def joinChannel(self, channel):
        self.socket.sendall("JOIN :%s\r\n" % channel)
	
    def getNick(self):
        return self.NICK 

    def setNick(self, nick):
        self.NICK = nick

    def getChannel(self):
        return self.CHAN

    def setChannel(self, channel):
        self.CHAN = channel
