import urllib   
import requests  
import re 

def search_match(date):
	regex1 = r"\"TEAM_ABBREVIATION\"\:\".+?\""
	regex2 = r"\"TEAM_ABBREVIATION\"\:\""		#regular expression
	url = 'https://stats.nba.com/scores/'+date  #the website which shows the matchs of 'date'
	html = requests.get(url).text 
	info = re.findall(regex1,html)
	if len(info) == 0 :		#there is no contenu in info
		print("There is not match this day.")
	else :				#info isn't empty, so there is match in this day
		for i in range(0,int(len(info)/2)):
			print(re.sub('\"','',re.sub(regex2,'',info[2*i]))+" VS "+re.sub('\"','',re.sub(regex2,'',info[2*i+1]))) #with the form "team1 VS team2"

