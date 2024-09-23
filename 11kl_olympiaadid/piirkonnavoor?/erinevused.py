def main():

    n = int(input())
    a = sorted(map(int, input().split()))

    sum_diff = 0
    for i in range(n):
        sum_diff += a[i] * (2 * i - n + 1)

    print(sum_diff)

main()