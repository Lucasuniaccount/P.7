

import random
from dinosaurs import Triceratops, Oviraptor, TyrannosaurusRex


class Egg:
    def __init__(self, type):
        self.__type = type

    def hatch(self):
        sex = random.choice(["Male", "Female"])

        match self.__type:
            case "TyrannosaurusRex":
                return TyrannosaurusRex("", sex, 0)
            case "Triceratops":
                return Triceratops("", sex, 0)
            case "Oviraptor":
                return Oviraptor("", sex, 0)
            case default:
                return "What chimken is this?!?"

    def __str__(self):
        return f"This egg will hatch into a baby {self.__type}"
