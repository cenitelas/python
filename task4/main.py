import random


class Samuray():

    def __init__(self, hp, armor, power, accuracy, agility):
        self.hp = hp
        self.armor = armor
        self.power = power
        self.accuracy = accuracy
        self.agility = agility

    def attack(self, samuray):
        samuray.hp = samuray.hp - ((self.power + self.agility) * random.randint(1, self.accuracy)/samuray.armor)


class CombatSamuray():

    def __init__(self, samuray1, samuray2):
        self.samuray1 = samuray1
        self.samuray2 = samuray2

    def go(self):
        while True:
            if self.samuray1.hp > 0:
                self.samuray1.attack(self.samuray2)
                print(f"Самурай 1 атакует Самурай 2:")
                print(f"Самурай 2 HP ={self.samuray2.hp}")
            else:
                print(f"Самурай 2 выйграл Самурай 1:")
                print(f"Самурай 1 HP = 0")
                print(f"Самурай 2 HP ={self.samuray2.hp}")
                break

            if self.samuray2.hp > 0:
                self.samuray2.attack(self.samuray1)
                print(f"Самурай 2 атакует Самурай 1:")
                print(f"Самурай 1 HP ={self.samuray1.hp}")
            else:
                print(f"Самурай 1 выйграл Самурай 2:")
                print(f"Самурай 1 HP ={self.samuray1.hp}")
                print(f"Самурай 2 HP = 0")
                break

def main():
    sam1 = Samuray(100, 100, 30, 5, 3)
    sam2 = Samuray(100, 100, 30, 5, 2)
    combat = CombatSamuray(sam1, sam2)
    combat.go()


main()
