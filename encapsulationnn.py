# Write a program to create a class with following variables and methods - 
# 1. Private variable named privateVar that contains an integer value 
# 2. Create a private function privMeth that prints a message 
# 3. Create a function hello that prints the value of privateVar 
# 4. Create an object for the class and call all the functions.


# class kuchbhi:
   
   
#     __privatevar=1283
   
   
#     def __privmeth():
#         print("this is a private fxn")
    
    
#     def hello(self):
#         print("The value of variable is ",kuchbhi.__privatevar)

# ob=kuchbhi()
# ob.hello()
# ob.__privmeth


#Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). 
# Now create an object for the class Computer. 
# Try changing the value of max price and use the sell function to display the updated price.
#  Use a setter function to update the value and again display the price.

class computer:
    def __init__(self):
       self.__max_price=12000

    def sell(self):
        print("the maximum price of computer is ", self.__max_price)

    def setmaxprice(self,price):
        self.__max_price=price


ob=computer()
ob.sell()
ob.__max_price=18000
ob.sell()
ob.setmaxprice(18000)
ob.sell()




















            


