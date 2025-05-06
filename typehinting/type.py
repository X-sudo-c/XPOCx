

def add(x,y):
    return x + y #this is how a basic function looks like


def addint(x:int , y:int) -> int:
    return x + y

# this is how a function looks like with type hinting



#now lets do a function that prints happy burthday 3 times

"""python is dynamically typed and that means
it can take any value as a type and it would
still process it but this can end up breaking
your code i think lol"""


def my_func(name,  age): 
    print(f"Happy birthday {name}")
    print(f"Youve turned {age} today.")
    print (f"So you long story short {name} and you are {age}")
    print(type(name), type(age))



"""In the second function we define the type of data we are expecting and the type of data that it returns"""

def my_2ndFunction(name: str, age : int) -> str:
     print(f"Happy birthday {name}")
     print(f"Youve turned {age} today.")
     print (f"So you long story short {name} and you are {age}")

     print(type(name), type(age) )

     

    








my_func("Aheng",18)
print("\n")
my_2ndFunction("jr", 199)

