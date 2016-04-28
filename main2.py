import sys
import random
def typewrite(str):
	import sys
	from time import sleep

	for char in str:
		sleep(0.03)
		sys.stdout.write(char)
		sys.stdout.flush()
global gold
gold = 0
global weapon
weapon = 0
#story
def fight2n():
	global gold
	typewrite("\nYou ran away from the fight")
	typewrite("\nFor being a bitch you lose 50 gold")
	gold = gold - 50
	print("\nTotal gold = {}".format(gold))
def win1():
	typewrite("\nyou won")
def death():
	print("\n sorry bitch you lost")
def fight2y():
	global gold
	global weapon
	if weapon == 1:
		print("\nYou taunt the spider to make him salty")
		print("\nYOU MUST HIT ABOVE A 5 TO KILL THE SPIDER")
		print("\nIF THE SPIDER HITS HIGHER THAN YOU YOU DIE")
		print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		fdmg1 = int(random.randint(3, 10))
		edmg1 = int(random.randint(1, 5))
		typewrite("\nyou hit a", fdmg1)
		typewrite("\nthe spider hits a", edmg1)
		if edmg1 > fdmg1:
			typewrite("\nThe spider did more dmg than you!")
			death()
		elif fdmg1 < 5:
			print("\nyou didin't do enough damage to kill the spider, but you manage to live")
			figh2y()
		else:
			typewrite("\nYou killed the spider")
			gold = gold + 150
			win1()





def story2():
	global gold
	global weapon
	print ("\ngold {} ".format(gold))
	print ("\nweapon".format(weapon))
	typewrite("\nYou walk into the cave you see a sign it says")
	typewrite("\n$$$$$$$$$$$$$$$$$$")
	typewrite("\nCAVERN OF LEGACEY")
	typewrite("\n$$$$$$$$$$$$$$$$$$")

	typewrite("\nA giant aracnad aproaches you should {} run or fight".format(name))
	ch2 = input("\nRun or Fight\n").lower()
	if ch2 == "run":
		fight2n()
	elif ch2 == "fight":
		fight2y()

def ch1no():
	global gold
	typewrite("\nInstead of picking up the weapon you pocket 100 gold")
	gold = gold + 100
	story2()

def ch1yes():
	global weapon
	typewrite("\nYou aproach the weapon")
	typewrite("\nYou notice its a hefty mace")
	typewrite("\nequping the mace will increase your weapon level")
	weapon = weapon + 1
	story2()
def story():
	typewrite("\nWelcom to the legacey of {}".format(name))
	typewrite("\nYou walk into a old building")
	typewrite("\nYou notice a weapon on the floor do you wish to take it?")
	ch1 = input("\nDo you wish to take the item on the floor\n").lower()
	if ch1 == "yes":
		ch1yes()
	elif ch1 == "no":
		ch1no()

name = input("What will you name your chacter\n")
typewrite("\nHey {} you have".format(name))
typewrite("\n{} gold".format(gold))
story()

#fight1 spider cavern
def fight1y():
	print("fight1y")
def fight1n():
	print("fight2n")
