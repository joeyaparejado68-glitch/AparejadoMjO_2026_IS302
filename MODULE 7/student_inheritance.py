class Human:
    def __init__(self, full_name, years_old):
        self.full_name = full_name
        self.years_old = years_old


class Learner(Human):
    def __init__(self, full_name, years_old, program):
        super().__init__(full_name, years_old)
        self.program = program

    def display_student(self):
        print("Name:", self.full_name)
        print("Age:", self.years_old)
        print("Course:", self.program)


# Create object
student_obj = Learner("Marvin Joey A", 19, "BSIS")

# Display info
student_obj.display_student()