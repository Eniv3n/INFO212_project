import random

def rollD6():
  rolled = random.randint(1,6)
  return(rolled)


def roll4d6():
    rolls = []
    counter = 0
    while counter < 4:
        rolled = rollD6()
        rolls.append(rolled)
        counter += 1
    print(rolls)
