# Day41_partb: 50daysofcodechallenge
class Ford:        # creating the class Ford
    def __init__(self, model, color, year, transmission, electric):    # creating the method __init()__
        self.model = model   # creating variables
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric

    def print_cars(self):  # creating a method called print_cars
        return (
            f"car_model = {self.model} \n Color = {self.color} \n Year = {self.year} \n Transmission = {self.transmission} \n Electric = {self.electric}")   # printing out the info for different cars


class BMW(Ford):  # creating a class BMW that inherits from the class Ford
    def __init__(self, model, color, year, transmission, electric):  # creating method called __init()__
        super().__init__(model, color, year, transmission, electric)  # giving the subclass BMW access to the properties of its parent class


class Tesla(Ford):   # creating a class Tesla that inherits from the class Ford
    def __init__(self, model, color, year, transmission, electric):    # creating the method __init__()
        super().__init__(model, color, year, transmission, electric)    # giving the subclass Tesla access to the properties of its parent class


ford1 = Ford("focus", "White", 2020, "Auto", False)   # creating the object ford1 from the class Ford
bmw1 = BMW("x6", "silver", 2018, "Auto", False)   # creating the object bmw1 from the class BMW
tesla1 = Tesla("S", "beige", 2017, "Auto", True)  # creating the object tesla1 from the class Tesla

print(ford1.print_cars())    # printing object ford1 with method print_cars()
