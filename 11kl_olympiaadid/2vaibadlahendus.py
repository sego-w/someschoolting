# opetajaga koos tehtud

f=open("/Users/gustavtamkivi/Documents/Code/someschoolting/11kl_olympiaadid/vaibad.txt")
K,L,P = [int(jupp) for jupp in f.readline().strip().split(" ")]

m=[[0]*L for nr in range(P)]


for nr in range(K):
    N,S,E,W = [int(jupp) for jupp in f.readline().strip().split(" ")]
    
#   print((L-E-W)*(P-N-S))
    for veerg in range(W, L-E):
        for rida in range(N, P-S):
            m[rida][veerg] = 1
        
# print("\n".join([str(lahter) for lahter in rida]) for rida in m)
'''
for rida in m:
    print(*[str(lahter) for lahter in rida])
'''
x=0
for rida in m:
    for lahter in rida:
        x+=lahter

print(f"Vaibad katavad kogupindaala {x} ruutyhikut")



'''
2 8 9
3 3 3 0
5 1 2 4
'''