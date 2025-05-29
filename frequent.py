compliment={'I':2,'am':6,'the':2,'kindest':2,'person':3,'in':2,'my':1,'class':2}
print("The original dicitionary : " + str(compliment))
k=input("enter the value you want to check the frequency of :  ")
s=0
for key in compliment:
    if compliment[key]==k:
     s=s+1
print("Frequency of ", k," in the following dictionary is : " +str(s))     
     