class LivingThing:
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def speak(self):
        print(self.animal_name, "makes a sound")


class CatAnimal(LivingThing):
    def meow(self):
        print(self.animal_name, "meows")


# Create object
pet_cat = CatAnimal("Mimi")

# Call methods
pet_cat.speak()
pet_cat.meow()