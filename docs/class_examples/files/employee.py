class Employee:
    def __init__(self, first_name, last_name, monthly_income, bonus_rate):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = Salary(monthly_income=monthly_income, bonus_rate=bonus_rate)

    def get_employee(self):
        print(f"Name: {self.first_name + self.last_name}.")
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


emp1 = Employee(first_name="Tim", last_name="Lang", monthly_income=8000, bonus_rate=5)
emp1.get_employee()
