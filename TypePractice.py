#!/usr/bin/python3

import time
import random
import os

def y_nCheck():
	yesList = ("y","Y","YES","Yes","yes")
	noList = ("n","N","NO","no","No")
	while(True):
		print("Y/N?")
		y_n = input()
		if y_n in yesList:
			return "y"
			break
		elif y_n in noList:
			return "n"
			break
		else:
			print("NOT Y/N!")
			
def str_to_char(string):
	li = []
	for i in string:
		li += [char for char in i]
	return(li)

textfile = open("Kinematics.txt", 'r')
phraise_list = textfile.readlines()
	


while(True):
	# -----
	phraise = phraise_list[random.randint(0,len(phraise_list))]
	x = 0 # counter used for tracking letter position.

	print("ENTER will START the Clock!")
	input()
	for i in range(0,3):
		print(3 - i)
		time.sleep(1)
		
	os.system('clear')
	print(phraise)
	# ---------------------
	t1 = time.perf_counter()

	phr = str_to_char(phraise)
	inp = input()
	inp_car = str_to_char(inp)
	fail_p = []

	# compare input vs phrase
	for i in inp:
		if i != phr[x]:
			fail_p.append("%d:%s"%(x+1,inp[x]))
		x += 1
	print(fail_p)

	t2 = time.perf_counter()
	t_time = t2-t1

	comp_equation = len(inp.split() * 60) / t_time
	print("\n Your typing took: %f seconds"%(t_time))
	print(" You types an avg of %f Words Per Minute"%(comp_equation))
	
	print(" Test Again? Y/N")
	if y_nCheck() == 'y':
		continue
	else:
		break
	# ------------------------
