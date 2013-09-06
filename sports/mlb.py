#!/usr/bin/env python
import httplib2
import datetime
import json

class Mlb(object):
    player_id = 1
    date = datetime.date.today()
    team =''
    data = {}
    def getRecentGame(self,team):
        h = httplib2.Http()
        month = str(self.date.month)
        day = str(self.date.day)
        year = str(self.date.year)
        if(len(month) == 1):
            month = "0" + month
        if(len(day) == 1):
            day = "0" + day
        resp, content = h.request("http://gd2.mlb.com/components/game/mlb/year_"+ year +"/month_"+month+"/day_"+day+"/master_scoreboard.json")
        if(resp.status == 200):
            self.data = json.loads(content)
	    teamNicks = {'same-ol-jays':'blue-jays',
	    	'evil-empire':'yankees',
		'bo-sox':'red-sox',
		'phightins':'phillies',
		'lastros': 'astros',
		'pale-hose':'white-sox',
		'the-birds': 'orioles',
		'wahoos':'indians',
		'twinkies':'twins',
		'the-halos':'angels',
		'the-elephants':'as',
		'ms': 'mariners',
		'blue-crew':'rangers',
		'bravos':'braves',
		'the-fish':'marlins',
		'the-amazins':'mets',
		'nats':'nationals',
		'north-siders':'cubs',
		'cubbies':'cubs',
		'south-siders':'white-sox',
		'big-red-machine':'reds',
		'brew-crew':'brewers',
		'buccos':'pirates',
		'redbirds':'cardinals',
		'dbacks':'d-backs',
		'rox':'rockies',
		'dem-bums':'dodgers',
		'friars':'padres',
		'los-gigantes':'giants'
		}
	    if(team in teamNicks):
	        team = teamNicks[team]
            team = team.replace('-',' ').title()
            self.team = team
            games = self.data['data']['games']['game']
            gameCount = len(games)
            score='No game for the ' + team + ' today'
            for i in range(0,gameCount) :
                if(games[i]['home_team_name'] == team or games[i]['away_team_name'] == team):
                    game = games[i] 
		    print game
                    home_team = game['home_team_name']
                    away_team = game['away_team_name']
                    if(game['status']['status'] != "Preview"):
                        away_score = game['linescore']['r']['away']
                        home_score = game['linescore']['r']['home']
                        score = away_team + " " + away_score + " " + home_team + " " + home_score + " " + game['status']['status']
                    else:
                        score = away_team + "(" + game['away_win'] + "-" + game['away_loss'] + ")@"
                        score += home_team + "(" + game['home_win'] + "-" + game['home_loss'] + ") " + game['time'] + game['home_time_zone'] + " TV: " + game['broadcast']['away']['tv'] + "/" + game['broadcast']['home']['tv']
            return score
        
