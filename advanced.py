# Write a program to return the addition of numbers of two different lists. Then, display a list that is square of numbers of another list. Use the map() function here to get the desired result.
# map = 
n1=[12,33,54,44]
n2=[20,38,56,84]
result=map(lambda x,y:x+y,n1,n2)
print("addition of two lists ")
print(list(result))

num=[8,4,6,5,0]
def sq(n):
    return n*n
square=list(map(sq , num))
print("square of numbers in list")
print(square)

# Write a program to return - 1. zipped list from two lists 2. elements of two lists zipped together, but 2nd list in reverse order 3. elements of two lists zipped into a dictionary

s1= {"safee","rohaan","ryyan"}
s2={20,18,16}
s3=list(zip(s1,s2))
print(s3,"\n")
l1=[10,20,30,40]
l2=[100,200,300,400]
for x,y in zip (l1,l2[::-1]):
    print(x,y)
stocks=["apple","dominos","samsumg"]
prices=[23947,19743,78999]
new_dict={stocks : prices for stocks,
          prices in zip(stocks,prices)}
print('\n{}'.format(new_dict))    