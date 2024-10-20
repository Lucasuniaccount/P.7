from dinosaur import Dinosaur

class Carnivore(Dinosaur):
    def hunt(self):
        return f"{self.__class__.__name__} is hunting for meat"