class Worker:
    def __init__(self, employee_name, monthly_salary):
        self.employee_name = employee_name
        self.monthly_salary = monthly_salary


class TeamLead(Worker):
    def __init__(self, employee_name, monthly_salary, team_name):
        super().__init__(employee_name, monthly_salary)
        self.team_name = team_name

    def display_manager(self):
        print("Name:", self.employee_name)
        print("Salary:", self.monthly_salary)
        print("Department:", self.team_name)


# Create object
manager_obj = TeamLead("Marvin Joey", 111000, "IT Specialistt")

# Display info
manager_obj.display_manager()