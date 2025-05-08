import click
from typing import List



def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print('*You add Sprinkles*')
        func(*args, **kwargs)
    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*here is your fudge*")
        func(*args, **kwargs)
    return wrapper


@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here is your {flavor} of ice cream")



version = "0.1.0"

# @click.command()
# @click.version_option(version)
# @click.argument("name", nargs = 2) 
# @click.option("-s", "--shout", type=bool, is_flag = True)
# @click.option("-a", "--age", type=int, default=0)
# def func(name:list[str], age:int, shout:bool ) -> None:
#     text = f"Hello {" ".join(name)}, you are {age} "
#     if shout:
#         print(text.upper())
#     else:
#         print(text)












if __name__ == "__main__":
    get_ice_cream("vanilla")


