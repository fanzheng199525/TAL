import urllib   
import requests  
import re 

def search_info_player(info):
	regex1 = r"\<p\>\<b\>.+?\.\<\/p\>"
	regex2 = r"\<.+?\>"
	regex3 = r"\[.+?\]"
	player = info.split()
	while(len(player) != 2):
	    info = input("Please input the player with the form (firstname lastname):")
	    player = info.split()
	url = 'https://en.wikipedia.org/wiki/'
	html = requests.get(url+player[0]+'_'+player[1]).text 
	info_original = re.findall(regex1,html)
	if len(info_original) == 0:
		print("There is no information")
	else:
	    intro = info_original[0]
	    info_player = re.sub(regex2,'',intro)
	    info_player = re.sub(regex3,'',info_player)
	    print(info_player)

