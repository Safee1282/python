import random
import time
number=random.randint(1,200)
def intro():
    print("May i ask for your name ???")
    global name 
    name=input()
    print(name +", we are going to play a game . i am thinking of a number between 1 and 200 ")
    if(number%2==0):
        x="even"
    else:
        x="odd"
    print("\n This is an {} number ".format(x))
    time.sleep(.5)    
    print("Go Ahead !!! Guess!!")    

def pick():
    guessestaken = 0
    while guessestaken<6:
        time.sleep(.25)
        enter=input("Guess: ")
        try:
            guess =int(enter)
            if guess<= 200 and guess>=1:
                guessestaken=guessestaken + 1
                if guessestaken<6:
                    if guess>number:
                        print("The guess of the number that you have entered is too high")
                    if guess<number:
                        print("The guess of the number that you have entered is too low")
                    if guess != number:
                        time.sleep(.5)
                        print("Try again")
                    if guess == number:
                        break 
            if guess>200 or guess<1:
                print("Silly Goose!! , That number isn't in the range")
                time.sleep(.25)
                print("Enter a number which is between 1 and 200")  
        except:
            print("I don't think that "+enter+"is a number , Sorry")
    if guess == number:
        guessestaken = str(guessestaken)
        print("Good job , {}!!. You guessed my number in {} guesses.".format(name , guessestaken))
    if guess != number:
        print("Nope , The number i was thinking of was " + str(number))
playagain="yes"
while playagain =="yes" or playagain == "Y" or playagain == "y"  or playagain == "YES" or playagain == "Yes":
    intro()
    pick()
    print("Do you want to play again???")
    playagain=input()               






