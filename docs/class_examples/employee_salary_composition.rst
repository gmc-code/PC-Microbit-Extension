====================================================
Employee Salary Composition  
====================================================

| See: https://www.geeksforgeeks.org/inheritance-and-composition-in-python/
| See: https://medium.com/swlh/the-best-way-to-understand-composition-in-python-5-case-studies-and-solution-4b23a6a2cc38

----

Composition
-----------------

| Composition models a has-a-relationship.
| Use composition to create components that can be reused by multiple classes.
| A composite class can be assigned to an instance variable.

| In the code below, ``self.salary = Salary(monthly_income=monthly_income, bonus_rate=bonus_rate)``, the composite class, ``Salary``, is assigned to an instance variable, ``self.salary``.
| The Salary method, ``get_total_salary()``, can be called from the instance variable: ``self.salary.get_total_salary()``.

----

Employee Salary
-----------------

.. admonition:: Tasks

    #. Write a **Salary** class to be assigned to a variable in the **Employee** class using the scaffold below.

        .. code-block:: python
                    
            class Employee:
                def __init__(self, firstname, lastname, monthly_income, bonus_rate):
                    self.firstname = firstname
                    self.lastname = lastname
                    self.salary =         (monthly_income=              , bonus_rate=         )

                def get_employee(self):
                    print(f"Name: {self.firstname + self.lastname}.")
                    print(f"Salary: ${self.salary.get_total_salary()}")


            class Salary:
                def __init__(self,            ,                 ):
                    self.monthly_income = monthly_income
                    self.bonus_rate = bonus_rate

                def get_annual_salary(self):
                    return self.monthly_income * 12

                def get_bonus(self):
                    return self.monthly_income * self.bonus_rate / 100

                def get_total_salary(self):
                    return f'{self.                  () + self.get_bonus():.2f}'


            emp1 = Employee(firstname="Tim", lastname="Lang", monthly_income=8000, bonus_rate=5)
            emp1.get_employee()

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a **Salary** class to be assigned to a variable in the **Employee** class using the scaffold below.

                .. code-block:: python
                            
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