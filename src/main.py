import mode1
import mode2
import mode3
import re
import random
import global_init
def main():
	print("-- Hello, I'm JJ!! I can help you to search for all the information about NBA. For more details, Please choose mode 3 and enter \"rule\".")
	print("-- Input \"remode\" to modify the mode")
	mode = input("mode: ")
	global_init.set_mode(int(mode))
	mode3.init()
	while True:
		my_p = input("\n-> ")
		if re.search(r"exit ", my_p, re.I):
			break;
		elif re.search(r"remode", my_p, re.I):
			print("Which mode you wan to use?")
			global_init.set_mode(int(input()))
		else:
			if global_init.get_mode() == 1 :
				print(mode1.rep())			
			if global_init.get_mode() == 2 :
				mode2.mode2(my_p)
			if global_init.get_mode() == 3 :
				mode3.mode3(my_p)
if __name__ =="__main__":
	main()