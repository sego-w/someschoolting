def main():
    p = []
    x = input()
    for i in range(int(x)):
        l = input()
        p.append(l)
    z= []
    for s in p:
        z.append(s.split())
    w = 0
    for i in range(int(x)):
        w += (int(z[i][1]) - int(z[i][0]))
        
    if w<0:
        print("MIINUSES")
    elif w==0:
        print("TASA")
    else:
        print("PLUSSIS")
    
    

main()