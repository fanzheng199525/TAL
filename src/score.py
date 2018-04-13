import urllib   
import requests  
import re 

def search_score(team1,team2,date):
	regex1 = r"{\"GAME_DATE_EST\"\:.+?\"FG_PCT\""
	url = 'http://stats.nba.com/scores/'+date
	html = requests.get(url).text 
	# team = input("Which team:")
	matchs = re.findall(regex1,html)

	score1 = str
	score2 = str
	print(matchs)
	for match in matchs:
		dates = match.split('\"')
		if team1 == dates[15]:
			score1 = dates[58]
			score1 = score1[1:-1]
		if team2 == dates[15]:
			score2 = dates[58]
			score2 = score2[1:-1]
	print(team1,score1,team2,score2)

 

