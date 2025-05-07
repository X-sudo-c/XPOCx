# validate user input exercise

# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits



while True:
    try:
        username = input("input your username! :")

        if len(username) > 12:
            print("username should be more than 12 characters long")
        elif " " in username :
            print("no whitespaces allowed")
        elif  username.isnumeric() == True:
            print("No digits allowed in this mayin ")
        else:
            print(f"Welcome {username} ")
            break
    except TypeError as e:
        print(f"You manged to mess up the logic in this mayin here you go [{e}]")
