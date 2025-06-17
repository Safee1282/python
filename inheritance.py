# Write a program to create a parent class Person (attributes - name, id number) with a method display to display the attributes.
#  Next, create a child class Employee (attributes - name, id number, salary, post). 
# Access the attributes of parent class in child class. 
# Then, create an object for child class and call the display method to display the name and id number.

class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print(self.name)
        print(self.id)

class employee(person):
    def __init__(self, name, id,salary,post):
        self.salary = salary
        self.post=post
        super().__init__(name, id)   

e1=employee("safee",1282,"1200000","CEO")
e1.display()





# Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage.
#  Then, create a Child Class Bus that inherits Class Vehicle. 
# Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.



class vehicle :
    def __init__(self,name,maximum_speed,mileage):
        self.name=name
        self.maximum_speed=maximum_speed
        self.mileage=mileage

class bus(vehicle):
    pass
b1=bus("School Volvo",120,45.3)
print("The name of the bus is", b1.name)
print("The mileage of the bus is ", b1.mileage)
print("The maximum speed of the bus is " ,b1.maximum_speed)


        