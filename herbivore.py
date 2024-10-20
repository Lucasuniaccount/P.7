from dinosaur import Dinosaur

class Herbivore(Dinosaur):
    def forage(self):
        return f"{self.__class__.__name__} is foraging for plants"
    