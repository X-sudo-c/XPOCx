x = "global x"



def level_six():
    z = "outer z"

    def donky():
        def inner(y):
            return x, y, z