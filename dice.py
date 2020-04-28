import random


class Dice:

    def roll(self):
        mytuple = (random.randint(0, 9), random.randint(0, 9))

        return mytuple


dic = Dice()
print(dic.roll())
