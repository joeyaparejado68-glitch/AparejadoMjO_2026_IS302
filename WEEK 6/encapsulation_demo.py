class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


# Create object
p1 = Person("MJA", 19)

# Display output
print("Name:", p1.get_name())
print("Age:", p1.get_age())