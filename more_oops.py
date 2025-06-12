# Write a program to create a class IOString which consists of a constructor that gives a default value to variable str1. 
# Next up create a method that gets a string as input from the user. 
# Create another method that will print the string in the upper case.
#  Next up create an object and call methods to get everything implemented.

class IOString:
    def __init__(self):
        self.str1=""
    def getS(self):
        self.str1=input("Enter a string   ")
    def printS(self):
        print("Result is ",self.str1.upper())
str1=IOString() 
str1.getS()
str1.printS()
        


# Write a program to create a class with the named employee and create a constructor and destructor. 
# Then, write a function to create an object for that class and delete the object.
#  Make sure you call the function to get everything implemented!     
 
       
class employee:
    def __init__(self):
        print("Employee hired")
    def __del__(self):
        print("Employee fired " \
        "As he was asking for raise on his first day")    
def company(): 
    print("Making an object ")
    e2=employee()
    return e2 
e2=company()
print("program ended")
print("interview ended as e2 agreed to do double work for half salary")


       
