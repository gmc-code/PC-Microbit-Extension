====================================================
Car Class Composition
====================================================
    
| Write a child class of the **Car** class, **ElectricCar**.     
| Set the car's **make**, **model**, **year**, **colour**. 

| Set the car's make, model, year, colour. 
| The child class, ElectricCar, assigns an instance of the Battery class the battery attribute.

.. code-block:: python

    class Car:
        
        def __init__(self, make, model, year, colour):
            self.make = make
            self.model = model
            self.year = year
            self.colour = colour
            self.odometer_reading = 0

        def get_info(self):
            return f"{self.year} {self.colour} {self.make} {self.model}".title()

        def get_odometer(self):
            print(f"{self.get_info()} has done {self.odometer_reading} km.")

        def update_odometer(self, km):
            if km >= self.odometer_reading:
                self.odometer_reading = km
            else:
                print("Km on an odometer can't be lowered.")

        def increment_odometer(self, km):
            if km >= 0:
                self.odometer += km
            else:
                print("Km on an odometer can't be lowered.")
                
        def fill_tank(self):
            print("Tank is full.")


    class Battery:
        """To be assigned to an attribute in the ElectricCar class"""
        
        def __init__(self, battery_size=75):
            """Initialize the battery's attributes."""
            self.battery_size = battery_size

        def get_battery_info(self):
            print(f"This car has a {self.battery_size}-kWh battery.")

        def get_range(self):
            if self.battery_size == 75:
                range = 430
            elif self.battery_size == 90:
                range = 480
            elif self.battery_size == 100:
                range = 500
            print(f"This car can go about {range} km on a full charge.")


    class ElectricCar(Car):
        """ElectricCar child of Car class."""
        
        def __init__(self, make, model, year, colour, battery_size):
            super().__init__(make, model, year, colour)
            self.battery = Battery()

        def fill_tank(self):
            """Override parent method"""
            print("No tank in this electric car.")
            
    my_tesla = ElectricCar('tesla', 'model S', 2019, "grey", 90)
    print(my_tesla.get_info())
    my_tesla.battery.get_battery_info()
    my_tesla.battery.get_range()
