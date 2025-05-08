# R-1.12 Python’s random module includes a function choice(data) that returns a random element from
# a non-empty sequence. The random module includes a more basic function randrange, with 
# parameterization similar to the built-in range function, that return a random choice 
# from the given range. Using only the randrange function, implement your own version of the choice function.


import random
from typing import List 


list = [1,3,4,5,6,8,7,86,5,44,34,2,2,42,5,3,63,456,4,645,65,7,34,3,45,2,3,123,1,4,354,6,7,6,7,654,32]


def choice(lst):
    if not lst:
        print("we dont allow empty list")
    rand = random.randrange(len(lst))
    return lst[rand]







print(choice(list))






