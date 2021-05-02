import random
import time
print("-----------------🤩Darlington's Guessing Game🤩-----------------")
time.sleep(2)
print("Loading...")
time.sleep(3)
name = input("What random name would you be called? \n")
print("\nWelcome, " + name, "\n" )
print("To quit anytime, enter: q")

time.sleep(2)
score = 0
print("Level 1 Begin🤤🤤🤤")
time.sleep(1)
print("Here you are to guess a number from 0 - 2 \n")
while True:
	
	guess = input("Guess: ")
	rdm_num = random.randrange(0, 3)
	if guess == "q":
		print("your score was", score)
		print("Hope you enjoyed ")
		break
	elif int(guess) == rdm_num:
		print("The number was : ", rdm_num)
		score = score + 10
		print("aded score: ", score)
		time.sleep(2)
	elif int(guess) != rdm_num:
		print("Your number was ", guess)
		print("The number was ", rdm_num) 
	if score == 50:
		print("Hurray...🥳🥳🥳 " + name + " You've completed level 1.🥳🥳🥳")
		print("\nLevel 2 Begins")
		break

print("Here you are to guess a number from 0 - 5 \n")
while True:
	guess = input("Guess:")
	rdm_num = random.randrange(0, 6)	
	if guess == "q":
		print( name + "Your score was", score )
		print("Hope you enjoyed the game")
		break
	elif int(guess) == rdm_num:
		print("Your number was ", guess)
		print("The number was : ", rdm_num)
		score = score + 10
		print("aded score: ", score)
		time.sleep(2)
	elif int(guess) != rdm_num:
		print("The number was ", rdm_num)
	if score == 100:
		print("\nHurray....🥳🥳🥳" + name )
		print("\nyour score was", score)
		print("\nYou've completed this game, please wait for more updates to continue playing")
		print("\nHope you enjoyed this game?")
	break
	
