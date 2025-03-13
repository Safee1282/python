#write a program to check whether the given number is positive?
# number=int(input("Enter a number : "))
# if number>0 :
#     print("Your number entered is positive")




#Write a program to check whether the given number is greater than 15 or smaller than 15.

# num=int(input("Enter a number : "))
# if num>15 :
#     print("your number entered is greater then 15 ")   
# else:
#     print("Your number is smaller than 15")  




    #Write a program to check whether the given number is even or odd? 

# n=int(input("Enter a number : "))
# if n%2==0 :
#     print("Your number entered is even")
# else:
#     print("Your number entered is odd")   


#Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss? 

cost_price=float(input("Enter the actual cost :"))
selling_price=float(input("Enter the selling cost :"))
if (selling_price>cost_price):
    amount=selling_price-cost_price
    print("you have a profit of  " , amount)
else:
    loss=cost_price-selling_price
    print("You have a loss of " , loss)    