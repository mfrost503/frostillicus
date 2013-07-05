#!/usr/bin/env python

class action:
    actions = ();
    def __init__(self, actions, socket):
        self.actions = actions
        self.socket = socket

    def isAction(self, ircEntry):
        for i in self.actions:
	    if self.actions[i].isAction(ircEntry):
	        return self.actions[i].getResponse()  
	return ''

    def respondToAction(self):
        actionResponse = self.isAction()
	if actionReponse not "":
	    msg = actionResponse
	    self.socket.sendall(msg)
