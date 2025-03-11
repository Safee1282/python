#t1=78
#t2=97
#t3=127
#t4=87
#t5=70
#sum=t1+t2+t3+t4+t5
#average=sum/5
#print("The average height of a tree is " , average)


#n1=78
#n2=4
#print(n1+n2)
#print(n1-n2)
# print(n1*n2)
# print(n1/n2)
# print(n1//n2)
# print(n1%n2)
# print(n2**7)


# math=40
# science=70 
# hindi=50
# english=60
# sum=math+english+science+hindi
# percentage=(sum/400)*100
# print("The percentage of Raj scores is " , percentage)


amt=int(input("Enter the amount : "))


note=amt//500
note1=(amt%500)//200
note2=((amt%500)%200)//100
note3=(((amt%500)%200)%100)//50
note4=((((amt%500)%200)%100)%50)//20
note5=(((((amt%500)%200)%100)%50)%20)//10

print(note)
print(note1)
print(note2)
print(note3)
print(note4)
print(note5)