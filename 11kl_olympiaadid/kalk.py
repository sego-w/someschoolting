import re,random
def main():
    x = 0
    inn = re.split("[+ * / -]",input())

    for i in range(len(inn)):
        r = random.randint(0,3)

        if r == 0:
            x += int(inn[i])
        elif r == 1:
            x *= int(inn[i])
        elif r == 2:
            x /= int(inn[i])
        else:
            x -= int(inn[i])
    print(x)

main()