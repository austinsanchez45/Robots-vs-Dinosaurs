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
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self, winners):
        if winners == "Dinosaurs":
            print("\nThe dinorsaurs have destroyed the robots and now have infested the island!")
        elif winners == "Robots":
            print("\nThe robots have stopped the dinosaurs from rampaging and peace has returned to the island!")


    

    


    