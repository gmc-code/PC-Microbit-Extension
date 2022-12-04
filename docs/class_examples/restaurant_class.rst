====================================================
Restaurant Class
====================================================
    
| Write a **Restaurant** class.
| Set the Restaurant's **name**, **food type**, **open hours** on calling the Restaurant class, as well as setting the number of **tables booked** to 0.
| e.g. ``res_1 = Restaurant("Pierre's", "French", "6-10pm")``
| Write a method, **get_info()**, to print a descriptive line, using f-strings: 
| Write a method to set the number of tables booked and a method to increment them.

| Write code to ouput:
| Pierre's serves French food 6-10pm. 8 tables booked.
| Louie's Bistro serves Italian food 10am - 2pm. 6 tables booked.

.. admonition:: Tasks

    #. Write a **Restaurant** class using the scaffold below.

        .. code-block:: python

            class Restaurant:

                def __init__(self, restaurant_name, food_type, open_hours):
                    self.
                    self.
                    self.
                    self.tables_booked
                    
                def get_info(self):
                    print(f"{          } serves {       } food {        }.")
                    print(f"{        } tables booked.")

                def set_number_tables_booked(self, tables_booked):
                    '''Set the number of tables booked'''
                    self.
                
                def increment_number_tables_booked(self, new_bookings):
                    '''Increment the number of tables booked'''
                    self.tables_booked
                    
            # instantiate 2 Restaurants
            res_1 = Restaurant("Pierre's", "French", "6-10pm")
            res_1.set_number_tables_booked(8)
            res_1.get_info()

            res_2 = Restaurant("Louie's Bistro", "Italian", "10am - 2pm")
            res_2.set_number_tables_booked(4)
            res_2.increment_number_tables_booked(2)
            res_2.get_info()


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a class for a Restaurant.

                .. code-block:: python

                    class Restaurant:

                        def __init__(self, restaurant_name, food_type, open_hours):
                            self.restaurant_name = restaurant_name
                            self.food_type = food_type
                            self.open_hours = open_hours
                            self.tables_booked = 0
                            
                        def get_info(self):
                            print(f"{self.restaurant_name} serves {self.food_type} food {self.open_hours}.")
                            print(f"{self.tables_booked} tables booked.")

                        def set_number_tables_booked(self, tables_booked):
                            '''Set the number of tables booked'''
                            self.tables_booked = tables_booked
                        
                        def increment_number_tables_booked(self, new_bookings):
                            '''Increment the number of tables booked'''
                            self.tables_booked += new_bookings
                            
                    # instantiate 2 Restaurants
                    res_1 = Restaurant("Pierre's", "French", "6-10pm")
                    res_1.set_number_tables_booked(8)
                    res_1.get_info()

                    res_2 = Restaurant("Louie's Bistro", "Italian", "10am - 2pm")
                    res_2.set_number_tables_booked(4)
                    res_2.increment_number_tables_booked(2)
                    res_2.get_info()
