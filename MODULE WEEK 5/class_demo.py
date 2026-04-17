class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


p1 = Person("Mj", 19)


p1.display_info()