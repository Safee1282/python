# medical=input("Does the student have a medical cause (y or n) ")
# attendance=float(input("Enter the attendance of the student "))
# if medical== "y" :
#     print("you are allowed to appear for the examination")
# else :
#     if attendance>=75 :
#         print("you are eligible for the examination ")
#     else :
#         print("You are not eligible for the examination ")    


#         Write a program to calculate the electricity bill. The bill is calculated by checking the number of units
#  consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that
#  bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25,
#  and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit 
# cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.

unit=int(input("Enter the number of units consumed "))

if unit<=50 :
    amt=(unit*2.60)
    tax=25
elif  unit<=100 :
    amt=130 + (unit-50)*3.25
    tax=35
elif  unit<=200 :
    amt= 100*3.25 + (u-100) * 5.26
    tax=45
else :
    amt=     100*3.25 + 100*5.26 + (unit-100) *8.45 
    tax=75
print("your total bill is " , (amt+tax))