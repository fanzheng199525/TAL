import mode1
import mode2
import re
import random
import global_init
def main():
	mode = input("mode: ")
	global_init.set_mode(int(mode))
	while True:
		my_p = input()
		if re.search(r"(exit)", my_p, re.I):
			break;
		else:
			if global_init.get_mode() == 1 :
				print("Rebot: ",mode1.rep())			
			if global_init.get_mode() == 2 :
				mode2.mode2(my_p)
			if global_init.get_mode == 3 :
				mode3.mode3(my_p)
if __name__ =="__main__":
	main()