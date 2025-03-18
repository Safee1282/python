# weight=float(input("Enter your weight in kg : "))
# height=float(input("Enter your height in metres : "))
# BMI=weight/(height*height)

# print("Your BMI value is " , BMI)


# if BMI<18.5 :
#     print("You are underweight")
# elif BMI>=18.5 and BMI<=24.9 :
#     print("You are normal weight") 
# elif BMI>=25 and BMI<=29.9 :
#     print("You are overweight")
# else :
#     print("You are obese")        
       


#  Q1. Write a program to accept percentage from the user and display the grade according to the following criteria:
# Marks Grade
# > 90 A
# > 80 and <= 90 B
# >= 60 and <= 80 C
# below 60 D

percentage=float(input("Enter your percentage : "))

if percentage>90 :
    print("Your grading is A")
elif percentage>80 and percentage<=90 :
    print("Your grading is B")
elif percentage>=60 and percentage<=80 :
    print("Your grading is C ")
elif percentage>=30 and percentage<60 :
    print("Your grading is D")
else :
    print("your grading is F")                