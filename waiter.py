# def total(bill,tip=10):
#     total_tip=0.1*bill
#     total_amount=total_tip+bill
#     total_amount=round(total_amount,7)
#     print("The total amount you have to pay is " ,total_amount)
# bill_amount=float(input("Enter the bill value : "))
# total(bill_amount) 

#cube of the cube

def cube(num):
    return num*num*num
def div_by_three(num):
    if num%3==0:
     return cube(num)
    else:
       return False
square=int(input("Enter a number "))
print(div_by_three(square))    


