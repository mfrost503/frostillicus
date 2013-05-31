#! /usr/bin/env python

import sys
import socket
import string
import time
import random
import urlparse
from sports.mlb import Mlb
from frostillicus import frostillicus

bot = frostillicus.frostillicus()
s = bot.connect()
NICK=bot.getNick()
CHAN=bot.getChannel()
readbuffer = ""
greetings = ['hey','hello','yo','whaddup',"what's crackin"]
while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer,"\n")
    readbuffer=temp.pop()
    for line in temp:
        print temp
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
        if(len(line) > 3 and line[3] == ":!mlb" and line[4] != ""):
            m = Mlb()
            score = m.getRecentGame(line[4])
            if(score != ""):
                s.sendall("PRIVMSG %s :%s\r\n" % (CHAN,score))
            
