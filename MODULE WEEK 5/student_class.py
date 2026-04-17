class Student:
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course

    
    def display_student(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Course:", self.course)


student1 = Student("Mj", "24-000-3321", "BSIS")


student1.display_student()