# try :
#     n=int(input("Enter a number "))
#     print("The number entered is ",n)
# except ValueError as v:
#     print("Exception: ",v)

#multiple exceptions
try:
    num1, num2= eval(input("Enter two numbers, seperated by a comma "))
    result=num1/num2
    print("Result is ",result)
except ZeroDivisionError:
    print("Division by zero is error !!!!")
except SyntaxError:
    print("comma missing . enter numbers seperated by comma ")
except :
    print("wrong input")
else:
    print("no exceptions")
finally :
    print("This will execute no matter what ")











    9
