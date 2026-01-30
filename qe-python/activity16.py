class Car:
    def __init__(self,manufacturer,model,make,transmission,colour):
     self.manufacturer = manufacturer
     self.model = model
     self.make = make
     self.transmission = transmission
     self.colour = colour
    def accelerate(self):
        print(f"{self.manufacturer} {self.model} is moving")
    def stop(self):
        print(f"{self.manufacturer} {self.model} has stopped")
car1 = Car("toyota","Forturner","2023","Manual","black")
car2 = Car("Ford","Mustang","1964","Manual","Black")

car1.accelerate()
car1.stop()

car2.accelerate()
car2.stop()