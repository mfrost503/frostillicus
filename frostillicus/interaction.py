#!/usr/bin/env python

import string
import random

class interaction() :
    def __init__(self, line, nick, greetings):
        self.line = line
        self.nick = nick
        self.greetings = greetings
        self.reactions = ['hmmm', 'you don\'t say', 'very interesting']

    def isInteraction(self) :
        line = self.line
        if(len(line) > 3 and self.nick in line[3] and line[1] == "PRIVMSG") :
            return True
        return False

    def getResponse(self):
        sender = self.getSender() 
        msg = sender + ": " + random.choice(self.reactions)
        if(self.isInteraction() == True):
            for x in range(4,len(self.line)) :
                if(self.isGreeting(self.line[x])):
                    msg = sender + ': ' + random.choice(self.greetings)
        return msg

    def getSender(self):
        user = self.line[0]
        username = string.split(user, '!')
        sender = string.lstrip(username[0], ':')
        return sender

    def isGreeting(self, word) :
        if(word in self.greetings) :
            return True
        return False


    
