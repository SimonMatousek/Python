class Animal:
    def __init__ (self) -> None:
        self.hunger = 50
        self.thirst = 50
        
    def drink(self) -> None:
        self.thirst -= 1
    def eat(self):
        self.hunger -= 1
    def play(self):
        self.hunger += 1
        self.thirst += 1
        
if __name__ == "__main__":
    panther = Animal()
    print(panther.hunger)
    print(panther.thirst)
    panther.drink()
    panther.eat()
    print(panther.hunger)
    print(panther.thirst)
    panther.play()
    print(panther.hunger)
    print(panther.thirst)
    
