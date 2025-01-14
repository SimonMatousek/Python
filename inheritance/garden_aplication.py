class Flower:
    def __init__(self, color):
        self.water_ammount = 0
        self.color = color
    def needs_water(self):
        if self.water_ammount < 5:
            print("The" + self.color + " Flower needs Water")
        else:
            print("The" + self.color + " Flower doesnt need Water")
    def watering(self):
        self.water_ammount += 0.75

class Tree:
    def __init__(self, color):
        self.color = color
        self.water_ammount = 0
    def needs_water(self):
        if self.water_ammount < 10:
            print("The" + self.color + " tree needs water")
        else:
            print("The" + self.color + " tree doesnt need water")
    def watering(self, water = int):
        self.water_ammount += water * 0.4

class Garden:
    def __init__(self,):
        self.list_of_flower = []
        self.list_of_tree = []
    
    def add_flower(self, flower = Flower):
        self.list_of_flower.append(flower)
    def add_tree(self, tree = Tree):
        self.list_of_tree.append(tree)
    def watering(self,ammount):
        flower_water = 0
        tree_water = 0
        for idx, flower in enumerate(self.list_of_flower):
            if flower.water_ammount < 5:
                flower_water += 1
        for idx, tree in enumerate(self.list_of_tree):
            if tree.water_ammount < 5:
                tree_water += 1
        ammount /= flower_water + tree_water
        for idx, flower in enumerate(self.list_of_flower):
            if flower.water_ammount < 5:
                flower.water_ammount += ammount * 0.75
        for idx, tree in enumerate(self.list_of_tree):
            if (tree.water_ammount < 10):
                tree.water_ammount += ammount * 0.4
if __name__ == "__main__":
    flower1 = Flower("yellow")
    flower2 = Flower("blue")
    tree1 = Tree("purple")
    tree2 = Tree("orange")
    
    garden = Garden()
    
    garden.add_flower(flower1)
    garden.add_flower(flower2)
    garden.add_tree(tree1)
    garden.add_tree(tree2)
    
    garden.watering(40)
    flower1.needs_water()
    flower2.needs_water()
    tree1.needs_water()
    tree2.needs_water()
    
    garden.watering(70)
    flower1.needs_water()
    flower2.needs_water()
    tree1.needs_water()
    tree2.needs_water()