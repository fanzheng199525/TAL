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

# if __name__=='__main__':
# 	while 1:
# 		print("Your term to speak: ")
# 		print("Rebot: ",rep(input()))