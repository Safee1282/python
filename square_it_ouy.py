num=[5,4,6,33,7,8,9,26,23,22,12]
sqnum=[]
even=0
odd=0
for i in num:
    
    sqnum.append(i*i)
print(num)
print(sqnum)
    
for j in sqnum:
        if j%2 == 0:
            even+=1
        else :
            odd+=1
print("Even : ",even)
print("Odd : ",odd)            

