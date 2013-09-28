#!/usr/bin/env python

import random

class Response():
    
    responses = []

    def addResponse(self, response):
        self.responses.append(response)

    def getResponses(self):
        return self.responses

    def getRandomResponse(self):
        return random.choice(self.responses)

    def isResponse(self, line):
        for response in self.responses:
            if response in line and "frostillicus:" in line and "PRIVMSG" in line:
                return True
        return False

    def clearList(self):
        self.responses = []
