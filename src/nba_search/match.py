import urllib   
import requests  
import re 

def search_match(date):
	regex1 = r"\"TEAM_ABBREVIATION\"\:\".+?\""
	regex2 = r"\"TEAM_ABBREVIATION\"\:\""
	url = 'https://stats.nba.com/scores/'+date
	html = requests.get(url).text 
	info = re.findall(regex1,html)
	if len(info) == 0 :
		print("There is not match this day.")
	else :
		for i in range(0,int(len(info)/2)):
			print(re.sub('\"','',re.sub(regex2,'',info[2*i]))+" VS "+re.sub('\"','',re.sub(regex2,'',info[2*i+1])))
	# intro = info_original[0]
	# information = re.findall(regex2,intro)
	# info_team = re.sub(regex2,'',intro)
	# print(info_team)
