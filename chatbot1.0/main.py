import mode1
import mode2
import mode3
import re
import random
import global_init
def main():
	print("-- Hello, I can help you to search for all the information about NBA. For more details, Please chose mode 3 and enter \"rule\".")
	print("-- For searching score, we can't offer the result within 3days because of the strange problem of our search site")
	mode = input("mode: ")
	global_init.set_mode(int(mode))
	mode3.init()
	while True:
		my_p = input("-> ")
		if re.search(r"exit ", my_p, re.I):
			break;
		else:
			if global_init.get_mode() == 1 :
				print("Rebot: ",mode1.rep())			
			if global_init.get_mode() == 2 :
				mode2.mode2(my_p)
			if global_init.get_mode() == 3 :
				mode3.mode3(my_p)
if __name__ =="__main__":
	main()