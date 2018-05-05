import re
import random
import global_init
import mode1
word_family = ["parent","child","mother","father","aunt","uncle","mom","dad","kid","brother","sister","grandfather","grandmother"]
word_fruit = ["apple","pear","banana","peach","strawberry","grape","kiwi","mango","berry","date","orange","melon"]
word_tableware = ["fork","knife","spoon","napkin","dish","plate","glass","cup","mup","cloth"]
word_music=["piano","organ","flute","guitar","violin","drum","gong","cymbal","harp","cornet"]
word_animal = ["tiger","rabbit","monkey","cat","dog","bear","wolf","chicken","dug","mouse","rat","horse","sheep"]

family_question = ["Do you think your family is important?","Do you go vocation with yor family frequently?"]
fruit_question = ["Do you like eating fruits?","What kind of fruits do you like best?"]
tableware_question = ["What kind of tablewares do you use the most frequently?","In your country, what kind of tablewares do people use?"]
animal_question = ["Do you want to have an dometic animal?","Have you had an animal?"]
music_question = ["Have you learned music?","What kind of musics do you like best?"]


list_family = [word_family, family_question]
list_fruit = [word_fruit, fruit_question]
list_tableware = [word_tableware, tableware_question]
list_music = [word_music, music_question]
list_animal = [word_animal, animal_question]

vocabulary = {}
vocabulary["family"]=list_family
vocabulary["fruit"]=list_fruit
vocabulary["tableware"]=list_tableware
vocabulary["music"]=list_music
vocabulary["animal"]=list_animal

# numero{} is to memorize the sentence used last time
numero = {}
numero["family"]=0
numero["fruit"]=0
numero["tableware"]=0
numero["music"]=0
numero["animal"]=0

def mode2(my_p):
	# abbreviated sentences: i'm, he's ...
	cond = re.search(r"(i'm|he's|she's|it's|they're|you're)", my_p, re.I)
	if cond:
		myp_list = re.split(r"i'm |he's |she's |it's |they're |you're ", my_p, flags=re.I)
		if re.search(r"(i'm)", my_p, re.I):
			myp_list[0]="are you"
		if re.search(r"(he's)", my_p, re.I):
			myp_list[0]="is he"
		if re.search(r"(she's)", my_p, re.I):
			myp_list[0]="is she"
		if re.search(r"(they're)", my_p, re.I):
			myp_list[0]="are they"
		if re.search(r"(it's)", my_p, re.I):
			myp_list[0]="is it"
		if re.search(r"(you're)", my_p, re.I):
			myp_list[0]="am I"
		print ("Rebot:","Why",myp_list[0],myp_list[1],"?")
	# no abbreviated sentences: i am, he is...	
	elif re.search(r"(am |is |was |will be |has been |are |had been |have been |were )", my_p, re.I):
		myp_list = re.split(r"(am|is|was|will be|has been|are|had been|have been|were)[ ]+", my_p, flags =re.I)
		if re.search(r"(i )", myp_list[0], re.I):
			# change the subject
			myp_list[0]="you"
			if re.search(r"(am)",myp_list[1], re.I ):
				# change the verb
				myp_list[1]="are"
			elif re.search(r"(was)",myp_list[1], re.I ):
				myp_list[1]="were"
			elif re.search(r"(has been)",myp_list[1], re.I ):
				myp_list[1]="have been"
		elif re.search(r"( you)", myp_list[0], re.I):
			myp_list[0]="I"
			if re.search(r"(are)",myp_list[1], re.I ):
				myp_list[1]="am"
			elif re.search(r"(were)",myp_list[1], re.I ):
				myp_list[1]="was"
			elif re.search(r"(have been)",myp_list[1], re.I ):
				myp_list[1]="has been"
		else:
			# Uniform use of "he" for non special subjects  
			myp_list[0]="he"
		print("Rebot:","Why",myp_list[1],myp_list[0],myp_list[2],"?")
	#---------------------------------------------------------------------------------------------------------------------
	else:
		flag = 0
		for key, values in vocabulary.items():
			for mot in values[0]:
				# to verifiy there are the keywords in the sentence my_p
				if re.search(mot, my_p, re.I):
					# choose a sentence different from last time
					num = random.randint(0,1)
					if num==numero[key]:
						num=(num+1) % 2
						numero[key]=num
					else:
						numero[key]=num
					print("Rebot:",values[1][num])

					flag = 1
					break 
			if flag == 1:
				break
		if flag == 0:
			# Chatbot fail to repond the user in mode 2, it will change to mode 1 automatiquement
			global_init.minus_mode()
			print("Rebot:",mode1.rep())

