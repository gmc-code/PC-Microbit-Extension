class Employee:
    def __init__(self, firstname, lastname, monthly_income, bonus_rate):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = Salary(monthly_income=monthly_income, bonus_rate=bonus_rate)

    def get_employee(self):
        print(f"Name: {self.firstname + self.lastname}.")
        print(f"Salary: ${self.salary.get_total_salary()}")


class Salary:
    def __init__(self, monthly_income, bonus_rate):
        self.monthly_income = monthly_income
        self.bonus_rate = bonus_rate

    def get_annual_salary(self):
        return self.monthly_income * 12

    def get_bonus(self):
        return self.monthly_income * self.bonus_rate / 100

    def get_total_salary(self):
        return f'{self.get_annual_salary() + self.get_bonus():.2f}'


emp1 = Employee(firstname="Tim", lastname="Lang", monthly_income=8000, bonus_rate=5)
emp1.get_employee()
