def main():
    
    origincount = []
    corrupts = []
    x = int(input())
    for i in range(x):
        origincount.append(int(input()))
        corrupts.append(input())
    print(origincount)
    print(corrupts)
    for el in range(len(corrupts)):
        y = int(len(corrupts[el]) / origincount[el])
        print(1)
        print(corrupts[el][0:y])



    '''
    def decrp(c, k):
        o = c[::k]
        print(c)
        print(o)

    n = int(input())

    for _ in range(n):
        k = int(input())
        c = input()
        decrp(c, k)
    '''
main()