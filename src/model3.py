import nltk
import datetime
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
	print(segments)
	score = False
	info = False
	match =False
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

	if score==True:
		if day!='':
			if day == "yesterday":
				date = datetime.date.today() - datetime.timedelta(days=1)
			elif day == "tomorrow":
				date = datetime.date.today() + datetime.timedelta(days=1)
			date = date.strftime("%m/%d/%Y")		
		
		print(date)
		if len(team)==0:
			print("Please ask me with the teams you want to search~")	
		else:
			search_score(team[0],team[1],date)
	elif info==True or (match==False and "about" in prep):
		if len(team)!=0:
			search_info(team[0])
		else:
			search_info(player)
	elif match==True:
		if len(team)==0:
			print("Please ask me with the teams you want to search~")
		else:
			search_match(team[0],team[1])

	

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
			date=segment[0]

	if player!='':
		player= player.rstrip()
		noun.append(player)
	return noun,prep,adj,date


def search_info(someone):
	print("".join(someone)+" is cool!")

def search_match(team1,team2,date):
	print(team1,team2,"17/04/2018, in Paris")




if __name__=='__main__':
	handle(input())