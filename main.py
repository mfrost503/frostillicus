#! /usr/bin/env python

import sys
import socket
import string
import time
import random
import urlparse
from sports.mlb import Mlb
from frostillicus import frostillicus
from frostillicus import interaction
from frostillicus import pong

bot = frostillicus.frostillicus()
s = bot.connect()
NICK=bot.getNick()
CHAN=bot.getChannel()
readbuffer = ""
#### Move greetings/funnies to separate class/config
greetings = ['hey','hello','yo','whaddup',"what's crackin"]
funnies = {"whoisyourdaddy?":"mfrost503","andwhatdoeshedo":"writes lame IRC bots","whatisbestinlife?":"To crush your enemies, see them driven before you and to hear the lamentation of their women"}
pong = pong.pong(s)
while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer,"\n")
    readbuffer=temp.pop()
    for line in temp:
        print temp
	pong.checkPing(temp)
	botInteraction = interaction.interaction(line, NICK, greetings)
	if(botInteraction.isInteraction() == True): 
	    s.sendall("PRIVMSG %s :%s\r\n" % (CHAN,botInteraction.getResponse()))
        if(len(line) == 4 and line[3] == ":!mlb"):
	    response = "Not sure what you're asking for"
	    s.sendall("PRIVMSG %s :%s\r\n" % (CHAN,response))
        if(len(line) > 4 and line[3] == ":!mlb"):
            m = Mlb()
            score = m.getRecentGame(line[4])
            if(score != ""):
                s.sendall("PRIVMSG %s :%s\r\n" % (CHAN,score))
            
