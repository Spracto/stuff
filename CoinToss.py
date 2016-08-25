import random

print "How many times would you like to flip a coin?"
flip_num = input()

x = 1
heads = 0
tails = 0

while x <= flip_num:
    y = random.choice([0, 1])
    if y == 0:
        heads = heads + 1
        print "Attempt #" + str(x), ": Throwing a coin... It's a head!... Got " +str(heads), "head(s) so far and " +str(tails), "so far"
        x = x + 1
    elif y == 1:
        tails = tails + 1
        print "Attempt #" + str(x), ": Throwing a coin... It's a tail!... Got " + str(heads), "head(s) so far and " + str(tails), "so far"
        x = x + 1

print "Ending the program, thank you!"
