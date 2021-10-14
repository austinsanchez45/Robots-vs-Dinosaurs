from weapon import Weapon

class Robot:
    def __init__(self):
        self.name = ""
        self.health = 0
        self.weapon = Weapon()

    def attack(self, dinosaur):
        print(f"\n{self.name} blasts the {dinosaur.name} with their {self.weapon}!")
        dinosaur.health -= self.weapon.attack_power
        print(f"\n{dinosaur.name} has {dinosaur.health} HP remaining!")
        if dinosaur.health <= 0:
            dinosaur.alive = False

    def weapon_selection(self):
        weapon_choice = input(f"""\nWhich weapon would you like to use for {self.name}?
        \n1: Plasma Rifle: Attack Power - 20
        \n2: Sword: Attack Power - 15
        \n3: Railgun: Attack Power - 50
        \n""")
        self.weapon.weapons(weapon_choice)