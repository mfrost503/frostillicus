#! /usr/bin/env python

import sys
import socket
import string
import time
import random

HOST = "irc.freenode.net"
PORT = 6667
NICK = "frostillicus"
IDENT = "frostillicus"
REALNAME = "frostillicus"
CHAN = "#dayly"
readbuffer = ""
s = socket.socket()
s.connect((HOST, PORT))
s.sendall("NICK %s\r\n" % NICK)
s.sendall("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
s.sendall("JOIN :%s\r\n" % CHAN)
s.sendall("NOTICE %s :%s\r\n" % (CHAN, "Hello There!"))
s.sendall("PRIVMSG %s :%s\r\n" % (CHAN, "I am a bot"))
greetings = ['hey','hello','yo','whaddup',"what's crackin"]
while 1:
    readbuffer=readbuffer+s.recv(1024)
    print readbuffer
    temp=string.split(readbuffer,"\n")
    readbuffer=temp.pop()
    for line in temp:
        line=string.rstrip(line)
        line=string.split(line)
        if(line[0] == "PING"):
            s.sendall("PONG %s\r\n" % line[1])
            print "PONG %s\r\n" % line[1]    
        if(len(line) > 3 and line[1] == "PRIVMSG" and NICK in line[3]) :
            user = line[0]
            username = string.split(user,'!')
            sender = string.lstrip(username[0],':')
            msg = sender
            msg += ': ' 
            msg += random.choice(greetings)
            for i in range(4,len(line)) :
                if(line[i] in greetings) :
                    s.sendall("PRIVMSG %s :%s\r\n" % (CHAN,msg)) 

