#!/usr/bin/env python

import string
import random

class pong():
    def __init__(self,socket):
        self.socket = socket
    def checkPing(self,line):
	if(type(line) is not list):
	    return 0
	lineText = line[0]
        components = string.rstrip(lineText)
	components = string.split(lineText)
	if(components[0] == "PING"):
	    self.socket.sendall("PONG %s\r\n" % components[1])
