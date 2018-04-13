import random
BACKCHANNELS = ["un huh","hmm","go on","yeah","yep","ah ha"]

class model1:
	def __init__(self):
		self.record = None

	def rep(self,sentence):
		 reponse = random.choice(BACKCHANNELS)
		 while reponse == self.record:
		 	reponse = random.choice(BACKCHANNELS)
		 self.record = reponse
		 return reponse

if __name__=='__main__':
	model1 = model1()
	while 1:
		print("Your term to speak: ")
		print("Rebot: ",model1.rep(input()))

