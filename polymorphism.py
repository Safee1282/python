class india():
    def capital(self):
        print("New Delhi is the capital of India . ")
    def language(self):
        print("Hindi is the most widely spoken language in India .")
    def type(self):
        print("India is a developing country . ")

class usa():
    def capital(self):
        print("Washington D.C is the capital of USA . ")
    def language(self):
        print("English is the primary language of USA .")
    def type(self):
        print("USA is a developed country . ")

obj_ind=india()
obj_usa=usa()

for country in (obj_ind , obj_usa):
    country.capital()
    country.language()
    country.type()