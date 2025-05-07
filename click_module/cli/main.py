import click 
from typing import List



version = "0.1.0"

@click.command()
@click.argument("name", nargs = 2)
@click.option("--age", "-a", type = int , default = None)
@click.option("-s","--shout", type=bool, is_flag =True)


def profile(name:List[str], age:str, shout:bool ) -> None:
    text = f"Hey there {" ".join(name)} you are {age} years old"

    if shout:
        print(text.upper())
    else:
        print(text)





if __name__ == "__main__":
    profile()

