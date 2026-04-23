student_name = input("Enter student name: ")
program = input("Enter course: ")

with open("students.txt", "a") as file_handle:
    file_handle.write(student_name + "," + program + "\n")

print("\nList of Students")

with open("students.txt", "r") as reader:
    for record in reader:
        print(record.strip())