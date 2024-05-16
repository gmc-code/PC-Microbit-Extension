====================================================
Car Class Composition
====================================================
    
| Write a child class of the **Car** class, **ElectricCar**.     
| Set the car's **make**, **model**, **year**, **color**. 

| Set the car's make, model, year, color. 
| The child class, ElectricCar, assigns an instance of the Battery class to the battery attribute.

| Complete the code to output:
| 2019 Grey Tesla Model S
| This car has a 90-kWh battery.
| This car can go about 480 km on a full charge.

.. admonition:: Tasks

    #. Write a **Battery** class to be assigned to a variable in the **ElectricCar** class using the scaffold below.

        .. code-block:: python

            class Car:
                
                def __init__(self, make, model, year, color):
                    self.make = make
                    self.model = model
                    self.year = year
                    self.color = color
                    self.odometer_reading = 0

                def get_info(self):
                    return f"{self.year} {self.color} {self.make} {self.model}".title()

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
                
                def __init__(self, make, model, year, color,          ):
                    super().__init__(make, model, year, color)
                    self.battery =             

                def fill_tank(self):
                    """Override parent method"""
                    print("No tank in this electric car.")
                    
            my_tesla = ElectricCar(make='tesla', model='model S', year=2019, color="grey", battery_size=90)
            print(my_tesla.get_info())
            my_tesla.battery.get_battery_info()
            my_tesla.battery.get_range()


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a **Battery** class to be assigned to a variable in the **ElectricCar** class.

                .. code-block:: python

                    class Car:
                        
                        def __init__(self, make, model, year, color):
                            self.make = make
                            self.model = model
                            self.year = year
                            self.color = color
                            self.odometer_reading = 0

                        def get_info(self):
                            return f"{self.year} {self.color} {self.make} {self.model}".title()

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
                        
                        def __init__(self, make, model, year, color, battery_size):
                            super().__init__(make, model, year, color)
                            self.battery = Battery(battery_size)

                        def fill_tank(self):
                            """Override parent method"""
                            print("No tank in this electric car.")
                            
                    my_tesla = ElectricCar(make='tesla', model='model S', year=2019, color="grey", battery_size=90)
                    print(my_tesla.get_info())
                    my_tesla.battery.get_battery_info()
                    my_tesla.battery.get_range()
