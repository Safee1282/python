# Base class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100   # base fare per person is 100


# Child class
class Bus(Vehicle):
    def fare(self):
        # 10% extra charges for maintenance
        total_fare = super().fare() + (0.1 * super().fare())
        return total_fare


# Example usage
bus1 = Bus("School Volvo", 12, 50)
print(f"Total Bus fare is: {bus1.fare()}")
