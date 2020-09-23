# Plant a orange tree
# Wait for orange tree to grow
# When it is 3 years old
#   Orange tree will start to bear fruits
# When orange tree has fruits
# Pick all the oranges from the tree
import random

class Orange():
    def __init__(self):
        self.diameter = random.randrange(25,35,1)

class OrangeTree():
    def __init__(self):
        self.height=7
        self.age=15
        self.oranges = []


    def has_oranges(self):
        return len(self.oranges)>0

    def grow(self):
        self.height+=1
        self.age+=1
        for i in range(0,5):
            self.oranges.append(Orange())

    def alive(self):
        return self.age<30

    def pick_orange(self):
        return self.oranges.pop()



tree = OrangeTree()

while not tree.has_oranges():
    tree.grow()
    print(f"Tree is {tree.age} years old and {tree.height} feet tall")

while tree.alive():
    basket = []

    while tree.has_oranges():
        basket.append(tree.pick_orange())
        print(basket[0].diameter)
        avg_diameter = 0
    for orange in basket:
        avg_diameter += (orange.diameter)

    avg_diameter = avg_diameter/len(basket)
    print(f"Year {tree.age} Report")
    print(f"Tree Height: {tree.height} feet")
    print(f"Harvest: {len(basket)} oranges with an average diameter of {avg_diameter} inches")
    print(" ")

    tree.grow()

print('Alas, the tree, she is dead!')