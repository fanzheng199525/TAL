import urllib   
import requests  
import re 

def search_score(team1,team2,date):
	regex1 = r"{\"GAME_DATE_EST\"\:.+?\"FG_PCT\""
	url = 'http://stats.nba.com/scores/'+date
	html = requests.get(url).text 
	matchs = re.findall(regex1,html)

	score1 = str
	score2 = str
	for match in matchs:	#verify if the team that we search for is in matchs
		dates = match.split('\"')
		if team1 == dates[15]:
			score1 = dates[58]
			score1 = score1[1:-1]
		if team2 == dates[15]:
			score2 = dates[58]
			score2 = score2[1:-1]
	if score1==str or score2==str:
		print("\n Sorry, there is no match on that day.")
	else:
		print(team1,score1,team2,score2)

 

