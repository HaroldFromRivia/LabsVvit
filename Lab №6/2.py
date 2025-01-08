class Vehicle:
    def __init__(self,make, model):
        self.__make = make
        self.__model = model
    def get_info(self):
        return [self.__make,self.__model]

class Car(Vehicle):
    def __init__(self,fuel_type):
        self.fuel_type = fuel_type
    def get_info(self):
        return self.fuel_type