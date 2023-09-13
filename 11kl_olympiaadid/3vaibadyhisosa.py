f=open("/Users/gustavtamkivi/Documents/Code/someschoolting/11kl_olympiaadid/vaibad.txt")
K,L,P = [int(jupp) for jupp in f.readline().strip().split(" ")]

n1, s1, e1, w1 = [int(jupp) for jupp in f.readline().strip().split(" ")]
n2, s2, e2, w2 = [int(jupp) for jupp in f.readline().strip().split(" ")]

'''
if e1 < L - w2 or w1 > L - e2:
    print(f"Yhisosa piirkond x-telge pidi on {abs(L-e1-e2)}")
'''

p1=L-e1
p2=L-e2
a1=P-s1
a2=P-s2

yhisxpikkus=max(min(p1,p2) - max(w1,w2), 0)
yhisypikkus=max(min(a1,a2) - max(n1,n2), 0)
print(yhisxpikkus*yhisypikkus)
