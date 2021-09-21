import random

# Defines a function to allow user to roll one standard 6-sided die.
def rollD6():
  rolled = random.randint(1,6)
  return(rolled)

# defines a funtion that uses the previous funtction to roll a D6 4 times.
def roll4d6():
    rolls = []
    counter = 0
    while counter < 4:
        rolled = rollD6()
        rolls.append(rolled)
        counter += 1
    print(rolls)
