import urllib   
import requests  
import re 

def search_info_team(info):
	regex1 = r"\<p\>.+?<\/p\>"
	regex2 = r"\<.+?\>"
	team = info.split()
	url = 'https://en.wikipedia.org/wiki/'
	html = requests.get(url+team[0]+'_'+team[1]).text 
	info_original = re.findall(regex1,html)
	intro = info_original[0]
	information = re.findall(regex2,intro)
	info_team = re.sub(regex2,'',intro)
	print(info_team)
