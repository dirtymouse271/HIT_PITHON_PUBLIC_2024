class Vehicle:
    def __init__(self,make):
        self.make = make
    def description(self):
        print(self.make)

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make)
        self.model = model
    def description(self):
        print(self.make, self.model)

class ElectricCar(Car):
    def __init__(self, make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size
    def description(self):
        print(self.make, self.model, self.battery_size)

Vehicle1 = Vehicle("Tesla")
Car1 = Car("Tesla","CyberTruck")
ElectricCar1 = ElectricCar("Tesla", "CyberTruck", "100000")
Vehicle1.description()
Car1.description()
ElectricCar1.description()
