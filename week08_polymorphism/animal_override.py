class Creature:
    def make_noise(self):
        print("Creature produces a sound")

class Canine(Creature):
    def make_noise(self):
        print("Canine howls")

class Feline(Creature):
    def make_noise(self):
        print("Feline purrs")

pet_list = [Canine(), Feline()]

for pet in pet_list:
    pet.make_noise()