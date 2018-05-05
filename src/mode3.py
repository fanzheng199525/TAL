import nltk
import datetime
import re
import nmt_mode
import os
import global_init
import mode1
from nba_search.score import search_score
from nba_search.match import search_match
from nba_search.player import search_info_player
from nba_search.team import search_info_team
from nba_search.playerinit import init_player

TEAMCHANNELS= {"PHO":"Phoenix Suns","SAS":"San Antonio Spurs","DAL":"Dallas Mavericks","SAC":"Sacramento Kings","HOU":"Houston Rockets",
"MEM":"Memphis Grizzlies","LAL":"L.A. Lakers","MIN":"Minnesota Timberwolves","DEN":"Denver Nuggets","LAC":"L.A. Clippers",
"POR":"Portland Trail Blazers","UTA":"Utah Jazz","GSW":"Golden State Warriors","NOP":"New Orleans Pelicans","MIA":"Miami Heat",
"DET":"Detroit Pistons","BOS":"Boston Celtics","CLE":"Cleveland Cavaliers","WAS":"Washington Wizards","ORL":"Orlando Magic",
"CHI":"Chicago Bulls","PHI":"Philadelphia 76ers","IND":"Indiana Pacers","MIL":"Milwaukee Bucks","BKN":"Brooklyn Nets",
"NYN":"New York Knicks","TOR":"Toronto Raptors","CHA":"Charlotte Hornets","ATL":"Atlanta Hawks","OCT":"Oklahoma City Thunder"}
SCORECHANNELS = ["score","point","grade","result"]
PLAYERCHANNELS = {}
INFOCHANNELS = ["information","info","something"]
MATCHCHANNELS = ["matches","games","competitions","tournaments","match","game","competition","tournament"]
DAYCHANNELS = ["yesterday","tomorrow","today"]
TEAM = ''
PLAYER =''


def seg(sentence):
	tokens = nltk.word_tokenize(sentence)
	segments = nltk.pos_tag(tokens)
	return segments

def when(day, date):
	if day!='':
		if day == "yesterday":
			date = datetime.date.today() - datetime.timedelta(days=1)
		elif day == "tomorrow":
			date = datetime.date.today() + datetime.timedelta(days=1)
		else:
			date = datetime.date.today()
		date = date.strftime("%m/%d/%Y")
		return date
	return date
	
def find_team(n):
	global TEAM
	com = re.compile(n,re.I)
	for key,contain in TEAMCHANNELS.items():
		if com.search(contain):
			TEAM = key
			return True
	return False

def find_player(n):
	global PLAYER
	player = []
	com = re.compile(n,re.I)
	for contain in PLAYERCHANNELS:
		if com.search(contain):
			player.append(contain)
	if len(player)==1:
		PLAYER = player[0]
		return True
	elif len(player)>1:
		print("There are ",len(player),"players who have the same name")
		for i in range(len(player)):
			print(i,": ",player[i])
		PLAYER = player[int(input("which one you wanna choose(give me the number)"))]	
		return True				
	return False

	
def handle(sentence):
	segments = seg(sentence)
	score = False
	info = False
	match =False
	rule = False
	day = ''
	team = []
	player = ''
	noun,prep,adj,date = classify(segments)

	for n in noun:
		if n in SCORECHANNELS:
			score = True
		elif n in TEAMCHANNELS.keys():
			team.append(n)	
		elif find_team(n):
			team.append(TEAM)
		elif n in MATCHCHANNELS:
			match = True
		elif n in INFOCHANNELS:
			info = True
		elif n in PLAYERCHANNELS:
			player = n
		elif find_player(n):
			player = PLAYER
		elif n in DAYCHANNELS:
			day = n
		elif n == "rule":
			rule =True
	date = when(day, date)

	if score==True:
		if len(team)==0:
			print("\nPlease ask me with the teams you want to search~")	
		else:
			if(date==''):
				print(" \nPlease tell me the date\n",
						"->")
				date = input()
			search_score(team[0],team[1],date)
	elif info==True or (match==False and "about" in prep):
		if len(team)!=0:
			search_info_team(TEAMCHANNELS[team[0]])
		else:
			if player=='':
				print("no such player in our system")
			else:
				search_info_player(player)
	elif match==True:
		print(date)
		if(date==''):
			print(" \nPlease tell me the date\n",
						"->")
			date = input()
		else:
			search_match(date)
	elif rule == True:
		print(
		  " The date need to be month/day/year\n",
		  "Attention-- For searching score, we can't offer the result within 2 days because of the strange problem of our search site")
	else:
		if os.path.exists('model/translate.ckpt-81000.data-00000-of-00001'):
			nmt_mode.mode4(sentence)
		else:
			global_init.minus_mode()
			print(mode1.rep())

def classify(segments):
	noun = []
	prep = []
	adj = []
	player=''
	date = ''
	for segment in segments:
		if segment[1]=='NN' or segment[1]=='NNS':
			noun.append(segment[0])
		elif segment[1] == 'NNP':
			if segment[0] not in TEAMCHANNELS.keys():
				player = player+segment[0]+' '
			else:
				noun.append(segment[0])
		elif segment[1]=='IN':
			prep.append(segment[0])
		elif segment[1]=='JJ':
			adj.append(segment[0])
		elif segment[1]=='CD':
			date = segment[0]
			while re.compile(r'^\d{1,2}\/\d{1,2}\/\d{4}').match(date)==None:
				print(" date form  wrong, Please enter the right date:\n",
						"->")
				date = input()			
	if player!='':
		player= player.rstrip()
		noun.append(player)
	return noun,prep,adj,date

def init():
	global PLAYERCHANNELS
	PLAYERCHANNELS = init_player()
	nmt_mode.modeinit()


def mode3(sentence):
	handle(sentence)

	