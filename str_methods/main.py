

name = input("Enter your full  name:")

result = len(name)  #I know this already just doing it because theres nothing like too much coding 

print(result) #returns the the output as a string


find = name.find(" ") #this looks for the first occurence of a space " "  in the string if we do name.find("w") the first instance of the letter "w" in the string and then report it to us 

print(find)#it returns an integer showing the position  of the what ever you define in this example  we did name.find("")



print(name.capitalize())#makes the first Letter a Capital letter

print(name.upper())#makes the whole word uppercase

print(name.lower())#makes all the letters lower

print(name.isdigit())#checks to see of theres a digit in it the data is a digit 






if name == name.isdigit():
    print("This is a digit yayyy")