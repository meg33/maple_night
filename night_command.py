import random
alcohol= ["gin", "whiskey", "rum", "vodka", "red wine", "tequilla", "brandy", "absinthe", "port", "sake", "rye", "schnapps", "mezcal", "aquavit", "beer", "cider", "toilet wine", "bathtub gin", "white wine", "fireball", "jagermeister", "whipped cream vodka", "hennessy", "coconut rum", "white whiskey", "cherry brandy", "champagne", "sambuca", "everclear", "ouzo", "mead", "blackberry cordial", "double chocolate bourbon", "jalapeno tequilla", "moonshine", "screech"]
mixers= ["orange juice", "coke", "sprite", "coffee", "tea", "ginger ale", "water", "cranberry juice", "soda", "ice", "vermouth", "kahlua", "mountain dew", "pickle juice", "yellow gatorade", "NOTHING", "apple cider", "coconut cream", "grenadine", "pineapple juice", "iced tea", "cream", "root beer", "chocolate milk", "lemonade", "kool-aid", "white claw", "apple juice", "hot sauce", "honey", "tonic", "banana liqueur", "triple sec", "a pickled toe", "a chicken wing", "some mint", "a sprig of rosemary"]
glass= [" boot", " martini glass", " coffee mug", " stein", " cracked teacup", " wine glass", " pint glass", " styrofoam cup", " drinking horn", " highball glass", " shot glass", " novelty disney glass", " dogbowl", " tupperware container", " skull of your enemy", " flute", " goblet", " holy grail", " Tim Horton's cup", " hurricane glass", "n acorn", " coupe glass", " rocks glass", " margarita glass", " beer helmet", " fancy hat", " copper mug", " tiki cup", " mason jar", "n eggshell", " tin can", " beaker", " light bulb", " plastic beach bucket", " flowerpot", " plastic bag", "n old milk bottle"]

def makeDrink(num1:int, num2:int, num3:int):
    alc=alcohol[num1]
    mix=mixers[num2]
    gla=glass[num3]
    return ("The bartender pours you "+alc+" with "+mix+" in a"+gla)

print (makeDrink(random.randint(0, len(alcohol)-1), random.randint(0, len(mixers)-1), random.randint(0, len(glass)-1))+". Delicious!")
