====================================================
Car Class
====================================================

| Write a **Car** class.  
| Set the car's **make**, **model**, **year**, **colour** on calling the Car class.
| Also set the **odometer** to 0.
| e.g. ``my_car = Car('ford', 'territory', 2005, "tan")``
| Write the methods, **get_info()** and **get_odometer()** to print a descriptive line, using f-strings.
| Write a method to **update** the odometer to a specified amount and a method to **increment** the odometer by a specified amount.

| Write code to ouput:
| 2005 Tan Ford Territory
| 2005 Tan Ford Territory has done 0 km.
| 2005 Tan Ford Territory has done 100000 km.
| 2005 Tan Ford Territory has done 100275 km.

.. admonition:: Tasks

    #. Write a **Car** class using the scaffold below.

        .. code-block:: python

            class Car:

                def __init__(self, make, model, year, colour):
                    self.      = make
                    self.      = model
                    self.       = year
                    self.       = colour
                    self.odometer =
                    
                def info(self):
                    return f"{       year} {      colour} {      make} {           model}".title()

                def get_info(self):
                    print(f"{self.info()}")

                def get_odometer(self):
                    print(f"{self.get_info()} has done {             } km.")

                def update_odometer(self, km):
                    """Set the odometer reading if km > current reading"""
                    if km >= self.odometer:
                        self. 
                    else: 
                        print("Km on an odometer can't be lowered.")

                def increment_odometer(self, km):
                    """increase the odometer reading"""
                    if km >= 0:
                        self. 
                    else:
                        print("Km on an odometer can't be lowered.")
                    
                
            my_car = Car('ford', 'territory', 2005, "tan")
            print(my_car.get_info())

            # update odometer using attribute
            my_car.                = 20
            my_car.get_odometer()

            # set odometer using method
            my_car.                 (100_000)
            my_car.get_odometer()

            # increment odometer using method
            my_car.                 (275)
            my_car.get_odometer()


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a class for a Car.

                .. code-block:: python

                    class Car:

                        def __init__(self, make, model, year, colour):
                            self.make = make
                            self.model = model
                            self.year = year
                            self.colour = colour
                            self.odometer = 0
                            
                        def info(self):
                            return f"{self.year} {self.colour} {self.make} {self.model}".title()

                        def get_info(self):
                            print(f"{self.info()}")

                        def get_odometer(self):
                            print(f"{self.info()} has done {self.odometer_reading} km.")

                        def update_odometer(self, km):
                            """Set the odometer reading if km > current reading"""
                            if km >= self.odometer:
                                self.odometer = km
                            else:
                                print("Km on an odometer can't be lowered.")

                        def increment_odometer(self, km):
                            """increase the odometer reading"""
                            if km >= 0:
                                self.odometer += km
                            else:
                                print("Km on an odometer can't be lowered.")
                            
                        
                    my_car = Car('ford', 'territory', 2005, "tan")
                    print(my_car.get_info())

                    # update odometer using attribute
                    my_car.odometer_reading = 20
                    my_car.get_odometer()

                    # set odometer using method
                    my_car.update_odometer(100_000)
                    my_car.get_odometer()

                    # increment odometer using method
                    my_car.increment_odometer(275)
                    my_car.get_odometer()

