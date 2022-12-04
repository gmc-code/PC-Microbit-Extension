====================================================
Restaurant inheritance
====================================================
    
| Write a **PizzaShop** class as a child class of the **Restaurant** class.
| Set the PizzaShop's **name**, **food type**, **open hours** on calling the PizzaShop class, as well as setting the **menu**.
| e.g. ``menu = ["Capricossa", "Hawaiian", "BBQ Chicken", "Pepperoni", "Margarita"]``
| e.g. ``res_1 = PizzaShop("Joe's Pizza", "Pizza", "6-10pm", menu)``
| Write a method, **show_menu()**, to print the PizzaShop's menu.

| Write code to ouput:
| Joe's Pizza serves Pizza food 6-10pm. 0 tables booked.
| Joe's Pizza has the following menu:
| 	- BBQ Chicken
| 	- Capricossa
| 	- Hawaiian
| 	- Margarita
| 	- Pepperoni


.. admonition:: Tasks

    #. Write a **PizzaShop** class as a child class of the **Restaurant** class using the scaffold below.

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


            class PizzaShop(Restaurant):
                '''child class of Restaurant'''
                
                def __init__(self, restaurant_name, food_type, open_hours, menu):
                             .__init__(              ,          ,           )
                    self.menu = 
                
                def show_menu(self):
                    print(f"\n{self.                } has the following menu:")
                    for menu_item in sorted(self.     ):
                        print(f"\t- {          }")


            # instantiate Restaurant
            menu = ["Capricossa", "Hawaiian", "BBQ Chicken", "Pepperoni", "Margarita"]
            res_1 = PizzaShop("Joe's Pizza", "Pizza", "6-10pm", menu)
            res_1.get_info()
            res_1.show_menu()


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a **Restaurant** class.

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


                    class PizzaShop(Restaurant):
                        '''child class of Restaurant'''
                        
                        def __init__(self, restaurant_name, food_type, open_hours, menu):
                            super().__init__(restaurant_name, food_type, open_hours)
                            self.menu = menu
                        
                        def show_menu(self):
                            print(f"\n{self.restaurant_name} has the following menu:")
                            for menu_item in sorted(self.menu):
                                print(f"\t- {menu_item}")


                    # instantiate Restaurant
                    menu = ["Capricossa", "Hawaiian", "BBQ Chicken", "Pepperoni", "Margarita"]
                    res_1 = PizzaShop("Joe's Pizza", "Pizza", "6-10pm", menu)
                    res_1.get_info()
                    res_1.show_menu()
