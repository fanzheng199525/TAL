def mode2_2(my_p):
	# i nees to add a boucle not finshed until i entre a key, for example, crtl+c
	global mode
	# print("222222222222222222222")
	# print(my_p)
	flag = 0
	for key, values in vocabulary.items():
		# print(numero)
		for mot in values[0]:
			if re.search(mot, my_p, re.I):
				num = random.randint(0,1)
				if num==numero[key]:
					num=(num+1) % 2
					numero[key]=num
				else:
					numero[key]=num
				print(values[1][num])

				flag = 1
				break 
		if flag == 1:
			break
	mode-=1
	print(mode)


import re
import random
def mode2_1(my_p):
	global mode
	# print("111111111111111111111")
	# print(my_p)
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
		print ("Why",myp_list[0],myp_list[1],"?")
	elif re.search(r"(am|is|was|will be|has been|are|had been|have been|were)", my_p, re.I):
		myp_list = re.split(r"(am|is|was|will be|has been|are|had been|have been|were)[ ]+", my_p, flags =re.I)
		if re.search(r"(i )", myp_list[0], re.I):
			myp_list[0]="you"
			if re.search(r"(am)",myp_list[1], re.I ):
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
			myp_list[0]="he"

		print("Why",myp_list[1],myp_list[0],myp_list[2],"?")
	else:
		mode-=1
		print(mode)


# if __name__ =="__main__":
# 	a = input()
# 	my_p = input("gfchdjk: ")
# 	if a=="1":
# 		mode2_1()
# 	else:
# 		mode2_2()





