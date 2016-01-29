#! /usr/bin/env python
import random
import readline
#from future import print

d = lambda n: random.randint(1,n)

def roll(x, seed = 0):
	x = int(x)
	if seed != 0:
		random.setstate(seed)
	bar = 10 - int((x - 100)/20)
	d100 = d(100)
	checkDie = 12
	success = 0
	while (checkDie > bar or checkDie == 12) and checkDie != 1:
		if ((d100 <= x and d100 <= 95) or d100 <= 5) and success >= 0:
			success += 1
			bar += 1 
			d100 = d(100)
			checkDie = d(12)
		elif ((d100 >= x and d100 >= 5) or d100 >= 95) and success <= 0:
			success -= 1
			bar += 1
			d100 = d(100)
			checkDie = d(12)
		else:
			break
	return success

def table():
	for i in range(0, 100, 5):
		print("{:3}".format(i), end=" ")
	print("")
	s = random.getstate()
	for i in range(0, 100, 5):
		n = roll(i, seed=s)
		print("{:3}".format(n), end=" ")
	print("")

def nameSuccess(success):
	if success == 1:
		return " success.\n"
	elif success > 1:
		return " successes.\n"
	elif success == -1:
		return " failure.\n"
	elif success < -1:
		return " failures.\n"
	else:
		return " . . . somethings.\n"

while True:
	try:
		x = input("Skill: ")
		if x == "q":
			break
		success = roll(x)
		print("\n\t\t"+str(abs(success)) + nameSuccess(success))
	except:
		s = ""
		for i in range(1, 6):
			s += "{:>8}".format(d(100))
		print(s)
		print("")
		s = ""
		for i in range(1, 6):
			s +="{:>8}".format(d(12))
		print(s)
		print("")
		




