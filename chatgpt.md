## query :
create a function named roll_dice  The input to roll_dice is an integer between 1 and 6.
The output of roll_dice is a tuple with random values between 1 and 6.
The length of tuple must match the argument given to roll_dice method.

## result:
import random

def roll_dice(num_dice):
    return tuple(random.randint(1, 6) for _ in range(num_dice))