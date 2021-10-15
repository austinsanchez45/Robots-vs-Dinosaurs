from herd import Herd
from fleet import Fleet
import keyboard

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_battle(self):
        game_start = self.display_welcome()
        if game_start:
            play_again = "Yes"
            while play_again == "Yes":
                self.herd.create_herd()
                self.fleet.create_fleet()
                self.display_winners(self.battle())
                play_again = input("\nDo you want to play again(Yes or No)? ")
                

    def display_welcome(key):
        game_start = keyboard.read_key(input("""
        \nRobots VS Dinosaurs
        \nPress Enter to begin!
        \n"""))
        if  game_start == keyboard.is_pressed("Enter"):
            return True
        else:
            return False

    def battle(self):
        game_continue = True
        while game_continue:
            game_continue = self.dino_turn(self.show_dino_opponent_options(), self.show_dino_opponent_options())
            if game_continue == False:
                return "Dinosaurs"
            game_continue = self.robo_turn(self.show_robo_opponent_options(), self.show_robo_opponent_options())
            if game_continue == False:
                return "Robots"

    def dino_turn(self, dinosaur, robot):
        self.herd.dinosaurs[dinosaur].attack(self.fleet.robots[robot])
        for robo in self.fleet.robots:
            if robo.alive == True:
                return True
        return False

    def robo_turn(self, robot, dinosaur):
        self.fleet.robots[robot].attack(self.herd.dinosaurs[dinosaur])
        for dino in self.herd.dinosaurs:
            if dino.alive == True:
                return True
        return False

    def show_dino_opponent_options(self):
        invalid_target = True
        while invalid_target:
            player_target = int(input("""
            \nPick your dinosaurs target to attack!
            \n1: {self.fleet.robots[0].name} with {self.fleet.robots[0].health} HP
            \n2: {self.fleet.robots[1].name} with {self.fleet.robots[1].health} HP
            \n3: {self.fleet.robots[2].name} with {self.fleet.robots[2].health} HP
            \n""")) - 1
            if self.fleet.robots[player_target].alive:
                return player_target
            elif self.fleet.robots[player_target].alive == False:
                print(f"{self.fleet.robots[player_target].name} is already destroyed! Choose another target!")
            else:
                print("Invalid input. Try again.")

    def show_robo_opponent_options(self):
        invalid_target = True
        while invalid_target:
            player_target = int(input("""
            \nPick your robots target to attack!
            \n1: {self.herd.dinosaurs[0].name} with {self.herd.dinosaurs[0].health} HP
            \n2: {self.herd.dinosaurs[1].name} with {self.herd.dinosaurs[1].health} HP
            \n3: {self.herd.dinosaurs[2].name} with {self.herd.dinosaurs[2].health} HP
            \n""")) - 1
            if self.herd.dinosaurs[player_target].alive:
                return player_target
            elif self.herd.dinosaurs[player_target].alive == False:
                print(f"{self.herd.dinosaurs[player_target].name} has already been stopped! Choose another target!")
            else:
                print("Invalid input. Try again.")

    def display_winners(self, winners):
        if winners == "Dinosaurs":
            print("\nThe dinorsaurs have destroyed the robots and now have infested the island!")
        elif winners == "Robots":
            print("\nThe robots have stopped the dinosaurs from rampaging and peace has returned to the island!")


    

    


    