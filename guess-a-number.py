#guess a number between 1 and 100

from random import randint

play = True

while play == True:
    #get a random number between 1 and 100
    luku = randint(1,100)
    #get the first guess from player
    ok = False
    while ok == False:
        try:
            arvaus = int(input("guess a number (1-100) "))
            ok = True
        except:
            print("You need to give a number")
    arvausten_maara = 1

    #check&tell if the guess is close or not
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
    #get a new guess and check&tell if it's closer or not
    while arvaus != luku:
        ok = False
        while ok == False:
            try:
                uusi_arvaus = int(input("guess again "))
                ok = True
            except:
                print("You need to give a number")
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
    #ask if player wants to play again
    again = input("Wanna play again? y/n ")
    if again.lower() == "y":
        play = True
    else:
        print("Thanks for playing!")
        play = False