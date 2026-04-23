class HumanBeing:
    def __init__(self, full_name, years_old):
        self.full_name = full_name
        self.years_old = years_old


class StudentUser(HumanBeing):
    def __init__(self, full_name, years_old, program_course):
        super().__init__(full_name, years_old)
        self.program_course = program_course

    def display_info(self):
        print("Student Name:", self.full_name)
        print("Age:", self.years_old)
        print("Course:", self.program_course)


class TeacherUser(HumanBeing):
    def __init__(self, full_name, years_old, teaching_subject):
        super().__init__(full_name, years_old)
        self.teaching_subject = teaching_subject

    def display_info(self):
        print("Teacher Name:", self.full_name)
        print("Age:", self.years_old)
        print("Subject:", self.teaching_subject)


# Create objects
student_obj = StudentUser("Mr MJ", 19, "BSIS")
teacher_obj = TeacherUser("Mr. Joshua", 18, "Mathematics")

# Display information
student_obj.display_info()
print("---")
teacher_obj.display_info()