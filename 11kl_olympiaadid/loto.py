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
    elif w>0:
        print("PLUSSIS")
    else:
        print("EI TEA")
    
    win = []
    loss = []
    for q in z:
        if int(q[1]) - int(q[0]) < 0:
            loss.append(int(q[0]) - int(q[1]))
        else: 
            win.append(int(q[0]) - int(q[]))

    
    
    print(max(loss), loss.index(max(loss))+1)



    

main()