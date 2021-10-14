from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot_one = Robot()
        robot_two = Robot()
        robot_three = Robot()
        self.robots = [robot_one, robot_two, robot_three]
        self.fleet_arrival()

    def fleet_arrival(self):
        print("\nThe fleet has arrived to protect the citizens from the dinosaurs that have escaped their encloser!\n")
        self.robots[0].name = "Death-Bringer"
        self.robots[0].weapon_selection()
        self.robots[1].name = "Terminator"
        self.robots[1].weapon_selection()
        self.robots[2].name = "Viktor"
        self.robots[2].weapon_selection()

