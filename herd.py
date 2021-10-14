from dinosaur import Dinosaur

class Herd:
    def __init__(self) :
        self.dinosaurs = []

    def create_herd(self):
            dinosaur_one = Dinosaur()
            dinosaur_two = Dinosaur()
            dinosaur_three = Dinosaur()
            self.dinosaurs = [dinosaur_one, dinosaur_two, dinosaur_three]
            self.herd_attacking()

    def herd_attacking(self):
        print("\n Oh no! The dinosaurs have broken out of their enclosures and are attacking people!")
        self.dinosaurs[0].dinosaurs_attacking(0)
        self.dinosaurs[1].dinosaurs_attacking(1)
        self.dinosaurs[2].dinosaurs_attacking(2)
    