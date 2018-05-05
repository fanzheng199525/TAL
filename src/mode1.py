import random
BACKCHANNELS = ["un huh","hmm","go on","yeah","yep","ah ha"]

record = None

def rep():
	global record
	reponse = random.choice(BACKCHANNELS)
	while reponse == record:
		reponse = random.choice(BACKCHANNELS)
	record = reponse
	return reponse
