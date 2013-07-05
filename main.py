#! /usr/bin/env python

import sys
import socket
import string
import time
import random
import urlparse
from sports.mlb import Mlb
from frostillicus import frostillicus
from frostillicus import pong

bot = frostillicus.frostillicus()
s = bot.connect()
NICK=bot.getNick()
CHAN=bot.getChannel()
readbuffer = ""
greetings = ['hey','hello','yo','whaddup',"what's crackin"]
funnies = {"whoisyourdaddy?":"mfrost503","andwhatdoeshedo":"writes lame IRC bots"}
pong = pong.pong(s)
while 1:
    readbuffer=readbuffer+s.recv(1024)
    temp=string.split(readbuffer,"\n")
    readbuffer=temp.pop()
    for line in temp:
        print temp
	pong.checkPing(temp)
        line=string.rstrip(line)
        line=string.split(line)
        if(len(line) > 3 and line[1] == "PRIVMSG" and NICK in line[3]) :
            user = line[0]
            username = string.split(user,'!')
            sender = string.lstrip(username[0],':')
            msg = sender
            msg += ': ' 
            msg += random.choice(greetings)
	    question = ""
            for i in range(4,len(line)) :
	        question += line[i] 
                if(line[i] in greetings) :
                    s.sendall("PRIVMSG %s :%s\r\n" % (CHAN,msg)) 
		if(question.strip() in funnies):
		    funny = question 
		    response = funnies[funny]
		    s.sendall("PRIVMSG %s :%s\r\n" % (CHAN,response))
        if(len(line) > 3 and line[3] == ":!mlb" and line[4] != ""):
            m = Mlb()
            score = m.getRecentGame(line[4])
            if(score != ""):
                s.sendall("PRIVMSG %s :%s\r\n" % (CHAN,score))
            
