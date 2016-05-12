import sys
import time
from time import sleep
import random

def typewrite(str):
	for char in str:
		sleep(0.03)
		sys.stdout.write(char)
		sys.stdout.flush()

def story_a():
	random.seed(time.time())
	name = raw_input("What Is Your Name?\n")
	if name == "kade":
		print("Whats up")
	hp = 100
	dead = False

def damage(amount):
	global hp
	global dead

	hp -= amount
	if hp <= 0:
		dead = True
		typewrite("You died!")
		return True
	return False

def pub_fight1():
	print ("Pub\nYou walk into a pub that seems very clean and nice but there is gambling\nYou get hit by a drunk dude\n")
	if damage(random.randrange(50, 150)):
		return
		print("Thankfully you survive!")



def start():
	print """
			WELCOME TO THE GAME OF STUFF
					`````````````````````
			````````````````
					````````````````````
		"""
		



def main():
	start()
	time.sleep(3)
	story_a()
	pub_fight1()
main()