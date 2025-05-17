import math 

bill=float(input("Enter the total amount:  "))
due=float(input("Enter the amount you paid:  "))
if bill>due :
    print("You have to pay the shopkeeper ", (bill - due) )
elif due > bill :
    print("the shopkeeper has to return ", (due - bill) ) 
else :
    print("Payment completed")       