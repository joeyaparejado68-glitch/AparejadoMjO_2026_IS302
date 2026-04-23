class Puppy:
    def make_sound(self):
        print("Puppy woofs")

class Kitten:
    def make_sound(self):
        print("Kitten purrs")

pets = [Puppy(), Kitten()]

for pet in pets:
    pet.make_sound()