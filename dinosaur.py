class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = ""
        self.attack_power = 0
        self.health = 0
        self.alive = True
        self.attack_name = ("Bite", "Stomp", "Beak Spear", "Jump Crash", "Tail Crash")

    def attack(self, robot):
        self.dinosaurs_attacking(robot)
        robot.health -= self.attack_power
        print(f"\n{robot.name} has {robot.health} HP remaining!")
        if robot.health <= 0:
            robot.alive = False

    def dinosaurs_attacking(self, robot):
        dinosaur_attack = int(input(f"""\nWhat attack would you like you use?
        \n1: {self.attack_name[0]}
        \n2: {self.attack_name[1]}
        \n3: {self.attack_name[2]}
        \n4: {self.attack_name[3]}
        \n5: {self.attack_name[4]}
        \n""")) - 1
        print(f"\nThe {self.name} viciously attacks {robot.name} with a {self.attack_name[dinosaur_attack]}!")

    def dinosaur_types(self, dinosaur_number):
        dinosaur_names = ["Allosaurus", "Pteranodon", "Spinosaurus"]
        dinosaur_health = [75, 60, 125]
        dinosaur_attack = [30, 20, 60]
        self.name = dinosaur_names[dinosaur_number]
        self.health = dinosaur_health[dinosaur_number]
        self.attack_power = dinosaur_attack[dinosaur_number]
