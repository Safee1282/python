#Write a program to create a class with the name Student and perform the following tasks - 
# 1. Declare a variable grade 
# 2. Print a sentence inside the class 
# 3. Create an object of class student and see the output

class student:
    grade=7
    print("Hi i am a student of grade ",grade)
safee=student()


# Write a program to create a class Vehicle and perform the following tasks - 
# 1. Create an __init__ method with arguments - max_speed and mileage 
# 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 
# 3. Print the values of max_speed and mileage by using the object

class vehicle:
     def __init__(self,max_speed,mileage):
          self.max_speed=max_speed
          self.mileage=mileage

jeep= vehicle(220,39)
print("Max speed of jeep compass is ",jeep.max_speed)    
print("Mileage of jeep compass is ",jeep.mileage)      



# Write a program to create a class Parrot and perform the following tasks - 
# 1. Create a class variable species 
# 2. Create a __init__ method that has instance variables - name and age 
# 3. Create instances of class Parrot, passing arguments as well 
# 4. Print Class variable by accessing it 
# 5. Print Instance variables as well


class parrot:
     species="bird"
     def __init__(self,name,age):
          self.name=name
          self.age=age 

bittu=parrot("bittu",5)
totu=parrot("totu",3)
print("Bittu is a ",bittu.species)
print(totu.name, " is ", totu.age," Years old")

         
        