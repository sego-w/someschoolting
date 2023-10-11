def avaldis():

    lol = input()
    z = lol.split(" ")
    if int(z[0]) != 0 and int(z[0]) != 1 and int(z[0]) != -1:
        if int(z[1]) > 0:
            print(f"{z[0]}x+{z[1]}")
        elif int(z[1]) == 0:
            print(f"{z[0]}x")
        else:
            print(f"{z[0]}x{z[1]}")
    elif int(z[0]) == 0:
        if int(z[1]) > 0:
            print(f"{z[1]}")
        elif int(z[1]) == 0:
            print("")
        
        else:
            print(f"{z[1]}")
    elif int(z[0]) == 1:
        if int(z[1]) > 0:
            print(f"x+{z[1]}")
        elif int(z[1]) == 0:
            print("x")
        else:
            print(f"x{z[1]}")
    elif int(z[0]) == -1:
        if int(z[1]) > 0:
            print(f"-x+{z[1]}")
        elif int(z[1]) == 0:
            print("-x")
        else:
            print(f"-x{z[1]}")
avaldis()