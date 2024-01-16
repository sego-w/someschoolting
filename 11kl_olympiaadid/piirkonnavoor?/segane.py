def main():

    def decrp(c, k):
        o = c[::k]
        print(c)
        print(o)

    n = int(input())

    for _ in range(n):
        k = int(input())
        c = input()
        decrp(c, k)

main()