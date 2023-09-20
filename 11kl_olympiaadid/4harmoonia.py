def main():
    
    with open("/Users/gustavtamkivi/Documents/Code/someschoolting/11kl_olympiaadid/hargsis.txt","r+") as x:
        q = []
        for lines in x:
            q.append(lines.strip())
        
    z = []
    for x in q:
        z.append(x.split(" "))
    
    
    
    for i in range(len(z)):
        funkshun = (int(z[i-1][1]) - int(z[i-1][0])) % 7
        if funkshun == 12:
            print(1)
        else:
            print("POLE")



main()