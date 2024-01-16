def main():

    n = int(input())
    a = sorted(map(int, input().split()))

    sum_diff = 0
    for i in range(n):
        sum_diff += a[i] * (i - (n - 1 - i))

    print(sum_diff)
    
main()