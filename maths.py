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
options =["Rock" , "Paper" , "Scissor"]
user_choice=input("Choose rock paper or scissors : ")
computer_choice=random.choice(options)
print("You choose : ",user_choice)
print("computer choose : ",computer_choice)

if user_choice==computer_choice:
    print("Its a tie")
elif user_choice=="Rock" and computer_choice=="Scissor":
    print("You win")
elif user_choice=="Paper" and computer_choice=="Rock":
    print("You win") 
elif user_choice=="Scissor" and computer_choice=="Paper":
    print("You win")     
else :
    print("you lose")          