import random


class Die:
    def __init__(self):
        self.sides = 6

    def roll_die(self):
        number = random.randint(1, self.sides)
        print(f"Number: {number}")

die = Die()

for x in range(10):
    die.roll_die()