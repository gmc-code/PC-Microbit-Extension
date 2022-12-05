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