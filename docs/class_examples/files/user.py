class User:
    def __init__(self, first_name, last_name, user_privileges):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = Privileges(user_privileges)
        self.logins = 0

    def get_privileges(self):
        return self.privileges.get_privileges()

    def get_info(self):
        print(f"{self.first_name} {self.last_name} is a {self.get_privileges()}.")

    def greet_user(self):
        print(f"Welcome, {self.first_name}!")

    def get_login_info(self):
        print(f"{self.first_name} {self.last_name} has logged in {self.logins} times.")

    def increment_logins(self):
        self.logins += 1
        print(f"logins: {self.logins}")

    def reset_logins(self):
        self.logins = 0
        print(f"logins: {self.logins}")


class Privileges:
    def __init__(self, privileges="Subscriber"):
        self.privileges_list = [
            "Administrator",
            "Editor",
            "Author",
            "Contributor",
            "Subscriber",
        ]
        if privileges in self.privileges_list:
            self.privileges = privileges
        else:
            self.privileges = "Subscriber"

    def get_privileges(self):
        return self.privileges


user1 = User("Tim", "Lang", "Contributor")
user1.greet_user()
user1.get_info()
