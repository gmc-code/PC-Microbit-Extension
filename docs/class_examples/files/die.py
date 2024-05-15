from random import choice


class Die:
    """dice simulator"""

    def __init__(self, sides=6):
        self.sides = sides
        self.face_list = self.make_face_list(sides)

    def make_face_list(self, sides):
        face_list = [i for i in range(1, sides + 1)]
        return face_list

    def get_die(self):
        print(f"The die has sides: {self.face_list}")

    def roll_die(self):
        return choice(self.face_list)


class LoadedDie(Die):
    def __init__(self, sides=6, bias=6, bias_count=4):
        super().__init__(sides=6)
        self.face_list = self.make_face_list_biased(sides, bias, bias_count)

    def make_face_list_biased(self, sides, bias, bias_count):
        biased_list = [i for i in range(1, sides + 1)] + [bias] * bias_count
        return biased_list


die0 = Die(sides=6)
die0.get_die()
for i in range(36):
    print(die0.roll_die(), end=" ")

print("\n")
die6 = LoadedDie(sides=6, bias=6, bias_count=4)
die6.get_die()
for i in range(36):
    print(die6.roll_die(), end=" ")
