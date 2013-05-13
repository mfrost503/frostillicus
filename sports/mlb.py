#!/usr/bin/env python
import httplib2

import json
import pprint

class Mlb(object):
    player_id = 1

    def getRecentGame(self,team):
        h = httplib2.Http()
        resp, content = h.request("http://sports.espn.go.com/mlb/bottomline/scores")
        if(resp.status == 200):
            print content
