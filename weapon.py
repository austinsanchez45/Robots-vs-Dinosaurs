class Weapon:
    def __init__(self, name, attack_power):
        self.name = ""
        self.attack_power = 0

    def weapons(self, weapon):
        if weapon == 1:
            self.name = "Plasma Rifle"
            self.attack_power = 20
        elif weapon == 2:
            self.name = "Sword"
            self.attack_power = 15
        elif weapon == 3:
            self.name = "Railgun"
            self.attack_power = 50