import urllib   
import requests  
import re 

def init_player():
	regex1 = r"data-display-answer=\".+?\""
	regex2 = r"data-display-answer=\""
	url = 'https://www.sporcle.com/games/ShakeyDeal/top-100-nba-players-of-the-century-hoopshype/results'
	html = requests.get(url).text 
	player_list = set()
	info = re.findall(regex1,html)

	for i in range(0,len(info)):
			player_list.add(re.sub('\"','',re.sub(regex2,'',info[i]))) #the list from web1
			
	regex3 = r"\.html\"\>.+?\<\/a\>\<\/td\>\<td class\=\"left \""
	regex4 = r"\<\/a\>\<\/td\>\<td class\=\"left \""
	regex5 = r"\.html\"\>"
	url2 = 'https://www.basketball-reference.com/contracts/players.html'   
	html2 = requests.get(url2).text
	info1 = re.findall(regex3,html2)
	for j in range(0,len(info1)):
			player_list.add(re.sub(regex5,'',re.sub(regex4,'',info1[j])))  #the list from web2
	return player_list