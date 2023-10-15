from random import uniform
from random import randint

def eki():
    tests = int(input())
    for i in range(tests):
        n_m = [eval(x) for x in input().split(" ")]
        countries = []
        comparisons = []
        for j in range(n_m[0]):
            countries.append(input().split(" "))
        for k in range(n_m[1]):
            comparisons.append(input().split(" ")) 
        for l in range(n_m[1]):
            x=0
            check1 = int(comparisons[l][0])-1
            check2 = int(comparisons[l][1])-1
            for i in range(5):
                l1 = uniform(0,10)
                l2 = uniform(0,10)
                l3 = uniform(0,10)
                valtest1 =  l1*int(countries[check1][0]) + l2*int(countries[check1][1]) + l3*int(countries[check1][2])
                valtest2 =  l1*int(countries[check2][0]) + l2*int(countries[check2][1]) + l3*int(countries[check2][2])
                if valtest1 > valtest2:
                    x+=1
            if x == 0:
                print('EI')
            else:
                print('JAH')





    


eki()