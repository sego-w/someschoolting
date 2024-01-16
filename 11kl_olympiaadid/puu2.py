import os
summa = 0
def uuri(asukoht):
    global summa
    kataloogipuhver = [asukoht]
    while len(kataloogipuhver)>0:
        uuritavkataloog=kataloogipuhver.pop()
        print(uuritavkataloog)
    print("\n"+asukoht,end=" ")
    if not os.path.isdir(asukoht):
        print(open(asukoht).read(), end="")
        summa+=int(open(asukoht).read())
    else:
        print(" "+nimetus)
        for nimetus in os.listdir(asukoht):
            uuri(asukoht+"/"+nimetus)
        '''
        for nimetus in os.listdir(asukoht):
            with open(nimetus,"r") as x:
                print(x)
            uuri(asukoht+"/"+nimetus)
        '''


uuri("11kl_olympiaadid/puu2")
print(summa)

#print(sum([int(s) for s in hoidla]))
