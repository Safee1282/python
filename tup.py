tup=(25 , 56 , 78,86)
print(tup[1:6])

d1=list(tup)
print(d1)
d1[0]=235686
tup=tuple(d1)
print(tup)

tuplle=(7,8,3,5,3,6,3,7,8,12,7890)
print(tuplle.count(3))

def palind(r):
    e=len(r)-1
    s=0
    while (s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r=input("Enter a number or word : ")
if (palind(r)):
    print("The tuple is flip-flop")
else :
    print("The tuple is not flip-flop")
