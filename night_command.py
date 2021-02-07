import random
alcohol= ["gin", "whiskey", "rum", "vodka", "wine", "tequilla", "brandy", "absinthe"]
mixers= ["coke", "sprite", "coffee", "tea", "ginger ale", "water", "cranberry juice"]
glass= ["rocks glass", "mug", "stein", "cracked teacup", "wine glass", "pint glass", "styrofoam cup", "solo cup", "drinking horn"]

def makeDrink(num1:int, num2:int, num3:int):
    alc=alcohol[num1]
    mix=mixers[num2]
    gla=glass[num3]
    return ("The bartender pours you "+alc+" with "+mix+" in a "+gla)

print (makeDrink(random.randint(0, len(alcohol)-1), random.randint(0, len(mixers)-1), random.randint(0, len(glass)-1))+". Delicious!")
