def nak():
    setup = input().split(" ")
    setup = [eval(i) for i in setup]
    n = setup[0]
    q = setup[1]
#    if 11<=n<=200000 and 1<=q<=300000:
    v = input().split(" ")
    v = [eval(i) for i in v]
#    if min(v) >= 16 and max(v) <=56:
    l_r = []
    for j in range(q):
        l_r.append(input().split(" "))
        
    plannedgroup = []
    for plans in l_r:
        #if int(plans[1]) -int(plans[0]) + 1 == 11:
        plannedgroup.append(v[int(plans[0]):int(plans[1])+1])
            
    for teams in plannedgroup:
        teams.sort()
        youngestgroup = teams[0:11]
        print(max(youngestgroup))
                
            
    


    

nak()