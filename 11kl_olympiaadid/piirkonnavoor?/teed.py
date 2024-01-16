def main():
    x = []
    for i in range(3):
        x.append(int(input()))
    if x[0] == 1 or x[0] == 3:
        if x[1] == 6 or x[1] == 8:
            if x[2] == 2 or x[2] == 5:
                print("JAH")
            else:
                print("EI")
        else:
            print("EI")
    else:
        print("EI")
    
main()