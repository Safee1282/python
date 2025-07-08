class circle:
    def __init__(self):
     
     radius=input("Enter the radius of the circle : ")
     self.r=radius
    def area(self,radius):
      
      area=(22/7*radius)* radius
      
      print(area)
    def perimeter(self):
       self.r=radius
       perimeter=2*22/7*radius
       print(perimeter)  
obj1=circle()
obj1.area()
obj1.perimeter()



