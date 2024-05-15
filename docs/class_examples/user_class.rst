====================================================
User Class
====================================================
    
| Write a **User** class.
| Set the User's **first_name**, **last_name**, **user_status** on calling the User class, as well as setting the number of **logins** to 0.
| Write the methods, **get_info()** and **get_login_info(self)** to print a descriptive line, using f-strings.
| Write a greeting method, **greet_user()**.
| Write a method to **reset** the number of logins and a method to **increment** them.

| Write code to ouput:
| Welcome, Tim!
| Tim Lang is a Subscriber.
| Tim Lum has logged in 2 times.
| Tim Lum has logged in 0 times.

.. admonition:: Tasks

    #. Write a **User** class using the scaffold below.

        .. code-block:: python

            class User:

                def __init__(self, first_name, last_name, user_status):
                    self.first_name = 
                    self.last_name = 
                    self.user_status = 
                    self.logins = 

                def get_info(self):
                    print(f"{       first_name} {      last_name} is a {      user_status}.")

                def get_login_info(self):
                    print(f"{     first_name} {      last_name} has logged in {     logins} times.")

                def greet_user(self):
                    print(f"Welcome, {      first_name}!")

                def increment_logins(self):
                    self.logins += 1

                def reset_logins(self):
                    self.logins = 0
                    
                    
            user_1 = User("Tim", "Lang", "Subscriber")
            user_1.greet_user()
            user_1.get_info()
            user_1.increment_logins()
            user_1.increment_logins()
            user_1.get_login_info()
            user_1.reset_logins()
            user_1.get_login_info()


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a class for a User.

                .. code-block:: python

                    class User:

                        def __init__(self, first_name, last_name, user_status):
                            self.first_name = first_name
                            self.last_name = last_name
                            self.user_status = user_status
                            self.logins = 0

                        def get_info(self):
                            print(f"{self.first_name} {self.last_name} is a {self.user_status}.")

                        def get_login_info(self):
                            print(f"{self.first_name} {self.last_name} has logged in {self.logins} times.")

                        def greet_user(self):
                            print(f"Welcome, {self.first_name}!")

                        def increment_logins(self):
                            self.logins += 1

                        def reset_logins(self):
                            self.logins = 0
                            
                            
                    user_1 = User("Tim", "Lang", "Subscriber")
                    user_1.greet_user()
                    user_1.get_info()
                    user_1.increment_logins()
                    user_1.increment_logins()
                    user_1.get_login_info()
                    user_1.reset_logins()
                    user_1.get_login_info()


