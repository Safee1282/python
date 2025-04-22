#write a program to check alphabet “A” is present in the given string or not.
#  And terminate the loop after finding the alphabet “A.”

# string=str(input("Enter a word ??? "))
# for i in string:
#     if i=="a" or i=="A":
#         print("Letter A found")
#         break
#     else :
#         print("Letter A not found")  

#Write a program to display 1 to 10 numbers in reverse order and skip the number 5.

# for i in range(10,0,-1):
#     if i==5:
#         continue
#     print(i)

# i=11
# while i>0 :
#     i=i-1
#     if i==5:
#         continue
#     print(i)

    #Write a program to satisfy the following conditions of the given range:
    #  If the number is divisible by 20, it provides an output "twist."
    #  If the number is divisible by 15, it will pass (no output)
    #  If the number is divisible by 5, it will give an output “fizz.
    # ” If the number is divisible by 3, it will give an output "buzz." 
    # Otherwise, it will give the output of that number.


n=int(input("Enter a number : "))
if n%20==0:
    print("Twist")
elif n%15==0:
    pass
elif n%5==0:
    print("Fizz")
elif n%3==0:
    print("buzz")
else:
    print(n)            

           
