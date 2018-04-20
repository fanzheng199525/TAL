import mode1
import mode2
import re
import random
word_family = ["parent","child","mother","father","aunt","uncle","mom","dad","kid","brother","sister","grandfather","grandmother"]
word_fruit = ["apple","pear","banana","peach","strawberry","grape","kiwi","mango","berry","date","orange","melon"]
word_tableware = ["fork","knife","spoon","napkin","dish","plate","glass","cup","mup","cloth"]
word_music=["piano","organ","flute","guitar","violin","drum","gong","cymbal","harp","cornet"]
word_animal = ["tiger","rabbit","monkey","cat","dog","bear","wolf","chicken","dug","mouse","rat","horse","sheep"]

family_question = ["Do you think your family is important","Do you go vocation with yor family frequently"]
fruit_question = ["Do you like eating fruits","What kind of fruits do you like best?"]
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

numero = {}
numero["family"]=0
numero["fruit"]=0
numero["tableware"]=0
numero["music"]=0
numero["animal"]=0

mode = 0
my_p = None
def main():
	global mode
	global my_p
	mode = input("mode: ")
	while True:
		my_p = input()
		if re.search(r"(exit)", my_p, re.I):
			break;
		else:
			if mode == "1":
				print("Rebot: ",mode1.rep())			
			if mode == "2":
				mode2.mode2_1(my_p)
			# if mode == 3:
			# 	mode3()
if __name__ =="__main__":
	main()