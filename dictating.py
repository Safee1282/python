# student={"name":"safee","age":12,"roll":20}
# print(type(student))
# print(student("name"))
# student["grade"]=7
# y=student.keys()
# print(y)
# z=student.values()
# print(z)
# x=student.items()
# print(x)
# student.popitem()
# student.pop("roll")
# print(student)
# cubes={1:1,2:8,3:27,4:64,5:125}
# for i in cubes:
#     print(cubes[i])

country_code={"India":'0091',"nepal":'00997',"australia":'0025'}
print("Country code for India - ")
print(country_code.get('India', 'Not found'))
print("country code for England -")
print(country_code.get('England', 'Not found'))

test_dict={'codingal':2,'is':2,'best':2,'for':2,'coding':1}
print("The original dictionary : " + str(test_dict))
k=2
r=0
for key in test_dict:
    if test_dict[key]== k:
        r=r+1
print("Frequency of k is : " + str(r))        

