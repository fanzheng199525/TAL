import nltk
import datetime
import re
from score import search_score

SCORECHANNELS = ["score","point","grade","result"]
TEAMCHANNELS = ["HOU","LAL","MIA","CHI","SAS","GSW","IND"]
PLAYERCHANNELS = ["Allen Ray","Bryant Kobe","Duncan Tim","Gasol Paul"]
INFOCHANNELS = ["information","info","something"]
MATCHCHANNELS = ["match","game","competition","tournament"]
DAYCHANNELS = ["yesterday","tomorrow"]

def seg(sentence):
	tokens = nltk.word_tokenize(sentence)
	segments = nltk.pos_tag(tokens)
	return segments
	
def handle(sentence):
	segments = seg(sentence)
	#print(segments)
	score = False
	info = False
	match =False
	rule = False
	day = ''
	team = []
	player = []
	noun,prep,adj,date = classify(segments)

	for n in noun:
		if n in SCORECHANNELS:
			score = True
		elif n in TEAMCHANNELS:
			team.append(n)	
		elif n in MATCHCHANNELS:
			match = True
		elif n in INFOCHANNELS:
			info = True
		elif n in PLAYERCHANNELS:
			player.append(n)
		elif n in DAYCHANNELS:
			day = n
		elif n == "rule":
			rule =True

	if score==True:
		if day!='':
			if day == "yesterday":
				date = datetime.date.today() - datetime.timedelta(days=1)
			elif day == "tomorrow":
				date = datetime.date.today() + datetime.timedelta(days=1)
			date = date.strftime("%m/%d/%Y")		
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
			search_info(team[0])
		else:
			search_info(player)
	elif match==True:
		if len(team)==0:
			print("\nPlease ask me with the teams you want to search~")
		elif len(team)==1:
			print("\nPlease tell me another team~")
		else:
			search_match(team[0],team[1])
	elif rule == True:
		print(" \n 1: team with uppercase letter\n"
		, "2: star player name with first name lastname\n",
		  "3: the date need to be month/day/year")
	else:
		print("\nsry, I can't understand what u say, Please type \"rule\" to see more details!")

	

def classify(segments):
	noun = []
	prep = []
	adj = []
	player=''
	date = ''
	for segment in segments:
		if segment[1]=='NN':
			noun.append(segment[0])
		elif segment[1] == 'NNP':
			if segment[0] not in TEAMCHANNELS:
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


def search_info(someone):
	print("".join(someone)+" is cool!")

def search_match(team1,team2,date):
	print(team1,team2,"17/04/2018, in Paris")




if __name__=='__main__':
	print("Hello, I can help you to search for all the information about NBA. For more details, Please enter \"rule\".")
	while True:
		print("->")
		handle(input())
		print("----------------------------------------")