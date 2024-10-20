

class Dinosaur:
    def __init__(self,name,sex,age):
        self.__name = name
        self.__sex = sex
        self.__age = age
        self.__egg = []


    def lay_egg(self):
        from egg import Egg

        if self.__sex == "Female" and self.__age >= 4:
            self.__egg = Egg(self.__class__.__name__)
            print(f"{self.__class__.__name__}")
        else:
            print(f"This dinosaur can not lay egg")
        

    def warm_egg(self):
        if self.__egg:
            baby_din = self.__egg.hatch()
            print(f" one baby {self.__egg} has hatched !")
            return baby_din
        else:
            print(f"No egg to hatch!")

    def name_baby(self,baby_din,baby_name):
        self.baby_din = baby_din
        self.baby_name = baby_name
        if self.__egg:
            return f"{self.baby_name}"
        else:
            print(f"No name for baby")
    

    def __str__(self):
        if self.__name:
            return f"{self.__class__.__name__} is a {self.__sex}, age {self.__age}.\n" \
                f"They are named {self.__name}."
        else:
            return f"{self.__class__.__name__} is a {self.__sex}, age{self.__age}. \n" \
            f"They haven't been named, yet!"
            
        
        




