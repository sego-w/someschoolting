# C. The way to home
import collections
def main():

    '''
    n, d = [int(i) for i in input().split()]
    s = input()
    frog_home = 0
    steps_home = 0
    current_pos = 0
    if len(s)==n:
        for i in range(n):
            for j in range(d):
                if s[current_pos+d-j] == '1':
                    steps_home += 1
                    current_pos = d-j
        if current_pos == len(s):
            frog_home = 1
                    
    else:
        exit()

    if frog_home == 0:
        print(-1)
    else:
        print(steps_home)
    '''
    n,d = map(int, input().split())
    vesiroosid = [None] + [x == "1" for x in input()]
    oldud = set()
    oldud.add(1)
    
    # jarjekord = [(1,0)]
    jarjekord = collections.deque()
    jarjekord.append((1,0))
    valmis = False
    while len(jarjekord) > 0 and not valmis:
        # eemaldab esimese elemendi ja tagastab selle
        koht, hyppeid = jarjekord.popleft()
        for hype in range(1, d+1):
            uus_koht = koht + hype
            if vesiroosid[uus_koht] and uus_koht not in oldud:
                if uus_koht == n:
                    valmis = True
                    print(hyppeid+1)
                    break
                jarjekord.append((uus_koht,hyppeid+1))
                oldud.add(uus_koht)

    if not valmis:
        print("-1")


main()   