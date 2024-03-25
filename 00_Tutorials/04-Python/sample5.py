class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def greet(self):
        print(f"Hi! My name is {self.name} and I am a {self.species}")
        
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name=name, species="cat")
        self.name = name
    
    def sound(self):
        print("Miwow")
        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name=name, species="dog")
        self.name = name
        
    def sound(self):
        print("Ruff")
        