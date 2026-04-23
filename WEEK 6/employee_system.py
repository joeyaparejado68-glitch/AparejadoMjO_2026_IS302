class Employee:
    def __init__(self, employee_name):
        self.__employee_name = employee_name
        self.__monthly_pay = 0

    def set_salary(self, amount):
        if amount > 0:
            self.__monthly_pay = amount
        else:
            print("Invalid salary")

    def get_salary(self):
        return self.__monthly_pay


# Create employee object
staff1 = Employee("MJA")

# Set salary
staff1.set_salary(30000)

# Display salary
print("Salary:", staff1.get_salary())