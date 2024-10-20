from dinosaur import Dinosaur

din1 = Dinosaur("Dino","male",5)
din1.lay_egg()
baby1 = din1.warm_egg()
print(baby1)
print(isinstance(din1,Dinosaur))
print(type(din1) == Dinosaur)
