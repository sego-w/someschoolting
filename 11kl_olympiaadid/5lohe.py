with open("/Users/gustavtamkivi/Documents/Code/someschoolting/11kl_olympiaadid/lohegsis.txt", "r") as x:
    lines = [ line.strip() for line in x ]

dumbshit = [ z.split(' ') for z in lines]


dumbshit[1] = [ eval(x) for x in dumbshit[1] ]
dumbshit[1].sort()

x = 0
for i in range(int(dumbshit[0][1])*2):
    x+= dumbshit[1][-i-1]

print(x)
    




        