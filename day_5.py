##Day-5

class Animals():
    def __init__(self, animalName, animalAge, animalGender, animalColour, animalSpecies):
        self.name = animalName
        self.age = animalAge
        self.gender = aanimalGender
        self.colour = animalColour
        self.species = animalSpecies
    
    def call(self):
        print("Hello there " + self.name + "come here")
        
    def color(self):
        print("Come my little " + self.colour + "one")
    
    def spec(self):
        print("It is a" + self.species)


class Dogs(Animals):
    def __init__(self, animalName, animalAge, animalGender, sound):
        super().__init__(animalName, animalAge, animalGender)
        self.sound = sound

    def dog_info(self):
        print(self.animalName + "is a good dog " + "It is " + self.animalAge + "and" + self.animalGender + "It loves " + self.sound)
        
    
class Cats(Animals):
    def __init__(self, sound):
        super().__init__(animalName, animalAge, animalGender, animalColour, animalSpecies)
        self.sound = sound
        
    
    def cat_info(self):
        print(self.animalName + "is a combative " + "It is " + self.animalAge + "and" + self.animalGender + "It is also a " + self.animalColour + "It is " + self.animalSpecies + "When it sees me, it loves to " + self.sound)


new_cat = Cats("Şimşek", "5", "Male", "black", "tekir", "miyav")
dir(new_cat)
new_cat.cat_info()
