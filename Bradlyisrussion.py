import random
global name, score
def are_you_sure():
	if question_1 == False:
		print("\n  You Leave the old door and walk back to the choosing ground.  ")
		start_2()
	elif question_1 == True:
		print("\n  You leave the Futrustic door and walk back to the choosing ground.  ")
		start_2()
def start():
	name = raw_input("What is your name? \n")
	print("Hello {}, how are you".format(name))
	print("\n  You need to play this game yeah you do")
def start_2():
	global name
	print("\n  You See Two rustic looking doors One looks futrustic and the other Looks quite old\n  What door do you wan't! ")
	question_1 = raw_input("\nLeft ' Old rustic door' Or Right'Futrustic looking door\n").lower()
	if question_1 == "left":
		print ("\n {} aprachoes the door slowly looking around before he enters.\n You open the door and see a world of Old times wizards and such".format(name))
		return False
		are_you_sure()
	elif question_1 == "right":
		print("\n As you walk towrds the futrustic door you see a world of tech you have never seen before.")
		return True
		are_you_sure()
	else:
		are_you_sure()

def main():
	start()
	start_2()
main()
