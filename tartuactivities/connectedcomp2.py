# B. Connected Components 2


def main():
    n, m = (int(i) for i in input().split(" "))

    tipu_naabrid = [[] for j in range(n+1)]
    tipu_nimed = {}

    for x in range(m):
        an, bn = input().split()
        if an not in tipu_nimed:
            tipu_nimed[an] = len(tipu_nimed)+1
        if bn not in tipu_nimed:
            tipu_nimed[bn] = len(tipu_nimed)+1
        a = tipu_nimed[an]
        b = tipu_nimed[bn]
        tipu_naabrid[a].append(b)
        tipu_naabrid[b].append(a)

        

    nagemata_tipud = set(range(1,n+1))
    sidususkomponentide_arv = 0

    
    def sygavuti(tipp):
        praegu_vaadatavad = [tipp]
        while len(praegu_vaadatavad) > 0:
            tipp = praegu_vaadatavad.pop()
            for naaber in tipu_naabrid[tipp]:
                if naaber in nagemata_tipud:
                    nagemata_tipud.remove(naaber)
                    praegu_vaadatavad.append(naaber)

    while len(nagemata_tipud) > 0:
        sidususkomponentide_arv +=1
        tipp = nagemata_tipud.pop()
        sygavuti(tipp)
            
    print(sidususkomponentide_arv)

main()