"""
Compute and print powerball numbers.
"""

import random

def powerball():
    #To create a list of random numbers without duplicates with Python,use the random.sample method.
    r1 = random.sample(range(1,69), 5)
    #The randrange() method returns a randomly selected element from the specified range.
    r2 = random.randrange(1,26)
    result = "Today's numbers are {}, {}, {}, {} and {}. The powerball number is {}.".format(r1[0],r1[1],r1[2],r1[3],r1[4],r2)
    print(result)

powerball()
