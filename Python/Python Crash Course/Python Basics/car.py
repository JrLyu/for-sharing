class Car:
    def __init__(self, make, model, year):
        """Initializing characteristics"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Increase the odometer by a certain value."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
    
    def fill_gas_tank(self):
        print("The gas tank is filled.")


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100: 
            range = 315
        
        print(f"This car can go about {range} miles on a full charge")

        
class ElectricCar(Car):
    """Special characteristics for an electic Car."""
    def __init__(self, make, model, year):
        """Initializing the features from the father/super class."""
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def describe_batter(self):
        """Print the battery information."""
        print(f"This car has a {self.battery_size}-kWh batter.")
     
    def fill_gas_tank(self): 
        """Rewrite the method which is previously defined in the father class. """
        print("This car doesn't need a gas tank! ")