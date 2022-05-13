#guess a number between 1 and 100

from random import randint

#get a random number between 1 and 100
luku = randint(1,100)
#get the first guess from user
arvaus = int(input("guess a number (1-100) "))
arvausten_maara = 1

#check if the guess is close or not
while arvaus != luku:
	if arvaus < 0 or arvaus > 100:
		print("OUT OF BOUNDS")
		break
	elif abs(luku - arvaus) <= 10:
		print("WARM")
		break
	elif abs(luku - arvaus) > 10:
		print("COLD")
		break
#get a new guess and check if it's closer or not
while arvaus != luku:
	uusi_arvaus = int(input("guess again "))
	arvausten_maara += 1
	while uusi_arvaus != luku:
		if uusi_arvaus < 0 or uusi_arvaus > 100:
			print("OUT OF BOUNDS")
			break
		elif abs(luku - arvaus) > abs(luku - uusi_arvaus):
			print("WARMER")
			break
		elif abs(luku - arvaus) < abs(luku - uusi_arvaus):
			print("COLDER")
			break
		elif abs(luku - arvaus) == abs(luku - uusi_arvaus):
			print("same distance")
			break
	arvaus = uusi_arvaus

print(f"you guessed it! The amount of guesses was {arvausten_maara}")
