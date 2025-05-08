#understanding decorators 
from typing import List



def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("something you want to happen before  your actual function")
        func(*args, **kwargs)
        print("something  you want to happen after func")
    return wrapper





@my_decorator
#start from here 
#so we have a function 
def func(x:str) -> str:
    print(f"First function (orignal instance)paremeter : {x}  ")
    return ""
    





func("john")