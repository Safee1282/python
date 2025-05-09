# import random
# num=str(random.randint(1,40))
# print("lets paly a game of guessing !!!")
# print("guess any number from 1-10 : ")
# while True :
#     choice=input("Enter your choice : ")
#     if num==choice:
#      print("right to the point")
#      print("The number was " ,num)
#      break
#     else :
#        print("Incorrect answer")
#        print("try again")

# import math 
# num=int(input("Enter a number : "))
# print(math.sqrt(num))
# print(math.ceil(34.1))
# print(math.floor(34.1))
# print(math.pow(5,10))


import random 
options =["rock" , "paper" , "scissor"]
user_choice=input("Choose rock paper or scissors : ")
computer_choice=random.choice(options)
print("You choose : ",user_choice)
print("computer choose : ",computer_choice)

if user_choice==computer_choice:
    print("Its a tie")
elif user_choice=="rock" and computer_choice=="scissor":
    print("You win")
elif user_choice=="paper" and computer_choice=="rock":
    print("You win") 
elif user_choice=="scissor" and computer_choice=="paper":
    print("You win")     
else :
    print("you lose")          