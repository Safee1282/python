class BMW:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def start(self):
        return f"BMW {self.model} is starting with a smooth ignition system."

    def stop(self):
        return f"BMW {self.model} has stopped safely."

    def accelerate(self):
        return f"BMW {self.model} accelerates quickly with powerful performance."


class Ferrari:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def start(self):
        return f"Ferrari {self.model} roars to life with a thunderous engine sound."

    def stop(self):
        return f"Ferrari {self.model} halts with sharp ceramic brakes."

    def accelerate(self):
        return f"Ferrari {self.model} zooms ahead with extreme speed."


# Function to demonstrate polymorphism
def car_demo(car):
    print(car.start())
    print(car.accelerate())
    print(car.stop())
    print("-" * 60)


# Creating objects
bmw_car = BMW("X5", 75000)
ferrari_car = Ferrari("F8", 250000)

# Using polymorphism
for car in (bmw_car, ferrari_car):
    car_demo(car)