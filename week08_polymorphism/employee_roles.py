class Staff:
    def perform_job(self):
        print("Staff handles responsibilities")

class Coder(Staff):
    def perform_job(self):
        print("Coder develops programs")

class Illustrator(Staff):
    def perform_job(self):
        print("Illustrator creates designs")

workers = [Coder(), Illustrator()]

for person in workers:
    person.perform_job()