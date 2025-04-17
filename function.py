# def demo(name):
#     print("hello",name)
#     print("I am your new teacher")

# demo("safee")

# def sum(a,b):
#     c=a+b 
#     print("The sum is ",c)
# n=int(input("Enter a random number : "))    
# n1=int(input("Enter another random number : "))    
# sum(n,n1)


def add(a,b):
    '''take two numbers add them and print their result'''
    return a+b 
def sub(a,b):
    return a-b
def into(a,b):
    return a*b
def by(a,b):
    return a/b
print("a,Addition")
print("b,subtraction")
print("c,multiplication")
print("d,division")
ask=str(input("Choose an operation "))
n=int(input("Enter a  number : "))    
n1=int(input("Enter another number : ")) 
if ask=="a":
    print("the sum of numbers entered is ",add(n1,n))
elif ask=="b":
    print("the difference of numbers entered is ",sub(n,n1))
elif ask=="c":
    print("the product of numbers entered is ",into(n,n1))  
else :
    print("the quotient of numbers entered is ",by(n,n1)) 

print(add.__doc__)   
print(print.__doc__)  
    


    
