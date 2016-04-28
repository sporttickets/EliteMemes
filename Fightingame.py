
def typewrite(str):
	import sys
	from time import sleep

	for char in str:
		sleep(0.03)
		sys.stdout.write(char)
		sys.stdout.flush()

import random
import sys
from time import sleep
gold = 0
#game function


#print_pause([
	#("fajdk;jkajdjkdf;adfajd;k", 2),
	#("jdfka;djk;ajdfk;ajdkfj;adfjk;", 2),
	#])

print 						("w-------------------------------w")
print 						("Welcome to the cavern of secrets!")
print 						("w---------------------------------w")

name = raw_input("What is your name\n")
typewrite("You Enter A Hold abandon house and find a sword Will you pick it up?\n")
ch1 = str(input("Do You take it?"))
if ch1.lower() in ["yes"]:
	print("you Have taken the sword")
	weapon=1
#stick not taken 
else:
	print("you did not take the stick\n")
	weapon=0
typewrite("You see a big ass spider do you want to kill it\n")

#question2
ch2 = str(input("Yes or no"))
if ch2.lower() in ["yes"]:
	print("```````````````````````````````````````````")
	typewrite("				  Fighting................")
	print(" YOU MUST HIT ABOVE A 5 TO KILL THE SPIDER")
	print("	IF THE SPIDER HITS HIGHER THAN YOU YOU WILL DIE")
	print("``````````````````````````````````````````````````")
	pdmg1 = int(random.randint(3, 10))
	edmg1 = int(random.randint(1, 5))


	print ("you hit a", pdmg1)
	print ("the spider hits a", edmg1)
	if edmg1 > pdmg1:
		print ("The spider did more dmg than you so there fore you're dead :(")
		complete = 0
	return complete


	elif pdmg1 < 5:
		print ("you didin't do enough dmg to kill the spider but you survied")
		complete = 1
		return complete


	else:
		print ("you killed the spider")
		gold = 100
		complete = 1
		return complete


else:
	print("you're a bitch")
