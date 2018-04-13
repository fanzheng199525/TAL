import nltk

def seg():
	sentence = "Hello!!!My name is Shadow Fiend!I love you!"
	tokens = nltk.word_tokenize(sentence)
	segments = nltk.pos_tag(tokens)
	for segment in segments:
		print (segment[0], '\t', segment[1])

if __name__=='__main__':
	seg()