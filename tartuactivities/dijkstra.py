# E dijkstra?
import heapq
def main():

    n, m = map(int,input().split())
    tipu_naabrid = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        if b in tipu_naabrid[a]:
            w = min(w,tipu_naabrid[a][b])
        tipu_naabrid[a][b] = w
        tipu_naabrid[b][a] = w




    import heapq
    jarjekord = []
    heapq.heappush(jarjekord, (0,0))
    nahtud = set()
    eellased = {}
    tipp_parim = {}

    while len(jarjekord) > 0:
        kaal, tipp, eellane = heapq.heappop(jarjekord)
        if tipp in nahtud:
            continue
        
        

        nahtud.add(tipp)  
        eellased[tipp] = eellane
        if tipp == n-1:
            break

        for naaber,servakaal in tipu_naabrid[tipp].items():
            uus_kaal = kaal + servakaal
            if naaber not in tipp_parim or uus_kaal <tipp_parim[naaber]:

                heapq.heappush(jarjekord, (uus_kaal,naaber, tipp))
                tipp_parim[naaber] = uus_kaal
                eellased[naaber] = tipp

    if n-1 not in eellased:
        print(-1)
    else:
        teekond = [n-1]
        while teekond[-1] != 0:
            teekond.append(eellased[teekond[-1]])
        teekond.reverse()
        for i in range(len(teekond)):
            teekond[i] += 1
        print(*teekond)
main()