class Dog:
    # Class variable (common to all dogs)
    species = "Canis familiaris"  

    def __init__(self, name, breed):
        # Instance variables (unique to each object)
        self.name = name
        self.breed = breed

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print("-" * 30)


# Create two Dog objects of different breeds
dog1 = Dog("Tommy", "German Shepherd")
dog2 = Dog("Bruno", "Golden Retriever")

# Display details
dog1.display_details()
dog2.display_details()