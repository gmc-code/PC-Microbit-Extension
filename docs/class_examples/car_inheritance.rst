====================================================
Car Class Inheritance
====================================================

| Write a child class of the **Car** class, **ElectricCar**.     
| Set the car's **make**, **model**, **year**, **colour**. 
| The child class, ElectricCar, has a unique attribute, **battery_size**, and unique method, **get_battery_info**.
| The child class, ElectricCar, has a method, **fill_tank**, which overrides the method of the same name in its parent's class.

| Output:
| 2019 Grey Tesla Model S
| This car has a 90-kWh battery.
| Electric car's don't have a tank.

.. admonition:: Tasks

    #. Write a **ElectricCar** class as a child class of the **Car** class using the scaffold below.

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


            class ElectricCar(Car):
                """ElectricCar child of Car class."""
                
                def __init__(       , make, model, year, colour,          ):
                    """
                    Initialize attributes of the parent class.
                    Then initialize attributes specific to an electric car.
                    """
                           .__init__(make, model, year, colour)
                    self.battery_size

                def get_battery_info(      ):
                    print(f"This car has a {self.             }-kWh battery.")
                    
                def fill_tank(     ):
                    """Override parent method"""
                    print("No tank in this electric car.")
                    
            my_tesla = ElectricCar('tesla', 'model S', 2019, "grey", 90)
            print(my_tesla.get_info())
            my_tesla.get_battery_info()
            my_tesla.fill_tank()


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a **ElectricCar** class.

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


                    class ElectricCar(Car):
                        """ElectricCar child of Car class."""
                        
                        def __init__(self, make, model, year, colour, battery_size):
                            """
                            Initialize attributes of the parent class.
                            Then initialize attributes specific to an electric car.
                            """
                            super().__init__(make, model, year, colour)
                            self.battery_size = battery_size

                        def get_battery_info(self):
                            print(f"This car has a {self.battery_size}-kWh battery.")
                            
                        def fill_tank(self):
                            """Override parent method"""
                            print("No tank in this electric car.")
                            
                    my_tesla = ElectricCar('tesla', 'model S', 2019, "grey", 90)
                    print(my_tesla.get_info())
                    my_tesla.get_battery_info()
                    my_tesla.fill_tank()
