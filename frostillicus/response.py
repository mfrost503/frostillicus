#!/usr/bin/env python
import string
class response:
    self.msg = ''
    greetings = [
        'hello',
	'hi',
	'whaddup',
	'yo',
	'howdy',
	"how'sitgoin',
	'morning'
    ]
    def isAction(self,ircEntry):
        entryComponents = ircEntry.split(' ')
        self.isPing(entryComponents):

    def isPing(self,entry):
        if entry[0] == "PING"
	    self.msg = "PONG " + entry[1]

    def isGreeting(self,entry):
	nickset = 0
        if entry[1] not "PRIVMSG":
	    return ''
	for i in range(3,len(entry)):
	    item = string.lstrip(entry[i],':')
            if item == nick:
	        nickset = 1
	    if nickset ==1 and item in greetings:
	        
	        

    def getResponse(self):
        return self.msg
	    

